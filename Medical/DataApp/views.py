from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Doctor,Department,Booking
# Create your views here.

def homepage(request,c_slug=None):
    obj1=Department.objects.all()
    c_page = None
    p = None
    if c_slug != None:
        c_page = get_object_or_404(Department,slug=c_slug)
        p = Doctor.objects.filter(category=c_page)
    else:
        p = Doctor.objects.all()
    return render(request, 'index.html',{'obj':c_page,'obj2': p,'obj1':obj1})

def demo(request):
    a = Department.objects.all()
    b = Doctor.objects.all()

    return render(request, 'doctor.html', {'demo1': a, 'demo2': b})

def display(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        dept = request.POST.get('dept')
        doc = request.POST.get('doc')
        date = request.POST.get('date')
        ob = Booking(name=name, phone=phone, email=email, dept=dept, doc=doc, date=date)
        ob.save()
    tt=Booking.objects.all()
    return render(request, 'details.html', {'tty': tt})
