from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
name = 'C:/Users/Kevin/Documents/GitHub/MyFirstWebApp/PrimeNumbers/CheckPrimeNumberKevin/Extra data for Web.py'

def primeInt(x):
    c = 2
    if x<2:
        return -1
    while c<x**0.5:
        if x%c == 0:
            return 0
        c+=1
    return 1

def primePower(x):
    num = 2**x-1
    if a<3:
        return -1
    count = 4
    i = 0
    while i<a-2:
        count = (count**2-1)%num
        i+=1
    if count == 0:
        return 1
    return 0

def values(func,start,end):
    sat = []
    i = start
    while i<=end:
        i+=1
        if func(i) == 1:
            sat.append(i)
    return sat

def primeKevin2(request):
    Intro1 = 'This is Kevin\'s web app for finding prime numbers. To select a new range, type different numbers at the top.<br/><br/>'
    Intro2 = 'You can turn Mersin Mode on and off by changing the url. Mersin mode calculates (2^num)-1 instead of num being prime or not.<br/><br/>'
    Intro3 = 'Check out my other web app using http://127.0.0.1:8000/checkPrimeNumber/?num=3&Mersin%20mode=0.<br/><br/>'
    Intro = Intro1+Intro2+Intro3
    start = int(request.GET.get('start'))
    end = int(request.GET.get('end'))
    mode = int(request.GET.get('Mersin mode'))
    if mode == 0:
        stuff = Intro
        for i in values(primeInt,start,end):
            stuff+=str(i)+'<br/>'
        return stuff
    if mode == 1:
        stuff = Intro
        for i in values(primePower,start,end):
            stuff+=str(i)+'<br/>'
        return stuff
