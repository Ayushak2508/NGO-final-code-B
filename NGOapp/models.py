from django.db import models
from django.utils.timezone import now

class VolunteerApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    interests = models.TextField(help_text="What would you like to help with?")
    photo = models.ImageField(upload_to='volunteers/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"


# models.py


class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.PositiveIntegerField()  # Amount in INR paisa (e.g. 50000 = ₹500)
    payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - ₹{self.amount/100:.2f}"

# Create your models here.



class Banner(models.Model):
    image_url = models.URLField(max_length=255)
    title = models.CharField(max_length=150)
    description = models.TextField()
    order = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class VisionMission(models.Model):
    vision_title = models.CharField(max_length=150)
    vision_description = models.CharField(max_length=200)
    mission_title = models.CharField(max_length=150)
    mission_description = models.CharField(max_length=200)
    last_updated = models.DateTimeField(default=now)

    def __str__(self):
        return "Vision & Mission"

class Statistic(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    order = models.CharField(max_length=150)
    status = models.CharField(max_length=50, default='active')  # 'active' or 'inactive'

    def __str__(self):
        return self.label

class Initiative(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image_url = models.URLField(max_length=150)
    order = models.IntegerField(default=0)
    status = models.TextField(default='active')  # 'active' or 'inactive'

    def __str__(self):
        return self.title
