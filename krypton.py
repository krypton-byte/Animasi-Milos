import os
while 0<=1:
	n=1
	while n<=153:
		no=str(n)
		a=open('text/ricardo_'+no+'.txt').read()
		os.system('clear')
		print(a)
		n+=1
