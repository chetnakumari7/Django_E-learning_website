from django.db import models

from django.contrib.auth.models import User



# Create your models here.
class ABC(models.Model):
     image=models.ImageField(upload_to='statics/images',default='a')
     name=models.CharField(max_length=50,default='a')
     price=models.CharField(max_length=20,default='Rs.25000')
     texth3=models.CharField(max_length=200,default='text')
     descriptionh=models.TextField(default='')
     texth4=models.CharField(max_length=200,default='text')
     descriptionh1=models.TextField(default='')
     texth5=models.CharField(max_length=200,default='text')
     descriptionh2=models.TextField(default='')
     syllabush=models.TextField(default='')
class signin(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50,default='a')
    def str(self):
        return self.name
class Contact(models.Model):
    name1=models.CharField(max_length=50)
    email1=models.CharField(max_length=50)
    message=models.CharField(max_length=200,default='a')
    def str(self):
        return self.name
class toppers(models.Model):
    image1=models.ImageField(upload_to='statics/images',default='a')
    text=models.CharField(max_length=200,default='text')
class courses(models.Model):
    image2=models.ImageField(upload_to='statics/images',default='a')
    name2=models.CharField(max_length=200,default='text')
    back_name=models.CharField(max_length=200,default='text')
    text2=models.CharField(max_length=200,default='text')
    text3=models.CharField(max_length=200,default='text')
    text4=models.CharField(max_length=200,default='text')
    text5=models.CharField(max_length=200,default='text')
    description=models.TextField(default='')
    text6=models.CharField(max_length=200,default='text')
    descriptionn=models.TextField(default='')
    text7=models.CharField(max_length=200,default='text')
    descriptionnn=models.TextField(default='')
    syllabus=models.TextField(default='')
class courses1(models.Model):
    image12=models.ImageField(upload_to='statics/images',default='a')
    name12=models.CharField(max_length=200,default='text')
    back_name1=models.CharField(max_length=200,default='text')
    text12=models.CharField(max_length=200,default='text')
    text13=models.CharField(max_length=200,default='text')
    text14=models.CharField(max_length=200,default='text')
    text15=models.CharField(max_length=200,default='text')
    description1=models.TextField(default='')
    text16=models.CharField(max_length=200,default='text')
    descriptionn1=models.TextField(default='')
    text26=models.CharField(max_length=200,default='text')
    descriptionn2=models.TextField(default='')
    syllabus1=models.TextField(default='')


class courses2(models.Model):
    image121=models.ImageField(upload_to='statics/images',default='a')
    name121=models.CharField(max_length=200,default='text')
    back_name11=models.CharField(max_length=200,default='text')
    text121=models.CharField(max_length=200,default='text')
    text131=models.CharField(max_length=200,default='text')
    text141=models.CharField(max_length=200,default='text')
    text151=models.CharField(max_length=200,default='text')
    description=models.TextField(default='')
    text161=models.CharField(max_length=200,default='text')
    descriptionn11=models.TextField(default='')
    text61=models.CharField(max_length=200,default='text')
    descriptionn12=models.TextField(default='')
    syllabus2=models.TextField(default='')
class Teach_us(models.Model):
    img1=models.ImageField(upload_to='statics/images',default='a')
    heading=models.CharField(max_length=50)
    para=models.TextField(default='text')
class index_us(models.Model):
    img2=models.ImageField(upload_to='statics/images',default='a')
    heading1=models.CharField(max_length=50)
    para1=models.TextField(default='text')
class home_courses(models.Model):
    imageh=models.ImageField(upload_to='statics/images',default='a')
    nameh=models.CharField(max_length=200,default='text')
    back_nameh=models.CharField(max_length=200,default='text')
    texth=models.CharField(max_length=200,default='text')
    texth1=models.CharField(max_length=200,default='text')
    texth2=models.CharField(max_length=200,default='text')
    texth3=models.CharField(max_length=200,default='text')
    descriptionh=models.TextField(default='')
    texth4=models.CharField(max_length=200,default='text')
    descriptionh1=models.TextField(default='')
    texth5=models.CharField(max_length=200,default='text')
    descriptionh2=models.TextField(default='')
    syllabush=models.TextField(default='')