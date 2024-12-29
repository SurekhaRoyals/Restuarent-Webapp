from django.db import models

# Create your models here. DataBase schema
class ItemList(models.Model):
    Category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList,related_name="Name", on_delete=models.CASCADE)
    Image = models.ImageField(upload_to="Items/")

    def __str__(self):
        return self.Item_name
    
class Home(models.Model):
    Intro = models.TextField(blank=False) 
    def __str__(self):
        return self.Intro  

class AboutUs(models.Model):
    description = models.TextField(blank=False)

    def __str__(self):
        return self.description

class Feedback(models.Model):
    User_name = models.CharField(max_length=20)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to="items/", blank=True) 


    def __str__(self):
        return self.User_name

class BookTable(models.Model):
    Name = models.CharField(max_length=20)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name
