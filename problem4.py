a=list()
print("enter 10 numbers")
for i in range(0,10):
	a.append(input())
a.sort()
print(set(a))
#or i in range(0,len(a)):
#	ele=int(a[i])
#	for j in range(i+1,10-i-1):
#		if(int(a[j])==ele):
#			a.pop(j)
#			print(a)
#	print(i)
#print(a)
