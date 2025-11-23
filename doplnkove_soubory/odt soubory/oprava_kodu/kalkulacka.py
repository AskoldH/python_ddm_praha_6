x=0
y=0

def f(a,b,c):
 if c==1:
    return a+b
 if c==2:
        return a-b
 if c==3:
  return a*b
 if c==4:
     if b==0:
            print("nejde")
            return
     else:
                 return a/b

print("kalkulacka")
print("1 scitani")
print("2 odecitani")
print("3 nasobeni")
print("4 deleni")

u = input("co chces:")
if u=="1":
   x = input("prvni:")
   y = input("druhy:")
   print("vysledek je", f(int(x),int(y),1))
elif u=="2":
   x = input("a:")
   y = input("b:")
   print("= ", f(int(x),int(y),2))
elif u=="3":
  x=input("x:")
  y=input("y:")
  print(f(int(x),int(y),3))
elif u=="4":
 x=input("cislo1:")
 y=input("cislo2:")
 print(f(int(x),int(y),4))
else:
 print("nevim co chces")