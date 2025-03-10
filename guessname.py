secret="apple"
name=""
count=0
count_num=3
while name!=secret and count<count_num:
      name=input("enter name:")
      count=count+1
if name==secret:
     print("you are win "+"at "+str(count)+" attempts")
else:    
    print("you are out "+"at "+str(count)+" attempts")
