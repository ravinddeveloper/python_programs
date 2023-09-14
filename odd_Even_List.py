import random
Odd=[]
Even=[]
for i in range(0,10):
   l=random.randint(1,50)
   if l%2==0:
    Even.append(l)
   else:
    Odd.append(l)
    
print("odd list is : ",Odd)
print("even list is : ",Even)