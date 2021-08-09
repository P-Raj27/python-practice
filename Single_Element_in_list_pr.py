# python-practice
#This programme finds the single element in a list which have all the element in a frequency of three.
#This code uses simple calculating the frequency of each element using dictionary.
#This can be also done using Counter function in collection module.
lst=[int(x) for x in input().split()]
dicti={}
for i in lst:
  if(i not in dicti):
    dicti[i]=1
  else:
    dicti[i]=dicti[i]+1
for i in dicti:
  if(dicti[i]==1):
    print (i)
