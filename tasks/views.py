from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


def search(request):
    results =None
    query= request.GET['query']
    # person=Persondetail.objects.all()
    person=Persondetail.objects.filter(Name__icontains=query)
    
    # if request.method=='GET': 
    #     form=searchform(request.GET)
    #     if form.is_valid():
    #         query = form.cleaned_data.get('query')

    #         results=searchform.object.filter(title__icontains=query)
    
    context={'person':person}
    return render(request,'accounts/search_results.html',context )
        # else:
        #      form=searchform()
        

            
     
def index(request):
    # tasks=Task.objects.all()

    # form=TaskForm()

    # if request.method =='POST':
    #     form= TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/')

    # context={'tasks':tasks , 'form':form}
    return render(request,'accounts/list.html')
  
def error(request):
    detail=Persondetail.objects.all()

    return render(request,'accounts/error.html',{'detail':detail})

    
def updateTask(request):
    
    form=detailform()
    # form1=emailform()
    # form2=phoneform()

    if request.method =="POST":
        print (request.POST)
        
        name=request.POST.get("name")
        address=request.POST.get("address")
        email=request.POST.get("email")
        number=request.POST.get("phone")
        emailtype=request.POST.get("emailtype")
        phonetype=request.POST.get("phonetype")
        print("Name:", name)
        print("Address:", address)
        print("Email:", email)
        print("Phone Number:", number)
        print("Email Type:", emailtype)
        print("Phone Type:", phonetype)

        # emailtype=request.POST.get()
        # form1=PhoneNO.objects.get_or_create(PhoneNO=number)
        form2,created=PhoneNO.objects.get_or_create(Number=number,Phonetype=phonetype)
        form1,created1=Email.objects.get_or_create(email=email,emailtype=emailtype)
        form=Persondetail(Name=name,Address=address,email=form1, phoneno=form2)
        form.save()
        # form1.save()
        # form2.save()
        # form=detailform(request.POST) 
        print('data:',form)

        # form1=emailform(request.POST)
        # form2=phoneform(request.POST)
        # if form.is_valid():
        # and form1.is_valid and form2.is_valid :
            # form.save()
            # form1.save()
            # form2.save()
        #     return redirect('/update_task')
        # else:
            # return HttpResponse('error.html')
        
    # 'form1':form1,'form2':form2
     
    # context= {'form':form  }
    return render(request,'accounts/update_task.html')
   #     task= Email.objects.get(id=pk)

#     form = TaskForm(instance=task)
#     if request.method == 'POST':
#             form = TaskForm(request.POST , instance=task)
#             if form.is_valid():
#                  form.save()
#                  return redirect('/')
#     context= {'form':form}
#     return render(request,'tasks/update_task.html',context)

# def deleteTask(request, pk):
#      item=PhoneNO.objects.get(id=pk)
#      if request.method =='POST':
#           item.delete()
#           return redirect('/')
#      context={'item':item}
#      return render(request,'tasks/delete_task.html',context)



 



