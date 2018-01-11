n=int(input())
h=int(input())
o=n%h
s=h
if o!=0:
    while s%o!=0:
        s=o
        o=h%o
if o!=0:
    print(h*n/o)
if o==0:
    print("your biger number is the answer")


        
    
