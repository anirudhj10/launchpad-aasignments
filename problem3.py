a=list()
b=list()
print("enter 5 numbers")
for i in range(0,5):
	a.append(input())
print("enter the key element")
ele=input()
for i in range(0,5):
	if(int(a[i])==int(ele)):
		b.append(i)
print(b)
