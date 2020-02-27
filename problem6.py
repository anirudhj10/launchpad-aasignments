a=dict()
k=list()
v=list()
i=1
print("enter the name and usn and press 0 to exit the loop")
l=0
while(i==1):
	k.append(input("enter name:"))
	v.append(input("enter usn"))
	a[k[l]]=v[l]
	i=int(input("do you want to continue"))
	if(i==0):
		break;
	else:
		l=l+1
print(a)
