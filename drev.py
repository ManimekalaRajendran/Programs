# Programs
n=int(input())
Reverse = 0
while(n > 0):
	r = n%10
	Reverse = (Reverse *10) + r
	n = int(n /10)
print(Reverse)
