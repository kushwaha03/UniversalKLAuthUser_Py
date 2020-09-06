from .managers import UserKLManager
from django.db import models
# Import default django models
from django.contrib.auth.models import AbstractBaseUser
# Import Project models
from django.contrib.auth.models import PermissionsMixin
# Import Additonal Django Models
import pdb
import uuid

from django.contrib.auth.signals import user_logged_in
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from guardian.mixins import GuardianUserMixin


from django.conf import settings
from django.urls import reverse_lazy

# mailing libraries
from django.core.mail import send_mail
#OTP library


class UserKL(GuardianUserMixin, AbstractBaseUser,PermissionsMixin):
	id 					= models.AutoField(primary_key=True)
	email				= models.EmailField(max_length=255, unique=True,  null=False, blank=False)
	FirstName			= models.CharField(max_length=255)
	LastName			= models.CharField(max_length=255,null=True)
	UserIDKL			= models.UUIDField(default=uuid.uuid4, editable=False,blank=True, unique=True)
	# Country 			= models.CharField()
	LKD					= models.CharField(max_length=255,null=True,default='')
	FB 					= models.IntegerField(null=True,default=0)
	GPlus 				= models.IntegerField(null=True,default=0)
	KL 					= models.IntegerField(null=True,default=0)
	LearnNet			= models.IntegerField(null=True,default=0)
	BookNet 			= models.IntegerField(null=True,default=0)
	SigMa				= models.IntegerField(null=True,default=0)
	Pi 					= models.IntegerField(null=True,default=0)
	CurrentRefferalID 	= models.CharField(max_length=255,default='KarmaaLab')
	PreviousRefferalID 	= models.CharField(max_length=255,default='KarmaaLab')
	active 				= models.BooleanField(default=True)
	is_staff			= models.BooleanField(default=False)
	email_verified 		= models.BooleanField(default=False)
	createdOn			= models.DateTimeField(auto_now_add=True)
	ModifiedOn			= models.DateTimeField(auto_now=True)
	username            = models.CharField(max_length=50 , unique=True , blank=True , null=True)
	objects = UserKLManager()
	class Meta:
		verbose_name = ('UserKL')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['FirstName']

	def get_full_name(self):
		'''
		Returns the first_name plus the last_name, with a space in between.
		'''
		full_name = '%s %s' % (self.FirstName, self.LastName)
		return full_name.strip()

	def get_short_name(self):
		'''
		Returns the short name for the user.
		'''
		return self.FirstName
	def get_user_type(self):
		'''
		Returns the short name for the user.
		'''
		return 'UserKL'

	def __str__(self):              
		return self.email
	@property
	def is_active(self):
		"Is the user active?"
		return self.active
	@property
	def is_authenticated(self):
		"""
		Always return True. This is a way to tell if the user has been
		authenticated in templates.
		"""
		return True


def get_anonymous_user(self):
	user, _ = UserKL.objects.get_or_create(
	    email=settings.ANONYMOUS_USER_NAME,
	    PreviousRefferalID='guardian',
	    CurrentRefferalID = 'guardian',

	)
	return user

