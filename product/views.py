from django.shortcuts import render, render_to_response

from product.models import Product

# Create your views here.
def product(request):
	product = Product.objects.all()
	return render(request, 'product/products.html', {
		'product':product,
	})

def productFinal(request,slug):
	context = Product.objects.filter(slug__exact=slug).get()
	product = Product.objects.all()
	return render(request, 'product/product.html',{
	 	'product':product,
	 	'context':context,
	})