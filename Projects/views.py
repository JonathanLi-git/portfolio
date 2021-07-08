from django.shortcuts import render

# Create your views here.
def Projects(request):
    return render(request, 'Projects/Projects.html');