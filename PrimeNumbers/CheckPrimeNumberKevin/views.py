from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

Intro = 'This is Kevin\'s first web app for determining prime numbers. To use a new number, type a different number at the top.<br/>'

def primeKevin(request):
    c = 2
    b = 0
    a = int(request.GET.get('num'))
    if a<2:
        return HttpResponse(Intro+"Sorry, I can not tell if "+str(a)+" is prime or not.")
    while c<a**0.5:
        if a%c == 0:
            return HttpResponse(Intro+str(a)+" is composite.")
        c+=1
    return HttpResponse(Intro+str(a)+" is prime")

