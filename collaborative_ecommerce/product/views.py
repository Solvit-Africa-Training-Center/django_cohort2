from django.shortcuts import render, redirect, get_object_or_404
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/list.html', {'categories': categories})
def category_create(request):
    if request.method=='POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category_list')
    return render(request, 'category/create.html')  

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.is_active = request.POST.get('is_active') == 'on'
        category.save()
        return redirect('category_list')
    return render(request, 'category/update.html', {'category': category})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list') 
    