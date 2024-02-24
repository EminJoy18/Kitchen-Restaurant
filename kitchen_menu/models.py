from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"), # EACH TUPLE HAS TWO STRINGS
    ("salads", "Salads"),
    ("main_course", "Main Course"),
    ("desserts", "Desserts"),
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available"),
)

# Create your models here.
class Menu(models.Model):
    Name = models.CharField(max_length=200, unique=True)
    Description = models.CharField(max_length=1000)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Meal_type = models.CharField(max_length=20, choices=MEAL_TYPE)
    Author = models.ForeignKey(User, on_delete = models.PROTECT, default=2)
    # JUST LIKE WE ARE CREATING THE MENU TABLE IN THE DATABASE,
    # 'USER' IS ANOTHER TABLE IN THE DATABASE which contains username and user password as fields
    # with FOREIGNKEY, WE ARE CREATING A RELATIONSHIP B/W THE Menu and User tables (MANY TO ONE RELATIONSHIP)
    # MANY ITEMS CAN BE ASSOCIATED WITH A SINGLE USER

    # suppose a user is deleted => so models.CASCADE deletes all the dishes that the particular user added

    # models.PROTECT => does not allow the deletion of user, and hence the dishes also wont be deleted

    # models.SET_NULL => even if the User is deleted, the dish wont be deleted. Author field will be set to null 


    status = models.IntegerField(choices=STATUS, default=1) 

    created_at = models.DateTimeField(auto_now_add = True)
    updates_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name
    


class UserFeedback(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank=False)
    message = models.CharField(max_length = 1000)