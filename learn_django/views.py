from django.http import HttpResponse
def index(request):
    return HttpResponse('Helo')

def about(request):
    return HttpResponse('<h1>About Page</h1>')