ns = [1,4,2,7,1,9,0,3,4,6,6,6,8,3]
lc = [x for x in ns if x > 5]
print(lc)
items = ["12", "1", "5", "10", "15"]

items1 = [int(x)  for x in items if int(x) > 10]
print(items1)

items2 = [int(x) * 2  for x in items if int(x) > 10]
print(items2)

a = ["1", "2", "3"]
b = ["one", "two", "three"]
z = zip(a,b)
print(list(z))
