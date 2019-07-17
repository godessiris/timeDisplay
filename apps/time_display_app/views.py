from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime
    
def index(request):
    context = {
        "date": strftime("%a, %B %d, %Y", localtime()),
        "time":strftime(" %I:%M %p", localtime())
    }
    return render(request,'time_display_app/index.html', context)
