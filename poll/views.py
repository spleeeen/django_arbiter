from django.http import HttpResponse

def index(request):
	return HttpResponse("You done did it")