capital = input("Please put in the sentence to capitalize: ")
capital_list = []
new_capital = ""
ignore_list = ["a", "an", "or", "for", "the", "and"]
number_of_space = capital.count(" ")
previous_space = 0
ignore_test = False

for i in range(0, number_of_space + 1):
  space = capital.find(" ")
  if (i == number_of_space):
    capital_list.append(capital[previous_space:])
  else:
    capital_list.append(capital[previous_space:space])
  capital = capital.replace(" ", "", 1)
  previous_space = space

for i in range(0, len(capital_list)):
  if i != 0:
    ignore_test = False
    for j in range(0, len(ignore_list)):
      if capital_list[i].lower() == ignore_list[j]:
        new_capital += " " + capital_list[i]
        ignore_test = True
        break
    if ignore_test == False:
      new_capital += " " + capital_list[i].capitalize()
    else:
      pass
  else:
    new_capital += capital_list[i].capitalize()
