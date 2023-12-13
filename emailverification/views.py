from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
def verification(request):
    
    if request.method=='GET':
        return render(request,'verification.html')
    if request.method=='POST':
        otp=random.randint(1000,9999)
        email=request.POST.get('email')
        subject='Email Verification from Evernote-replica'
        from_email='xyz@gmail.com' 
        to=email
        html_content=render_to_string('email_template.html',{'otp':otp})
        text_conetent=strip_tags(html_content)
        msg=EmailMultiAlternatives(subject,text_conetent,from_email,[to])
        
        msg.send()
        request.session['email']=email
        request.session['otp']=otp
        return render(request,'otp_verify.html')



def otp_verification(request):
    if request.method=='GET':
        return render(request,'otp_verify.html')
        
    if request.method=='POST':
        otp=request.POST.get('otp')
        if(int(otp)==request.session.get('otp')):
            sucess="EmailVerification succesfull"
            return render(request,'signup.html',{'sucess':sucess})
        else:
            error="enter correct OTP"
            return render(request,'otp_verify.html',{'error':error})
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



