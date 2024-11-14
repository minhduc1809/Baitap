a=[]
with open("TBCINP2.txt","r+") as f:
   t=int(f.readline())
   for i in range (t):
      s=f.readline().split()
      res=0
      for i in s:
         res+=int(i)
      a.append(res/len(s))     
with open("TBCOUT2.txt","w") as t:
   for i in a:
       t.write(str(i)+"\n")