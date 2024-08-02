import os

f=open("sayings.txt",encoding="utf-8")
result=[]
for i in f.readlines():
    if(i[0]=="#" or i.strip()=="" or i.strip()=="\n"):
        continue
    result.append(i)
f.close()

os.makedirs("out",exist_ok=True)
f=open("out/index.html","w",encoding="utf-8")
f.write("".join(result))
f.close()