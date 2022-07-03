from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from resume.forms import resumeform
from resume.models import Resume
# Create your views here.
def home(request):
    candidate = Resume.objects.all()
    if request.method=='POST':
        fm = resumeform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = resumeform()
    return render(request,'resume/home.html',{'fm':fm,'candidate':candidate})


def profile(requests,id):
    candidate = Resume.objects.get(pk=id)
    return render(requests,'resume/profile.html',{'candidate':candidate})