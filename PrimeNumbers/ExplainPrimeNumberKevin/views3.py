from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

New = '<br/><br/>'
Part1 = 'This is where you will find my explanations to my two other web pages which you can visit using '
Part2 = 'http://127.0.0.1:8000/findPrimeNumber/?start=0&end=10&Mersin%20mode=1 and http://127.0.0.1:8000/checkPrimeNumber/?num=2&Mersin%20mode=0'+New
Part3 = 'A prime number is defined as a number with no prime factors. My program will go through all numbers up to sqrt(num) for any factors. '
Part4 = 'You only have to go up to sqrt(num) because if you had to go further to find one, that would not happen because if the number did '
Part5 = 'have a prime factor, it would have already showed up before.'+New
Part6 = 'You may have noticed that Mersin primes have the form 2^p-1. p must be prime for 2^p-1 to be prime with the following proof:'+New
Part7 = 'Suppose p was not prime. That would mean p=ab where a and b are integers. That would mean that 2^p-1=2^ab-1.'+New
Part8 = '2^ab-1 can be factored into (2^a-1)(2^(ab-a)+2^(ab-2a)+2^(ab-3a)+.....+1). '
Part9 = 'That means if p is not prime, 2^p-1 must also not be prime.'+New+New
Part10 = 'You might be wondering how I was able to determine Mersin Primes a lot faster than regular primes of the same size. '
Part11 = 'I use a special method first used by Lucas to determine that 2^127-1 was prime.'+New
Part12 = 'The method is that you first take the sequence f(1)=4 and f(x)=f(x-1)^2-2. '
Part13 = 'To determine if 2^p-1 is prime, take f(p). If 2^p-1 divides into f(p), 2^p-1 is prime.'+New
Part14 = 'Of course you have to be more clever than to just calculate f(p) because the numbers get quite large. '
Part15 = 'You only have to calculate f(p) mod 2^p-1 because you will divide it in the end.'+New
Part16 = 'For more details check out the video about primes made by Numberphile using the url https://www.youtube.com/watch?v=lEvXcTYqtKU.'

Writing = Part1+Part2+Part3+Part4+Part5+Part6+Part7+Part8+Part9+Part10+Part11+Part12+Part13+Part14+Part15+Part16

def primeKevin3(request):
    return HttpResponse(Writing)
