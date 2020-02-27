a=list()
print(" enter 10 numbers")
for i in range(0,10):
	a.append(input())
for i in range(0,10):
	if(int(a[i])<5):
		print(a[i])