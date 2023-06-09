from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Form


# Create your views here.

# def index(request):
#     return render(request,'index.html')

def index(request):
    item1= Form.objects.all()
    if request.method =='POST':
        slno=request.POST.get('sl','')
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        item=Form(slno=slno,name=name,desc=desc)
        item.save();
    return render (request,'index.html',{'item':item1})

def delete(request,id):
    item = Form.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'delete.html')

# def update(request, id):
#     item= Item.objects.get(id=id)
#     if request.method == 'POST':
#         item.delete()
#         return redirect('/')
#     return render(request, 'update.html')

def update(request,id):
    item=get_object_or_404(Form,id=id)
    if request.method == 'POST':
        item.num = request.POST.get('num')
        item.name = request.POST.get('name')
        item.desc = request.POST.get('desc')
        item.save()
        return redirect('/')
    return render(request,'update.html',{'task':item})


