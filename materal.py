def mat(x, y, z, cum):
    sumofproportion = (x+y+z)
    cement = (1.54/sumofproportion)*(1440/50)*cum
    sand = (1.54/sumofproportion)*y*(35.28)*cum
    aggrigate = (1.54/sumofproportion)*z*(35.28)*cum
    a = ('%.2f'%cement)
    b = ('%.2f'%sand)
    c = ('%.2f'%aggrigate)
    print("Cement Qty = {} Bags \nSand Qty   = {} Cft \naggrigate qty = {} Cft".format(a, b, c))
x = int(input("Enter proportion of cement: "))
y = int(input("Enter proportion of sand: "))
z = int(input("Enter proportion of aggrigate: "))
cum = int(input("Enter Quantity of concrete: "))
print(mat(x, y, z, cum))