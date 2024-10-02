student = {
    "name" : "Marko",
    "age" : 20,
    "major" : "Software Engineering"
}

students = [  
    {
        "name" : "Marko",
        "age" : 20,
        "major" : "Software Engineering"
    },
    {
        "name" : "Marko",
        "age" : 20,
        "major" : "Software Engineering"
    }
]

marko = [(key, value) for key, value in student.items()]

for key, value in student.items():
    print(f"Key : {key}, Value : {value}")

for key in student.keys():
    print(f"Key : {key}")

for value in student.values():
    print(f"Value : {value}")


print(type(students[0]))

student = {
    "name" : "Marko",
    "age" : 20,
    "major" : "Software Engineering"
}

students = [
    {
        "name" : "Marko",
        "age" : 20,
        "major" : "Software Engineering"
    },
    {
        "name" : "Marko",
        "age" : 20,
        "major" : "Software Engineering"
    }
]


marko = [(key, value) for key, value in student.items()]

for key, value in student.items():
    print(f"Key : {key}, Value : {value}")

for key in student.keys():
    print(f"Key : {key}")

for value in student.values():
    print(f"Value : {value}")


print(type(students))



person = {
    "first_name" : "Nikolcho",
    "last_name" : "Spasovski"
}


print(person)



#Nested Dictonary

nested_dictonary = {
    "nested_item1" : {
        "name" : "Random",
        "age" : "Random"
    },
    "nested_item2" : {
        "name" : "Random2",
        "age" : "Random2"
    }
}

print(type(nested_dictonary))
