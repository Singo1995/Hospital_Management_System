from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    d = 0;
    p = 0;
    a = 0;
    for i in doctor:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    d1 = {'d':d,'p':p,'a':a}
    return render(request,'index.html',d1)
def Login(request):
    error = ""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u,password = p)
        try:
            if user.is_staff:
                login(request,user)
                error ="no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    # print(type(Doctor.objects.all()))
    doc = Doctor.objects.all()
    d = {'doc':doc}
    # print(type(d))
    return render(request,'view_doctor.html',d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    # print(type(Doctor.objects.all()))
    pat = Patient.objects.all()
    d = {'pat':pat}
    # print(type(d))
    return render(request,'view_patient.html',d)

def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=c,special=sp)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'add_doctor.html',d)
def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
        try:
            Patient.objects.create(name=n,gender=g,mobile=m,address=a)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'add_patient.html',d)
def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')
def Delete_Patient(request,ptid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=ptid)
    patient.delete()
    return redirect('view_patient')
def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=d1,time1=t)
            error = "no"
        except:
            error = "yes"
    d = {'patient':patient1,'doctor':doctor1,'error':error}
    return render(request,'add_appointment.html',d)

def Delete_Appointment(request,paid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=paid)
    appointment.delete()
    return redirect('view_appointment')

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    # print(type(Doctor.objects.all()))
    appoint = Appointment.objects.all()
    d = {'appoint':appoint}
    # print(type(d))
    return render(request,'view_appointment.html',d)