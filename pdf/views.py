from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io


# Create your views here.
def Accepte(request):
    if request.method== "POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        summery=request.POST.get("summery","")
        degree=request.POST.get("degree","")
        school=request.POST.get("school","")
        university=request.POST.get("university","")
        previous_work=request.POST.get("previous_work","")
        skill=request.POST.get("skill","")
        image=request.POST.get("image")

        profile=Profile(name=name,email=email,phone=phone,summery=summery,degree=degree,school=school,university=university, pervious_work=previous_work,skill=skill)
        profile.save()

    
    return render(request,"pdf/accounts.html")
 
def Resume(request,id):
    userpro=Profile.objects.get(id=id)
    template=loader.get_template('pdf/resume.html')
    html=template.render({"userpro":userpro})
    options={
        'page-size':'letter',
        'encoding':'UTF-8',
    }
    pdf=pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type="application/pdf")
    response['content-Disposition'] ='attachment'
    filename="resume.pdf"
    return response

def List(request):
    profile=Profile.objects.all()
    return render(request,"pdf/list.html",{"profile":profile})