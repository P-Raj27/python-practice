# python-practice
lst=[str(x) for x in input().split()]
lst2=[]                              #to store groups of anagrams
lst3=[]                                 #store the list of lst2
lst4=[]
for i in range(len(lst)):            
    if (lst[i] in lst4):                        #to avoid duplication
        continue
    lst2=[]
    lst2.append(lst[i])
    
    for j in range(i+1,len(lst)):                     #sorting and then finding anagrams
        if sorted(lst[j])==sorted(lst[i]):
            lst2.append(lst[j])
            lst4.append(lst[j])
            lst4.append(lst[i])
    if(len(lst2)>1):                                         #to avoid single words to be printed
        lst3.append(lst2)
print(lst3)
