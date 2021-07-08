# python-practice
#This question is to rearrange the elements in the array such that arr[i]=arr[arr[i]]
#I took help from geek for geeks solution

#The Aprraoch is to make the each element value such that n/len gives the new ouput and n%len gives the old output
#E.G two number 0,1
#0+0*len when divided by len will give the new value 0  NOTE:Value of the original elements are less than len.
arr=[int(x) for x in input().split()]
for i in range(len(arr)):
            arr[i]=arr[i]+(arr[arr[i]]%n)*n
        for i in range(len(arr)):
            arr[i]=arr[i]//n
print(arr)
