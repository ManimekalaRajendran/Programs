# Programs
h1=int(input("Enter the hour in time 1:\n"))
m1=int(input("Enter the minits in time 1:\n"))
s=h1*60
t1=s+m1
h2=int(input("Enter the hour in time 2:\n"))
m2=int(input("Enter the minits in time 2:\n"))
g=h2*60
t2=g+m2
t=abs(t1-t2)
print("Diff between times is:",t)
       
