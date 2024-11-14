res=""
with open("DaySoINP.txt","r+") as f:
   t=int(f.readline().strip())
   s=f.readline().split()
   for i in s:
     if(int(i)%2==0):
       res+=i+" "
with open("DaySoOUT.txt","w") as t:
   t.write(res)