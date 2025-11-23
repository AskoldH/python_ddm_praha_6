import random

p="abcdefghijklmnopqrstuvwxyz"
P="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="0123456789"
z="!$%&*@?#"

h=""

x=input("delka: ")
if x=="":
  x="8"

i=0
while i<int(x):
   r=random.randint(0,4)
   if r==0:
      h=h+p[random.randint(0,len(p)-1)]
   if r==1:
      h=h+P[random.randint(0,len(P)-1)]
   if r==2:
      h=h+c[random.randint(0,len(c)-1)]
   if r==3:
      h=h+z[random.randint(0,len(z)-1)]
   if r==4:
      h=h+p[random.randint(0,len(p)-1)]
   i=i+1

print("tady mas:",h)
