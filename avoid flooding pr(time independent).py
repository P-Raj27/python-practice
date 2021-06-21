# python-practice
rain_list=[int(x) for x in input().split()]
full_list=[]
out_list=[]
for i in range(len(rain_list)):
    flag=0
    
    #If element present in full_list then it will be flodded so return empty list and break
    
    if(rain_list[i] in full_list):
        out_list=[]
        break
        
    #full_list is updated with each elements
    
    else:
        if(rain_list[i]>0):
            full_list.append(rain_list[i])
            out_list.append(-1)
            print(full_list)
            
    #Now if 0 comes then we have to remove an element from full_list to avoid flooding
            
        if(rain_list[i]==0):
            
            #Wehave to remove that element only which comes first after the 0.
            #SO we have to choose the very first element after 0 in rain_list that is in full_list to remove.
                
            for j in range(i+1,len(rain_list)):
                    #if there is another 0 after 0 then we have to continue till we find a lake number
                    if(rain_list[j]==0):
                        continue
                        
                    #once the element is found we remove from full_list and also update out_list and break loop
                    
                    if(rain_list[j] in full_list):
                        full_list.remove(rain_list[j])
                        out_list.append(rain_list[j])
                        flag=1
                        break
                        
            #As specified in the question if there is nothing to remove then update list with 1
            #this occurs when full_list is empty and nothing to remove(ar any lake can be emptied
            
            if(flag==0):
                out_list.append(1)
                
                        
print(rain_list)
print(out_list)
                
