from django.shortcuts import render

# Create your views here.
from .models import Feedbacform
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime
date1=datetime.datetime.now()
def feedbackview(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')

            data=Feedbacform(name=name,
                              rating=rating,
                              feedback=feedback,
                              date=date1
                              )
            data.save()

            fdata=Feedbacform.objects.all()
            fform=FeedbackForm()
            return render(request,'feedback.html',{'fform':fform,'fdata':fdata})
        else:
            return HttpResponse('invalied form')
    else:
        fdata=Feedbacform.objects.all()
        fform=FeedbackForm()
        return render(request,'feedback.html',{'fform':fform,'fdata':fdata})
