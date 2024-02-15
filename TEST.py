people = [
    {"name": "Alice", "age": 30, "dept":"Eng"},
    {"name": "Bob", "age": 25,"dept":"Eng"},
    {"name": "Charlie", "age": 35,"grade":{"eng":10}},
    {"name": "Diana", "age": 28}
]

def get_age(emp):
    return emp["age"]

y=sorted(people,key=get_age,reverse=True)

# print(y)


count=0

# ans=[emp for emp in people if emp["name"]=="Alice"]

print(people[2].items())