list1=[4,8,99,64,13,1]

def multiply(list1):
  temp=1
  length=len(list1)
  for i in list1:
    temp*=i
  return temp
  
print(multiply(list1))