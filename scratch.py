def add_item(item,items=[]):
    items.append(item)
    return items
print(add_item("a"))
print(add_item("b"))   
print(add_item("c"))

a = [1, 2, 3]
b = a
b.append(4)
print(a)

s = "hello"
t = s
t += " world"
print(s)

a = [[1, 2], [3, 4]]
b = a[:]
b[0].append(99)
print(a)

l1 = [1, 2]
l2 = [1, 2]
print(l1 == l2, l1 is l2)

x = 256; y = 256
print(x is y)
x = 257; y = 257
print(x is y)

name = "Peter"

print(f"{name:>10}")