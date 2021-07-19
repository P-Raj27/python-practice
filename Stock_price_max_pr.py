# python-practice
#In a given array we have to find maximum difference in which the bigger value is on right of the minumum value.
lst=[int(x) for x in input().split()]
min_ele=lst[0]
max_diff=lst[1]-lst[0]
print(max_diff)
for i in range(len(lst)):
    if(lst[i]-min_ele>max_diff):            #every line we are update maxdiff and alos minimum value.
        max_diff=lst[i]-min_ele
    if(lst[i]<min_ele):
        min_ele=lst[i]
print(max_diff)
