


from django.shortcuts import render
from django.http import HttpResponse
from.models import ABC,signin,toppers,courses,courses1,courses2,Contact,Teach_us,index_us
from django.shortcuts import render, redirect
from django.contrib import messages, sessions
from .models import signin
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from django.contrib.auth import hashers


import os
def Signin(request):
    if request.method == "POST":
         name = request.POST.get('name')
         email = request.POST.get('email')
         password = request.POST.get('password')
         password=hashers.make_password(password)

         User.objects.create(username=name,email=email,password=password)
         messages.success(request, 'You have successfully signed up. Please sign in.')
         return redirect('login')  # Redirect to the login page after successful sign-up
    return render(request, "login_signup")

from django.contrib.auth import authenticate, login
from django.contrib import messages

def login1(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        users = authenticate(username=email, password=password)
        print(users.username)
        if users is not None:
            login(request, users)
            messages.success(request, 'You have successfully logged in.')
            e = toppers.objects.all()
            for x in e:
                x.image1 = os.path.basename(x.image1.url)
            d = ABC.objects.all()
            for i in d:
                i.image = os.path.basename(i.image.url)
            c = index_us.objects.all()
            for i in c:
                i.img2 = os.path.basename(i.img2.url)
            return render(request, "index.html", {'data': d, 'data1': e,'data3':c})
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
    return render(request, "login_signup.html")




def login_signup(request):
     return render(request, "login_signup.html")

def logoutUser(request):
    logout(request)
    return redirect('')
# def a2(request):
#     e=toppers.objects.all()
#     for x in e:
#           x.image1=os.path.basename(x.image1.url)
#     d=ABC.objects.all()
#     for i in d:
#           i.image=os.path.basename(i.image.url)
def a2(request):
    e=toppers.objects.all()
    for x in e:
          x.image1=os.path.basename(x.image1.url)
    d=ABC.objects.all()
    for i in d:
          i.image=os.path.basename(i.image.url)
    c=index_us.objects.all()
    for i in c:
         i.img2=os.path.basename(i.img2.url)
         
    return render(request,"index.html",{'data':d,'data1':e,'data3':c})

# Create your views here.
def courses_1(request):
     sh=courses1.objects.all()
     for z in sh:
          z.image12=os.path.basename(z.image12.url)
     return render(request,"course1.html",{'data13':sh})
def courses_2(request):
     ch=courses2.objects.all()
     for z1 in ch:
          z1.image121=os.path.basename(z1.image121.url)
     return render(request,"course2.html",{'data131':ch})


def contact(request):
     return render(request,"contactus.html")
def Courses(request):
    ed=courses.objects.all()
    for y in ed:
          y.image2=os.path.basename(y.image2.url)
    return render(request,"courses.html",{'data3':ed})
def teach_us(request):
     td=Teach_us.objects.all()
     for t in td:
          t.img1=os.path.basename(t.img1.url)
     return render(request,'Teach.html',{'tdata':td})
def home_details(request,hname,hid):
     hobj=ABC.objects.get(id=hid)
     # for c in cobj:
     hobj.syllabush=[x for x in hobj.syllabush.split('\n')]
     # print(cobj.syllabus[0])
     return render(request,'hcourse.html',{'hdata':hobj})



 

def contact_us(request):
    if request.method=="POST":
         name1=request.POST.get('name1')
         email1=request.POST.get('email1')
         message=request.POST.get('message')
         Contact.objects.create(name1=name1,email1=email1,message=message)
    return render(request,"contactus.html")

def govt(request):
     return render(request,"govt.html")
def course_details(request,cname,cid):
     cobj=courses.objects.get(id=cid)
     # for c in cobj:
     cobj.syllabus=[x for x in cobj.syllabus.split('\n')]
     # print(cobj.syllabus[0])
     return render(request,'info.html',{'cdata':cobj})
def govt_details(request,gname,gid):
     gobj=courses1.objects.get(id=gid)
     # for c in cobj:
     gobj.syllabus1=[x for x in gobj.syllabus1.split('\n')]
     # print(cobj.syllabus[0])
     return render(request,'govtinfo.html',{'gdata':gobj})
def school_details(request,sname,sid):
     sobj=courses2.objects.get(id=sid)
     # for c in cobj:
     sobj.syllabus2=[x for x in sobj.syllabus2.split('\n')]
     # print(cobj.syllabus[0])
     return render(request,'schoolinfo.html',{'sdata':sobj})
def search(request):
    query = request.GET.get('q')
    print(query)
    if query:
        results = courses.objects.filter(name2__icontains=query)
        for y in results:
          y.image2=os.path.basename(y.image2.url)
    else:
        results = courses.objects.none()
    return render(request, 'courses.html', {'data3': results})
def search(request):
    query = request.GET.get('q')
    print(query)
    if query:
        course_results = courses.objects.filter(name2__icontains=query)
        for course in course_results:
            course.image2 = os.path.basename(course.image2.url)
        
        if not course_results:
            course1_results = courses1.objects.filter(name12__icontains=query)
            for course1 in course1_results:
                course1.image12 = os.path.basename(course1.image12.url)
            
            if not course1_results:
                course2_results = courses2.objects.filter(name121__icontains=query)
                for course2 in course2_results:
                    course2.image121 = os.path.basename(course2.image121.url)

                return render(request, "course2.html", {'data131': course2_results})
            else:
                return render(request, "course1.html", {'data13': course1_results})
        else:
            return render(request, "courses.html", {'data3': course_results})
    else:
        results = courses.objects.none()
    return render(request, 'courses.html', {'data3': results})