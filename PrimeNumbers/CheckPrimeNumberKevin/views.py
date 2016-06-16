from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

name = 'C:/Users/Kevin/Documents/GitHub/MyFirstWebApp/PrimeNumbers/CheckPrimeNumberKevin/Extra data for Web.py'

def resultPage(num,ans):
    return '<html><body style="font-family:verdana;"><h1>This is Kevin\'s Homepage.</h1><p>This website is dedicated to math.</p><img src="https://i.ytimg.com/vi/GjDNCfOmmPk/maxresdefault.jpg" height="360"width="640"></img><h2>Project: Prime Numbers</h2><p>This is Kevin\'s first web app for determining prime numbers.To use a new number, type a different number at the top.</p><p>You can turn Mersin Mode on and off by changing the url. Mersin mode calculates (2^num)-1 instead of num being prime or not.</p><p>Message from the future: you can now search for prime numbers onmy other web app http://127.0.0.1:8000/findPrimeNumber/?start=2&end=100&Mersin%20mode=0. If you want explanations, visit my web app http://127.0.0.1:8000/explainPrimeNumber/.The biggest prime number I found was 2^3217-1. That has 969 digits! Can you find a bigger one?</p><p>This page has been seen <i>99</i> times.</p><p style="color:#FF0000;"><b>'+num+' is '+ans+'.</b></p><p>Link to my homepage: <a href="/PrimeNumber/">Homepage</a></p></body</html>'

def primeInput(request):
    return HttpResponse('<html><body style="font-family:verdana;"><h1>This is Kevin\'s Homepage.</h1><p>This website is dedicated to math.</p><img src="https://i.ytimg.com/vi/GjDNCfOmmPk/maxresdefault.jpg" height="360"width="640"></img><h2>Project: Prime Numbers</h2><p>This is Kevin\'s first web app for determining prime numbers.To use a new number, type a different number at the top.</p><p>You can turn Mersin Mode on and off by changing the url. Mersin mode calculates (2^num)-1 instead of num being prime or not.</p><p>Message from the future: you can now search for prime numbers onmy other web app http://127.0.0.1:8000/findPrimeNumber/?start=2&end=100&Mersin%20mode=0. If you want explanations, visit my web app http://127.0.0.1:8000/explainPrimeNumber/.The biggest prime number I found was 2^3217-1. That has 969 digits! Can you find a bigger one?</p><form action="/checkPrimeNumber/">Number:<input type="text" name="num"></input><p>Mersin Mode?(0 or 1)<input type="text" name="Mersin mode"></input></p><p><input type="submit" value="Check Prime Number"></input></p></form></body</html>')

def primeKevin(request):
    with open(name,'r') as f:
        views = int(f.read())
    with open(name,'w') as g:
        g.write(str(views+1))
    a = int(request.GET.get('num'))
    mode = int(request.GET.get('Mersin mode'))
    if mode == 0:
        c = 2
        if a<2:
            return HttpResponse(Intro+"Sorry, I can not tell if "+str(a)+" is prime or not.")
        while c<=a**0.5:
            if a%c == 0:
                return HttpResponse(resultPage(str(a),'composite'))
            c+=1
        return HttpResponse(resultPage(str(a),'prime'))
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
            return HttpResponse(resultPage(str(num),"prime"))
        return HttpResponse(resultPage(str(num),"composite"))
