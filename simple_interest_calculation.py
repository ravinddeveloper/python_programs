
p=input("enter the amount : ")
t=input("enter time period : ")
r=input("enter rate of interest : ")

if p!="" and t!="" and r!="":
  print(" amount taken : ",p,"\n" ,"time period : ",t,"\n","rate of interest : ", r) 
else:
  print("some of the value you entered are empty it will take default values : ")
  p=1345
  t=5
  r=3
  print(" amount taken : ",p,"\n" ,"time period : ",t,"\n","rate of interest : ", r) 

si=int(p)*int(t)*int(r)/100

print("\n","the simple interest is : ",si)