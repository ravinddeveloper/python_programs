name ={
    "ravi":7894567889,
    "shekar":7845698547,
    "kumar":4785967478,
    
}
def new_add(search):
  print("name is not in list add this")
  new_num=input("enter number to be add : ")
  name[search]=new_num
  
print("sorted order : ",sorted(name))
for i in name:
  print('{}:{}'.format(i,name[i]))


for i in name:
  search_name=input("enter name to be search : ")
  if i!=search_name :
    new_add(search_name)
    break
  else:
    break
  
print("sorted order : ",sorted(name))
for i in name:
  print('{}:{}'.format(i,name[i]))
