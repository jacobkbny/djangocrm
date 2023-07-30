from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .EmailScripts.India.india_reach_out import reach_out_mail as india
from .EmailScripts.India.gap import gap_mail 
from .EmailScripts.India.first_appreciation import first_appreciation_mail as appreciation_mail
from .EmailScripts.korea.korea_reach_out import korean_email

@csrf_exempt
def reach_out(request):
    if request.method == "POST":
        # india(email,name)
        email_address_array = request.POST.getlist("email")
        name_array = request.POST.getlist("name")
        if len(email_address_array) == 1:
            india(email_address_array[0], name_array[0])
        else:
            for i in range(1, len(email_address_array)):
                india(email_address_array[i], name_array[i])
        return render(request,"email_sender/index.html",{"target":"reach"})
    else:
        return render(request,"email_sender/index.html",{"target":"reach"})
    
@csrf_exempt
def gap(request):
    if request.method == "POST":
        email_address_array = request.POST.getlist("email")
        name_array = request.POST.getlist("name")
        if len(email_address_array) == 1:
            gap_mail(email_address_array[0], name_array[0])
        else:
            for i in range(1, len(email_address_array)):
                gap_mail(email_address_array[i], name_array[i])
        return render(request,"email_sender/index.html",{"target":"gap"})
    else:
        return render(request,"email_sender/index.html",{"target":"gap"})
        
@csrf_exempt   
def korea(request):
    if request.method == "POST":
        email_address_array = request.POST.getlist("email")
        name_array = request.POST.getlist("name")
        if len(email_address_array) == 1:
            korean_email(email_address_array[0], name_array[0])
        else:
            for i in range(1, len(email_address_array)):
                korean_email(email_address_array[i], name_array[i])
        return render(request,"email_sender/index.html",{"target":"korea"})
    else:
        return render(request,"email_sender/index.html",{"target":"korea"})
    
@csrf_exempt
def appreciation(request):
    if request.method == "POST":
        email_address_array = request.POST.getlist("email")
        name_array = request.POST.getlist("name")
        if len(email_address_array) == 1:
            appreciation_mail(email_address_array[0], name_array[0])
        else:
            for i in range(1, len(email_address_array)):
                appreciation_mail(email_address_array[i], name_array[i])
        return render(request,"email_sender/index.html",{"target":"appreciation"})
    else:
        return render(request,"email_sender/index.html",{"target":"appreciation"})
    
def home(request):
    return render(request,'email_sender/home.html')