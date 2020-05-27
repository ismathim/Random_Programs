
#This function helps in getting the even list from the whole lot
def even_list(my_list):
    current_val=0
    even_only=[]
    for i in range (0,len(my_list)):
        if my_list[i]%2==0:
            current_val=my_list[i]
            even_only.append(current_val)
        else:
            continue
    print(current_val)
    return(even_only)
    
#This function helps in getting the highest even number  
def highest_list(even_only):
    a=sorted(even_only)
    length=len(a)
    return(a[length-1])
    
#Main
list_1=[10,8,7,3,2]
a=even_list(list_1)
print(highest_list(a))
