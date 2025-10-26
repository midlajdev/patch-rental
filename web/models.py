from django.db import models


FAQ_TYPE=(
    ("rent_tracking","Rent Tracking"),
    ("new_deposite","New Deposite"),
    ("existing_deposite","Existing Deposit")
)

class Testimonial(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="testimonials/")
    designation=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.name


class Promoter(models.Model):
    name=models.CharField(max_length=225)
    image=models.ImageField(upload_to="promoters/")

    def __str__(self):
        return self.name


class Faq(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField()
    faq_type=models.CharField(max_length=128,choices=FAQ_TYPE)
    
    def __str__(self):
        return self.title


class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email