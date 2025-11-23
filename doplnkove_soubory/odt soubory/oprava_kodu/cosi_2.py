import random

a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
A=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n=["0","1","2","3","4","5","6","7","8","9"]
s=["!","?","%","$","@","*","-"]

def f(k):
 z=""
 i=0
 while i<k:
  x=random.randint(0,3)
  if x==0:
   z=z+random.choice(a)
  if x==1:
     z=z+random.choice(A)
  if x==2:
     z=z+random.choice(n)
  if x==3:
   z=z+random.choice(s)
  i=i+1
 return z

j=input("kolik? ")
if j=="":
 print(f(8))
else:
 print(f(int(j)))
