

def Balanced(num):
	st = str(num) # integer to string
	if len(st)%2!=0: #for only odd length string
		size = len(st)
		mid = int((size+1)/2)-1 #find mid index
		summ=0
		summ2=0
		for x in st[:mid]: # take string till mid & sum its element
			summ =summ+int(x)
		for j in st[mid+1:]: # take string fom mid to last and sum its element
			summ2 = summ2+int(j)
	
		if summ == summ2:
			print("Balanced Number")
		else:
			print("Not a Balanced Number")

	else:print("error")
		
Balanced(1234006)
Balanced(1234)
