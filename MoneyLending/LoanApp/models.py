from django.db import models
from django.contrib.auth.models import User
from UserApp.models import Borrower
from uuid import UUID
from uuid import uuid4
# Create your models here.

class Loan(models.Model):
	loanID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	borrower = models.ForeignKey(Borrower,on_delete=models.CASCADE)
	Amount = models.IntegerField(null=False)
	InterestR = models.IntegerField()
	time = models.IntegerField(null=False)
	
	def __str__(self):
		return self.loanID

class loanDetails(models.Model):
	loanID = models.ForeignKey(Borrower,on_delete=models.CASCADE)
	lender = models.ForeignKey(User,on_delete=models.CASCADE)
	LendedAmt = models.IntegerField(null=False)
	MonthlyEMI = models.IntegerField()

	def __str__(self):
		return self.loanID
