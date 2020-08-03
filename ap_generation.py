# write a program to generate an arthematic progression :

# program:

def ap(a,n):
    d=int(input("Enter d:"))
    l=[]
    for i in range(n):
        y=a+(i-1)*d
        print('The value of y now is:',y)
        l.append(y)
    return l
a=int(input('Enter intial value:'))
n=int(input('Enter the step:'))
j=ap(a,n)
for k in range(len(j)):
    print(j[k], end=" ")
print('/n')
print(*j)

# output:
'''Enter d:1                                                                                                                                                                
The value of y now is: 4                                                                                                                                                 
The value of y now is: 5                                                                                                                                                 
The value of y now is: 6                                                                                                                                                 
The value of y now is: 7                                                                                                                                                 
4 5 6 7 /n                                                                                                                                                               
4 5 6 7  '''                                                                                                                                                                
                        
