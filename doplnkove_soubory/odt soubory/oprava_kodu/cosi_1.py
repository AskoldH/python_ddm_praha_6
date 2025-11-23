q=[3,1,4,1,5,9,2,6,5,3,5]

def g(h):
 for i in range(len(h)):
    for j in range(len(h)-1):
       if h[j] > h[j+1]:
        t=h[j]
        h[j]=h[j+1]
        h[j+1]=t
 return h

w = input("zadej cisla oddelene carkou: ")
if w!="":
 z=w.split(",")
 for i in range(len(z)):
  z[i]=int(z[i])
else:
 z=[]
 for a in q:
  z.append(a)

r=g(z)

s=0
for x in r:
 s=s+x

print("->", r)
print("==", s)
print("::", r[len(r)//2])
