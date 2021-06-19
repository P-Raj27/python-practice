# python-practice
def strictincrease(*lst):
    '''Returns True if list is strictly increasing'''
    f=1
    for i in range(len(lst)-1):
        if(lst[i]>=lst[i+1]):
            f=0
            break
    if(f==1):
        return True
    else:
        return False
def strictdecrease(*lst):
    ''' Returns True if list is strictly decreasing'''
    f=1
    for i in range(len(lst)-1):
        if(lst[i]<=lst[i+1]):
            f=0
            break
    if(f==1):
        return True
    else:
        return False
if __name__ == "__main__":
    main_lst=[int(x) for x in input().split()]
    temp=list(main_lst)                              # making a copy of main_ist 
    
    max_index=main_lst.index(max(main_lst))
    temp.pop(max_index)                                 
    if(max_index>0 and max_index<len(main_lst)-1 and (main_lst[max_index] not in temp)):
        increase=strictincrease(*main_lst[0:max_index])
        decrease=strictdecrease(*main_lst[max_index+1:len(main_lst)])
        if(increase==True and decrease==True):
            print("Mountain List")
        else:
            print("not Mountain List")
    else:
        print("not Mountain list")


        
