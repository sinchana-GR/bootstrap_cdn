from django.shortcuts import render

# Create your views here.
def animate(request):
    return render(request,'animate.html')