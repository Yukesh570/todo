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
    return render(request,'accounts/error.html')

    
def updateTask(request):
    
    form=detailform()
    form1=emailform()
    form2=phoneform()

    if request.method =="POST":
        form=detailform(request.POST)
        form1=emailform(request.POST)
        form2=phoneform(request.POST)
        if form.is_valid() and form1.is_valid and form2.is_valid :
            form.save()
            form1.save()
            form2.save()
            return redirect('/update_task')
        else:
            return HttpResponse('error.html')
        asdfsadfsad
    
     
    context= {'form':form,'form1':form1,'form2':form2  }
    return render(request,'accounts/update_task.html',context)
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



 



