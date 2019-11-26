from django.db import models

# If you would like to use Django's Auth user model, uncomment the next line
from django.contrib.auth.models import User

# Define your Sublet Application models here
# Example:
# class Foo(models.Model):
#     """Foo represents a real-world foo.
#    
#     If a Foo is active then it can be borked by any Zoot.
#     ... (other non-trivial comments)
#     """
#     bar = models.CharField(max_length=16, default="")
#     ... Your other fields go below


class Apartment(models.Model):
    TYPES=[(1,'Beach House'),(2,"High Rise Apt"),(3,"Town House")]
    LOCATIONS=[(1,"Inner City"),(2,"Outer City"),(3,"Suburbs")]
    PETS=[(True,"Pet friendly"),(False,"No Pets Allowed")]
    owner=models.ForeignKey(User, on_delete=models.CASCADE) #attached to owner, one owner can have multiple apartments. Apartments cannot have multiple owners
    customer=models.ForeignKey(User, on_delete=models.CASCADE) #attached to customer, one customer can book multiple apartments. Apartments cannot be booked by multiple customers.
    address=models.IntegerField(max_length=5)
    availableStart=models.DateField()
    availableEnd=models.DateField()
    price=models.IntegerField()
    booked=models.BooleanField()
    type=models.IntegerField(choices=TYPES)
    location=models.IntegerField(choices=LOCATIONS)
    pet=models.BooleanField(choices=PETS)

def user_registration(nameInput):
    #create user
    #using user Django auth user model
    user=User.objects.create(name=nameInput)
    user.save()

def list(username,postcode,dates,priceTag):
    #for apartment with that postcode
    #add available dates to availableStart and availableEnd
    #add price


    pass

def book(username,postcode):
    #search user by username
    #search apt by address
    #check if booked
    #if not booked, book it
    apt=Apartment.objects.get(address=postcode)
    if apt.booked==False:
        apt.customer=User.objects.get(name=username)
        apt.booked=True
        print(username,"has booked apartment ",postcode)

    else:
        print("Booking failed, apartment taken")

def search(dates,typeInput,locationInput,pets):
    # Query apartments, if not booked and within dates given, filter by type of apartment, location and if pets allowed
    pass

def display_user(username):
    #search username. display all apartments owned by user.
    # If not booked and listed, display apartments.
    #Show apartments booked bu user with end dates after current date

    pass

def display_apartment(address):
    #search by address
    #show owner, hide customer for privacy reasons. type of apartment, location, pet policy, listing time (if listed), booked or not, price
    pass