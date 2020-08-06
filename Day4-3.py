import os.path

d={}

print("歡迎進入成績查詢系統")

def buildMenu():
    print("1.建立成績")
    print("2.列出所有成績")
    print("3.查詢成績")
    print("4.離開")
    
    sel=int(input("輸入選項:"))
    return sel
    
if os.path.isfile("scores.txt"):
    print("存在")
    fo=open("scores.txt","r")
    x=fo.read()
else:
    print("不存在")
    fo=open("scores.txt","w")
    fo.write(d)
    
while True:
    sel = buildMenu()
    if sel==1:
        n=input("輸入名字:")
        s=input("輸入成績:")
        d[n]=s
        fo=open("scores.txt","a")
        fo.write(n)
        fo.write(":")
        fo.write(s)
        fo.write("\n")
        fo.close()
        
    #elif sel==2:
        #print(d)
    #elif sel==3:
        
      



