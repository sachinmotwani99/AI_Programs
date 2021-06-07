n = int(input("Enter total number of fish"))
a = int(input("Enter the actual percentage of red fish"))
b = int(input("Enter the desired percentage of red fish"))
ac = (a/100) * n;
bc = (b/100) * n;
d = ac - bc
x = (100*d)/(100-b)
print(x)
