from django.shortcuts import render
from .forms import DocumentForm
from .models import Document

# Create your views here.

def upload(request):
    data= Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'task.html',context={'form':form,'data':data})
    form = DocumentForm()
    return render(request,'task.html',context={'form':form,'data':data})


def delete(request,pk):
    d = Document.objects.get(pk=pk)
    d.delete()
    return d

def view(request,pk):
    v=Document.object.get(pk=pk)
    return v
def download(request,pk):
    dp=Document.objects.get(pk=pk)



