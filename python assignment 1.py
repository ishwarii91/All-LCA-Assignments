# LIST
a = [10, 20, 30, 40]

a.append(50)
a.insert(1, 15)
a.extend([60, 70])
a.remove(30)
a.pop()
a.sort()
a.reverse()

print(a)
print(a[0], a[-1], a[1:3])
print(len(a), 20 in a, a.count(20), a.index(20))

# TUPLE
b = (10, 20, 30, 20, 40)

print(b)
print(b[0], b[-1], b[1:4])
print(len(b), 20 in b, b.count(20), b.index(40))

c = b + (50, 60)

# DICTIONARY
d = {"name": "Rahul", "age": 20, "marks": 90}

print(d["name"])
print(d.get("age"))

d["age"] = 21
d["city"] = "Pune"
d.update({"marks": 95})

print(d.keys())
print(d.values())
print(d.items())

d.pop("city")
d.popitem()

print(len(d))
print("name" in d)

for key, value in d.items():
    print(key, value)
