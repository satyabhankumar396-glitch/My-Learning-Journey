# Dictionary Basics
student={

    "name" : "Satybhan",
     "City": "Hamirpur ruru",
     "Age" : 16,
     "Roll number" : 23

}

print(type(student))
print(student["name"])
print(student)
print(student["City"])
student["City"]= "Delhi"
print(student)
student["FavSubject"]= "Maths"
print(student)

student.pop("FavSubject")
print(student)
print(student.items())