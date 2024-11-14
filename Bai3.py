res=""
with open("UOCINO.txt","r+") as f:
   t=int(f.readline())
   for i in range (1,t+1):
     if(t%i==0):
       res+=str(i)+" "
with open("UOCOUT.txt","w") as t:
   t.write(str(res))