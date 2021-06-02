from django.shortcuts import render

def myindex(request):
	return render(request, 'index.html')
