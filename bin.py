N = int(input("enter the number"))
d = bin(N)[2:]
z = d.replace('1', 'y').replace('0', '1').replace('y', '0')
print("Result:",int(z, 2))
