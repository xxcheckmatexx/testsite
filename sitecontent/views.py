from django.shortcuts import render, render_to_response

from sitecontent.models import Content

# Create your views here.
def index(request,slug):
	context = Content.objects.get(id=5)
	return render(request, 'sitecontent/index.html', {
		'context':context,
	})