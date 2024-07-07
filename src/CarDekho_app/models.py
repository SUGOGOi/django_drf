from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User



#***********************************VALIDATOR FOR CAR_LIST*********************
def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError('Only alphanumeric character')
    return value


#********************************SHOWROOM MODEL********************************
class ShowroomList(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

#*********************************CAR MODEL************************************
class CarList(models.Model):
    name  = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length=100, blank=True, null=True, validators=[alphanumeric])
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    showroom = models.ForeignKey(ShowroomList, on_delete=models.CASCADE, related_name="cars", null=True)

    def __str__(self):
        return self.name


#*********************************REVIEW MODEL************************************
class Review(models.Model):
    apiuser = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator, MaxValueValidator])
    comments = models.CharField(max_length=300, null=True)
    car = models.ForeignKey(CarList, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car.name + " : "+ str(self.rating)+", by "+ self.apiuser.username