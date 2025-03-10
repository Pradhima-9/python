def power(base,pow):
 result=1
 for i in range(pow):
    result=result*base
 return result
base=int(input("enter base:"))
pow=int(input("enter power:"))
print(power(base,pow))

