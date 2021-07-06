# python-practice
#THIS APPROACH USES TWO POINTERS AT STARITNG AND ENDING
#IT ITERATES TILL BOTH reach 1 and 0 respectively and then swaps
lst=[int(x) for x in input().split()]
left=0
right=len(lst)-1
flag_l=0
flag_r=0
decision=True
while(decision==True):
    if(lst[left]==0):        #traverses till it finds 0 at positions and if found fun flag is raised
        left=left+1
    else:
        flag_l=1
    if(lst[right]==1):      ##traverses till it finds 1at positions and if found fun flag is raised
        right=right-1
    else:
        flag_r=1
    if(flag_r==1 and flag_l==1):       #if both flag is raised then swaping is done
        if(left<right):
            lst[left],lst[right]=lst[right],lst[left]
    if(left>right):                       #if left becomes greater than right that means work is done
        decision=False
print(lst)
        
