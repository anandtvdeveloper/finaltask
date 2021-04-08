from django.contrib import admin
from .models import Department,Doctor,Booking
# Register your models here.
admin.site.register(Booking)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Department, DepartmentAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Doctor, DoctorAdmin)
