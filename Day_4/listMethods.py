# Methods in list
# indexing


# Lists are mutable
marks= [ 99, 100, 90, 95]
print(marks[3])


marks[1]= 94
print(marks)

# Slicing

print(marks[1:3])
print(max(marks))
print(min(marks))


marks.append(92)
print(marks)
marks.sort()
print(marks)

marks.pop(1)
print(marks)

marks.remove(94)
print(marks)

marks.insert(1,94)
print(marks)


# # String are Immutable
# name= "Satybhan"
# name[1]= "A"
# print(name)
