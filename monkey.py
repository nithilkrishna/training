n=int(input( "Total no of Monkeys"))
k=int(input( "Number of eatable Bananas by Single Monkey"))
j=int(input( "Number of eatable Peanuts by single Monkey"))
m=int(input("Total number of Bananas"))
p=int(input("Total number of Peanuts"))
a=(m+k-1)//k
b=(p+j-1)//j
eaten=a+b
if eaten > n:
   eaten = n
print("Number of monkeys left on the tree :",n - eaten)
