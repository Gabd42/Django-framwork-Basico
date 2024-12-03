from django.shortcuts import render

# Create your views here.

def Index(request):
	context = {
		'curso':'programação python'
	}
	return render(request, 'index.html', context)