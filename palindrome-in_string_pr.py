# python-practice
S=input()
def check_palindrom(string):
    if(string==string[::-1]):
        return True
    else:
        return False
upper=len(S)
lower=0
lst=[]
while(upper!=lower):
        while(upper!=lower):
            if(check_palindrom(S[lower:upper])):
                lst.append(S[lower:upper])
            upper=upper-1
        lower=lower+1
        upper=len(S)
print(set(lst))
