capital = input("Please put in the sentence to capitalize: ")
new_capital = ""
ignore_list = ["the, or, a"]

for i in range(0, len(capital) + 1):
  if i == 0:
    new_capital += capital[i].upper()
  if i > 0:
    if capital[i] == " ":
      new_capital += capital[i + 1].upper()
  
  i += 1

print(new_capital)
  

