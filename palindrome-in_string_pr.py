# python-practice
#this program is O(n^2)
S=input()
def check_palindrom(string):
    '''This functions return true for palindrome string'''
    if(string==string[::-1]):
        return True
    else:
        return False
if __name__ == "__main__":
    upper=len(S)
    lower=0
    lst=[]
    while(upper!=lower):                    #Traversing through the string in all possible manner.
            while(upper!=lower):
                if(check_palindrom(S[lower:upper])):      
                    lst.append(S[lower:upper]) 
                upper=upper-1
            lower=lower+1
            upper=len(S)
    print(set(lst))               #To Avoid Duplication
