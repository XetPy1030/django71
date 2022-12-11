from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Product, Company

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def create_companies():
    if not Company.objects.all().count():
        Company.objects.create(name='Google')
        Company.objects.create(name='Asus')
        Company.objects.create(name='MSI')


def create(request):
    create_companies()
    
    if request.method == 'POST':
        product = Product()
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.company_id = request.POST['company']
        product.save()
        return HttpResponseRedirect('/')

    companies = Company.objects.all()
    return render(request, 'create.html', {'companies': companies})


def edit(request, id):
    try:
        product = Product.objects.get(id=id)
        
        if request.method == 'POST':
            product.name = request.POST['name']
            product.price = request.POST['price']
            product.company_id = request.POST['company']
            product.save()
            return HttpResponseRedirect('/')
        else:
            companies = Company.objects.all()
            return render(request, 'edit.html', {'product': product, 'companies': companies})
    except Product.DoesNotExist:
        return HttpResponseNotFound('Product not found')


def delete(req, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect('/')
    except Product.DoesNotExist:
        return HttpResponseNotFound('Product not found')