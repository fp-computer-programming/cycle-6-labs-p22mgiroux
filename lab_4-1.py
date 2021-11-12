#Author: MOG 11/12/21

colors = ["red", "orange", "yellow", "green"]
colors.extend(["blue", "indigo", "violet"])
print(colors.count("yellow"))
colors.insert(3, "slightly more yellow")
colors.clear()
print(colors.count("red"))