from django.db import models
from django.contrib.auth.models import User
# Create your models
class UserProfileInfo(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)
	#additional
	DOB = models.DateField()
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

	def __str__(self):
		return self.user.username

#we will make new db now
class Borrower(models.Model):
	borrower = models.OneToOneField(User,on_delete=models.CASCADE)
	CreditScore = models.IntegerField()
	TLoanAmt = models.IntegerField()
	def __str__(self):
		return self.user.username

