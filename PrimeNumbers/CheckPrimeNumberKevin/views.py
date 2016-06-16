from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

name = 'C:/Users/Kevin/Documents/GitHub/MyFirstWebApp/PrimeNumbers/CheckPrimeNumberKevin/Extra data for Web.py'

def primeKevin(request):
    with open(name,'r') as f:
        views = int(f.read())
    with open(name,'w') as g:
        g.write(str(views+1))
    Intro1 = 'This is Kevin\'s first web app for determining prime numbers. To use a new number, type a different number at the top.<br/><br/>'
    Intro2 = 'You can turn Mersin Mode on and off by changing the url. Mersin mode calculates (2^num)-1 instead of num being prime or not.<br/><br/>'
    Intro3 = 'Message from the future: you can now search for prime numbers on my other web app http://127.0.0.1:8000/findPrimeNumber/?start=2&end=100&Mersin%20mode=0. '
    Intro3a = 'If you want explanations, visit my web app http://127.0.0.1:8000/explainPrimeNumber/.'
    Intro4 = 'The biggest prime number I found was 2^3217-1. That has 969 digits! Can you find a bigger one?<br/><br/>'
    Intro5 = 'This page has been seen '+str(views)+' times.<br/><br/>'
    Intro = Intro1+Intro2+Intro3+Intro3a+Intro4+Intro5
    a = int(request.GET.get('num'))
    mode = int(request.GET.get('Mersin mode'))
    if mode == 0:
        c = 2
        if a<2:
            return HttpResponse(Intro+"Sorry, I can not tell if "+str(a)+" is prime or not.")
        while c<=a**0.5:
            if a%c == 0:
                return HttpResponse(Intro+str(a)+" is composite.")
            c+=1
        return HttpResponse(Intro+str(a)+" is prime")
    else:
        num = 2**a-1
        if a<3:
            return HttpResponse(Intro+"Sorry, I can not tell if "+str(num)+" is prime or not.")
        count = 4
        i = 0
        while i<a-2:
            count = (count**2-2)%num
            i+=1
        if count == 0:
            return HttpResponse(Intro+str(num)+" is prime.")
        return HttpResponse(Intro+str(num)+" is composite.")
