
while True:
    c = 2
    b = 0
    a = str( input("Enter a positive integer other than one. I recommend only up to one trillion: (q to stop.):"))
    if(a=='q'):
        break
    a = int(a)
    if(a<2):
        print("Sorry, I can not tell if this number is prime or not.")
        break
    else:
        while(c<a**0.5):
            if(a%c):
                b=b+0
            else:
                b=1
            c=c+1
        if(b==0):
            print("prime")
        else:
            print("composite")
