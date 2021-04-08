from django.db import models

# Create your models here.
from django.urls import reverse


class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='category')

    class Meta:
        ordering=('name',)
        verbose_name='department '
        verbose_name_plural='departments'

    def get_url(self):
        return reverse("DataApp:department_by_category", args=[self.slug])


    def __str__(self):
        return '{}'.format(self.name)


class Doctor(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    category=models.ForeignKey(Department,on_delete=models.CASCADE)
    class Meta:
        ordering=('name',)
        verbose_name='doctor '
        verbose_name_plural='doctors'

    def __str__(self):
        return '{}'.format(self.name)

class Booking(models.Model):
    name = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField()
    dept = models.CharField(max_length=250)
    doc = models.CharField(max_length=250)
    date = models.CharField(max_length=250)