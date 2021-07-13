class Solution:
    #Function to rearrange an array so that arr[i] becomes arr[arr[i]]
    #with O(1) extra space.
    def arrange(self,arr, n): 
        
        hashmap={}  # hashamap stores tuples of (a[i],a[a[i]]) at keys which are equal to indexes
        for i in range(n):
        	hashmap[i]=(arr[i],arr[arr[i]])
        for i in range(n):
        	arr[i]=hashmap[i][1]  #replacing values of a[i] with value to replaced with stored in the tuple 
        return(arr)
