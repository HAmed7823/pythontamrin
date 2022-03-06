i=int(input('please enter number i:'))
j=int(input('please enter number j:'))
k=int(input('please enter number k:'))
if i<j :
    if i<k :
       i=j
    else :
        j=k
else : 
   if j>k: 
     j=i
   else :
    i=k
print("i =",i, "j =",j ,"k =",k)
#i is 3.j is 5 and k is7 => i=5 , j=5 , k=7

