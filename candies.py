n=int(input("enter the total capacity:"))
k=int(input("Enter the min to keep in jar:"))
t=n
tc=0
i=1
while i==1:
  c=int(input("Enter the no of candies want:"))
  if c>n:
    print("invalid input")
  else:
    n=n-c
    tc=tc+c
    print("candies sold:",c)
    if n<k:
      n=t
    print("No of candies available:",n)
    i=int(input("DO you want to continue(1or0):"))

print("Total no of candies sold:",tc)
