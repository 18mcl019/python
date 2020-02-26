n=121
x=n
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if(x==rev):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
    
