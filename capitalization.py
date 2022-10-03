capital = input("Please put in the sentence to capitalize: ")
capital_list = []
new_capital = ""
ignore_list = ["or, a"]
number_of_space = capital.count(" ")
previous_space = 0

for i in range(0, number_of_space + 1):
  
  space = capital.find(" ")
  if (i == number_of_space):
    capital_list.append(capital[previous_space:])
  else:
    capital_list.append(capital[previous_space:space])
  capital = capital.replace(" ", "", 1)
  previous_space = space