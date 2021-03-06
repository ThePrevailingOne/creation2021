from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now
import pytz


class ChallengeStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, primary_key=True)
    register1 = models.BooleanField(default=False)
    submit1 = models.BooleanField(default=False)
    register2 = models.BooleanField(default=False)
    submit2 = models.BooleanField(default=False)
    register3 = models.BooleanField(default=False)
    submit3 = models.BooleanField(default=False)
    register4 = models.BooleanField(default=False)
    submit4 = models.BooleanField(default=False)
    registerSide = models.BooleanField(default=False)
    submitSide = models.BooleanField(default=False)

# Create your models here.
class Statement_1(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='challenge_statement_1')
    img_url = models.CharField(max_length=300, blank = True)
    raw = models.FileField(upload_to='challenge_statement_1')
    raw_url = models.CharField(max_length=300, blank = True)
    time = models.DateTimeField(default=now())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Statement_2(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='challenge_statement_2')
    img_url = models.CharField(max_length=300, blank = True)
    raw = models.FileField(upload_to='challenge_statement_2')
    raw_url = models.CharField(max_length=300, blank = True)
    time = models.DateTimeField(default=now())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Statement_3(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='challenge_statement_3')
    img_url = models.CharField(max_length=300, blank = True)
    raw = models.FileField(upload_to='challenge_statement_3')
    raw_url = models.CharField(max_length=300, blank = True)
    time = models.DateTimeField(default=now())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Statement_4(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='challenge_statement_4')
    img_url = models.CharField(max_length=300, blank = True)
    raw = models.FileField(upload_to='challenge_statement_4')
    raw_url = models.CharField(max_length=300, blank = True)
    time = models.DateTimeField(default=now())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    


class SideChallenge(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='side_challenge')
    img_url = models.CharField(max_length=300, blank = True)
    raw = models.FileField(upload_to='side_challenge')
    raw_url = models.CharField(max_length=300, blank = True)
    time = models.DateTimeField(default=now())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  


class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    inquiry = models.TextField()
