from django.shortcuts import render

def start_window(request):
    return render(request, 'main/start.html')
