from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


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
  
def updateTask(request):
    detail=Persondetail.objects.all()
    form=detailform()
    if request.method =="POST":
        form=detailform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/update_task')
    context= {'form':form ,'detail':detail}
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



 



