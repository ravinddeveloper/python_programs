list={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}
pattern=['double','two','triple','one','zero','double','two','six','seven','nine','triple','zero'] # phone number with triple and double words

list1=[]
def getindex(pattern,l,r):
    index=pattern.index(l)
    for i in range (0,r):
      list1.append(pattern[index+1])
        
for l in pattern:
  if l=='triple' :
    r=2
    getindex(pattern,l,r)
  elif l=='double':
    r=1
    getindex(pattern,l,r)
  else:
    list1.append(l)


for i in list1:
  print(list[i],end='')
    
