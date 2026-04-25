marks={
    "Harry": 98,
    "Rohan": 90,
    "Hammad": 86,
    "Shubham": 79,
    "Pritam": [92,95,89,100],
    0: "This is a key with integer value"
}

print(marks["Harry"])
print(marks.get("Hammad"))

print(marks.items())
print(marks.values())
print(marks.keys())

print(marks.get("Pritam"))

marks.update({"alok":69})
print(marks)

print(marks.popitem())
print(marks)

# print(marks.clear())

dict={"name":"harry","marks":98,"class":12}

d=dict.copy()
print(d)

