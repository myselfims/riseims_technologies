from django.shortcuts import render
from .models import *
from django.core.mail import send_mail

# Create your views here.
def home(request):
    contact = ContactDetail.objects.get(id = 1)
    return render(request,'base.html',{'contact':contact})

def services(request):
    reviews = Review.objects.all()
    contact = ContactDetail.objects.get(id = 1)
    services = Services.objects.all()
    return render(request,'services.html',{'services':services,'reviews':reviews,'contact':contact})

def pricing(request):
    plans = Plan.objects.all()
    contact = ContactDetail.objects.get(id = 1)
    plandetails = PlanDetail.objects.all()
    return render(request,'pricing.html',{'plans':plans,'plandetails':plandetails,'contact':contact})
    
    

def booking(request,id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        desc = request.POST.get('desc')
        booking = Booking(plan=id,name=first_name+last_name,email=email,mobile=mobile,desc=desc)
        booking.save()
        plan = Plan.objects.get(id=id)
        try:
            send_mail(
                'Sir we have a new booking!!!',
                f'Here is the clients details : Name : {first_name} {last_name}, email : {email}, mobile: {mobile}, description : {desc}, Plan : {id}',
                'riseimstechnologies@gmail.com',
                ['shaikhimran7585@gmail.com'],
                fail_silently=False,
            )
        except:
            pass
        return render(request,'booking.html',{'submitted':True,'plan':plan})
    
    plan = Plan.objects.get(id=id)
    return render(request,'booking.html',{'plan':plan})


def contact_us(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        message = Message(name=first_name+last_name,email=email,mobile=mobile,message=message)
        message.save()

        return render(request,'contact.html',{'submitted':True})
    return render(request, 'contact.html')