from django.shortcuts import render, render_to_response

from sitecontent.models import Content

# Create your views here.
def index(request,slug):
	context = Content.objects.filter(slug__exact=slug).get()
	navigation = Content.objects.all()
	return render(request, 'sitecontent/index.html', {
		'context':context,
		'navigation':navigation,
	})