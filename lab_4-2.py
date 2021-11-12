#Author: MOG 11/12/21

classes = ["Math", "Science", "Tech"]
print(classes)

classes.append("History")
print(classes)

print(classes.index("Tech"))

classes.sort()
print(classes)

more_classes = classes.copy()

more_classes.reverse()
print(more_classes)