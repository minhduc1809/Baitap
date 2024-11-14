res=0
with open("DaySoINP2.txt","r+") as f:
   t=int(f.readline())
   s=f.readline().split()
   for i in s:
     if(int(i)%3==0):
       res+=int(i)
with open("DaySoOUT2.txt","w") as t:
   t.write(str(res))