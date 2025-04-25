# write a program to fill a letter tempelate given below with name and date.

letter = '''dear <|Name|>,
    you are selected!
    <|Date|> '''

print(letter.replace("<|Name|>", "Shubhakant").replace("<||Date>", "20 March 2004"))