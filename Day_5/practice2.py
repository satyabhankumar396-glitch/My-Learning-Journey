# you are given a list of programming languages:
# ["Python", "Java", "C++", "Python", "Java", "C"]
# Convert it into a set  and print how many unique languages Satybhan knows.

programminglist= ["Python", "Java", "C++", "Python", "Java", "C"]
print(type(programminglist))
# how to convert a list into set
programmingset= set(programminglist)

print(type(programmingset))
print(programmingset)
print("Satybhan knows these many languages", len(programmingset))