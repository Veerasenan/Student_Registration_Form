from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StudentDatas

def home(request): 
    mydata=StudentDatas.objects.all()  # inline comment
    if(mydata!=''):
        return render(request,'home.html',{'StudentDatas':mydata})   
    else:  
        return render(request,'home.html')

def AddData(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']
        
        obj=StudentDatas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Mail=mail
        obj.save()
        mydata=StudentDatas.objects.all()
        return redirect('home')
    return render(request,'home.html')

def UpdateData(request,id):
    mydata=StudentDatas.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']
        
        mydata.Name=name
        mydata.Age=age
        mydata.Address=address
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.save()
        return redirect('home')
    return render(request,'update.html',{'data':mydata})

def DeleteData(request,id): 
    # need to change : variable name 
    mydata = StudentDatas.objects.get(id=id)
    mydata.delete()
    return redirect('home')

