marks = {
    "Shubhakant": 100,
    "Vinay": 101,
    "Shubham": 89,
    0: "Shubhakant"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Vinay": 99, "Renuka":100})
print(marks)

print(marks.get("Vinay2")) # print None
print(marks["Vinay2"]) # returns an error