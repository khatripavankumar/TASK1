from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import DocumentForm
from .models import Document


def upload(request):
    data = Document.objects.all()

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('upload')

    form = DocumentForm()
    return render(request, 'task.html', {'form': form, 'data': data})


def delete(request, pk):
    d = Document.objects.get(pk=pk)
    d.delete()
    return redirect('upload')


def view(request, pk):
    doc = Document.objects.get(pk=pk)
    return FileResponse(doc.File.open('rb'))


def download(request, pk):
    doc = Document.objects.get(pk=pk)

    response = FileResponse(doc.File.open('rb'))
    response['Content-Disposition'] = f'attachment; filename="{doc.File.name}"'

    return response