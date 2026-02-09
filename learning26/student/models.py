from django.db import models

# Create your models here.
class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    #meta class
    class Meta:
        db_table = "student" #table name
    def __str__(self):
        return self.studentName    

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "product"
class car(models.Model):
    carName=models.CharField(max_length=50)
    companyName=models.CharField(max_length=50)
    carColour=models.CharField(max_length=20)

    class Meta:
        db_table = "car"

#1-1 one std=one stdProfile
class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    #studentPrilfe id --> pk create auto...
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofile"
    def _str_(self):
        return self.studentId.studentName    

# for 1 to Many:-
#category --> #service

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"

    def _str_(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def _str_(self):
        return self.serviceName    
    

class intern(models.Model):
    internName=models.CharField(max_length=100)
    internAge=models.IntegerField()
    Department=models.CharField(max_length=100)

    class Meta:
        db_table = 'intern'
    
    def _str_(self):
        return self.internName
    
class internDetails(models.Model):
    internID=models.OneToOneField(intern,on_delete=models.CASCADE)
    internPhone = models.CharField(max_length=10)
    internGender = models.CharField(max_length=10)

    class Meta:
        db_table = 'internDetails'

    def _str_(self):
        return self.internID.internName
    
class teacher(models.Model):
    teacherName=models.CharField(max_length=100)
    phoneNo=models.IntegerField(max_length=10)
    Email=models.EmailField()
    
    class Meta:
        db_table = 'teacher'
    
    def _str_(self):
        return self.teacherName
    
class subject(models.Model):
    subject=(("BEE","BEE"),("BME","BME"),("M-2","M-2"))
    subName=models.CharField(max_length=100,choices=subject)
    subID=models.IntegerField(max_length=25)
    teacher = models.ForeignKey(teacher,on_delete=models.CASCADE)

    class Meta:
        db_table = 'subject'

    def _str_(self):
        return self.teacher.teacherName