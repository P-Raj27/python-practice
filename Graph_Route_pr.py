# python-practice
#Lets Try with Recusrion
maps=dict()
maps["cab"]=["car","cat"]
maps["car"]=["bar","cat"]
maps["bar"]=["bat"]
maps["cat"]=["mat","bat"]
maps["mat"]=["bat"]
maps["bat"]=[]
Start=input("Enter the Starting point")
End=input("Enter the End Point")
lst=[]
def finder(string,count):
    if(maps[string]==[]):
        return None
    if(End in maps[string]):
        print(string)
        return count
    else:
        count=count+1
        print(maps[string])
        for i in maps[string]:
            print("We are at",i,count)
            lst.append(finder(i,count))
            #lst.append(i)
finder(Start,0)
print((lst))
        
       
