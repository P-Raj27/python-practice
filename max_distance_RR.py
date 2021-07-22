from collections import defaultdict
class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr, n):
        
        store = defaultdict(list)
        
        for i in range(n):
            store[arr[i]].append(i)
            
        mx = 0
        for ele in list(store.values()):
            if (max(ele)-min(ele)) >= mx:
                mx = (max(ele)-min(ele)) 
        return((mx))
