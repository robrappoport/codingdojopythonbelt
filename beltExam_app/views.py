from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
	return render(request, "index.html")
def addTrip(request):
	errors = Trips.objects.tripValidator(request.POST)
	print(errors)
	if errors:
		for key, value in errors.items():
			messages.error(request, value, extra_tags=key)
		return redirect("/newtrip")
	else:
		trip = Trips.objects.create(added_by_id = request.session['user_id'], destination = request.POST["destination"], departure_date = request.POST["departure_date"], return_date = request.POST['return_date'], reason_for_trip = request.POST['reason_for_trip'])
		user = User.objects.get(id = request.session["user_id"])
		user.joinTrip.add(trip)
		print(trip.departure_date)
		print(trip.return_date)
		return redirect("/dashboard")
def newTrip(request):
	if "user_id" not in request.session:
		return redirect("/")
	else:
		return render(request,"add.html")

def removeTrip(request, trip_id):
	trip = Trips.objects.get(id = trip_id)
	user = User.objects.get(id = request.session["user_id"])
	user.joinTrip.remove(trip)
	return redirect ("/dashboard")

def joinTrip(request, trip_id):
	trip = Trips.objects.get(id = trip_id)
	user = User.objects.get(id = request.session["user_id"])
	user.joinTrip.add(trip)
	return redirect ("/dashboard")

def viewTrip(request, trip_id):
	trip = Trips.objects.get(id = trip_id)
	all_users = trip.joined_by.exclude(id = int(trip.added_by.id))
	context={
		"trip":trip,
		"all_users":all_users
	}
	return render(request,"destination.html", context)

def logout(request):
	request.session.clear()
	return redirect("/")

def register(request):
	errors = User.objects.regValidator(request.POST)
	print(errors)
	if errors:
		for key, value in errors.items():
			messages.error(request, value, extra_tags=key)
		return redirect("/")
	else:
		hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(name = request.POST['name'], username = request.POST['username'], password = hash.decode())
		request.session['user_id']= user.id
		return redirect("/dashboard")

def dashboard(request):
	if "user_id" not in request.session:
		return redirect("/")
	else:
		user = User.objects.get(id=request.session['user_id'])
		all_destinations = Trips.objects.all()
		user_destinations = user.joinTrip.all()
		context={
			"user": user,
			"user_destinations": user_destinations,
			"all_destinations": all_destinations,
			"other_destinations": all_destinations.difference(user_destinations)
		}
		return render(request, "dashboard.html", context)
def login(request):
	result = User.objects.loginValidator(request.POST)
	print(result)

	if result[0]:
		for key, value in result[0].items():
			messages.error(request,value,extra_tags=key)
			return redirect('/')
	else:
		request.session["user_id"] = result[1].id
		return redirect("/dashboard")