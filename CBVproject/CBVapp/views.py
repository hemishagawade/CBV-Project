from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from CBVapp.models import Student

# Create your views here.
class StudentList(View):
    def get(self,request):
        # fetch data from database and display on dashboard
        data = Student.objects.all()
        context = {'students':data}
        return render(request,'viewstu.html',context)

class AddStudent(View):
    def get(self,request):
        return render(request,'addstu.html')
   
    def post(self,request):        
        # 1) fetch FORM data 
        n = request.POST['name'] 
        b = request.POST['branch'] 
        p = request.POST['perc'] 
        # 2) inserting data into database
        s = Student.objects.create(name=n,branch=b,perc=p)
        s.save()
        # 3) return to dashboard
        return redirect('/viewstu')

class UpdateStudent(View):
    def get(self,request,sid):
        s = Student.objects.filter(id=sid)
        context = {'stu':s[0]}
        return render(request,'updatestu.html',context)
    
    def post(self,request,sid):
        # 1) fetch FORM data 
        n = request.POST['name'] 
        b = request.POST['branch'] 
        p = request.POST['perc'] 
        # 2) updating data 
        s = Student.objects.filter(id=sid)
        s.update(name=n,branch=b,perc=p)
        return redirect('/viewstu')
    
class DeleteStudent(View):
        def get(self,request,sid):
            s = Student.objects.filter(id=sid)
            s.delete()
            return redirect('/viewstu')
