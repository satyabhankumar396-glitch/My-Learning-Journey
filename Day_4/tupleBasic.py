# tuples Basics

myTuple= (78, 90, 75)
studentTuple= ("Satybhan", "Anurag", "Anshu", "Ritik", "Satybhan")


# studentTuple[1]="Alok"  #Tuples are Immutable/not changeable

print(studentTuple[2])


# empty Tupbles

emptyTuple=()
singleTuple=(1,)
print(type(emptyTuple))
print(type(studentTuple))
print(studentTuple.index("Satybhan"))
print(studentTuple.count("Satybhan"))
