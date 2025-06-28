# Write a program to greet all the persons names stored in a list 'l' and which starts with S. 
# l = ["Hrry", "shubhakant", "vinay", "radha"]

l = ["Harry", "shubhakant", "vinay", "radha"]

for name in l:
    if(name.startswith("s")):
        print(f"Hello {name}")