from django.db import models
import re
import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class TripManager(models.Manager):
	def tripValidator(self, form):
		destination = form['destination']
		trip_reason = form['reason_for_trip']
		departure_date = form['departure_date']
		return_date = form['return_date']
		errors = {}

		if not destination:
			errors['destination'] = "Please provide a destination for your trip!"
		elif len(destination) < 2:
			errors['destination'] = "Your destination must contain at least two characters."

		if not departure_date:
			errors['departure_date'] = "Please provide a departure date for your trip!"
		elif len(departure_date) > 10:
			errors['return_date'] = "Your trip cannot exist that far into the future."
		elif departure_date > return_date:
			errors['departure_date'] = "Your trip cannot begin after it has ended."

		if not return_date:
			errors['return_date'] = "Please provide a return date for your trip!"
		elif len(return_date) > 10:
			errors['return_date'] = "Your trip cannot exist that far into the future."
		elif return_date < departure_date:
			errors['return_date'] = "Your trip cannot end before it has begun."

		return errors

class UserManager(models.Manager):
	def regValidator(self, form):
		name = form['name']
		username = form['username']
		password = form['password']
		confirm_pw = form['confirm_pw']
		errors ={}

		if not name:
			errors['fullname'] = "Name can not be blank"
		elif len(username) < 3:
			errors['fullname'] = "Name must be atleast 3 characters"

		if not username:
			errors['username'] = "Username can not be blank"
		elif len(username) < 3:
			errors['username'] = "Username must be atleast 3 characters"
		elif User.objects.filter(username=username):
			errors['username'] = "Username already exists. Please log in."

		if not password:
			errors['reg_password'] = "Password can not be blank"
		elif len(password) < 8:
			errors['reg_password'] = "Password must be 8 characters"
		if not confirm_pw:
			errors['confirm_pw'] = "Please confirm password"
		elif password != confirm_pw:
			errors['confirm_pw'] = "Passwords do not match"



		return errors
	def loginValidator(self, form):
		username = form['loginusername']
		password = form['loginpass']

		errors = {}

		if not username:
			errors['loginusername'] = "Please enter username to log in."
		elif not User.objects.filter(username=username):
			errors['loginusername'] = "Username not found. Please register."
		else:
			if not password:
				errors['loginpass'] = "Password required"
				return errors, False
			else:
				user = User.objects.get(username=username)
				if not bcrypt.checkpw(password.encode(), user.password.encode()):
					errors['loginpass'] = "Incorrect password. Please try again."
			return errors, user
		return errors, False

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	#tripsAdded --> one to many join (trips added_by this user)
	#joinTrip --> many to many join

class Trips(models.Model):
	destination = models.CharField(max_length=255)
	departure_date = models.DateTimeField()
	return_date = models.DateTimeField()
	reason_for_trip = models.CharField(max_length=500)
	added_by = models.ForeignKey(User, related_name = 'tripsAdded', on_delete=models.CASCADE)
	joined_by = models.ManyToManyField(User, related_name = 'joinTrip')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = TripManager()
