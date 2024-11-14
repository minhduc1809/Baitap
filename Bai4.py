res=0
with open("TBCINP.txt","r+") as f:
   t=int(f.readline())
   for i in range (t):
     res+=int(f.readline().strip())
   res=res/t  
with open("TBCOUT.txt","w") as t:
   t.write(str(res))