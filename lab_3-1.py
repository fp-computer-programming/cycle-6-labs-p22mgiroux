#Author: MOG 11/12/21

my_row = ["Charlie", "Mohamed"]
my_row[len(my_row):] = ["Michael"]

my_row2 = my_row
print(my_row2)

del my_row[1]
print(my_row)