with open("currency_data.txt") as op:
    data = op.readlines()

curr_dict = {}
for line in data:
    parsed = line.split("\t")
    curr_dict[parsed[0]] = parsed[1]

amount = int(input("Enter amount: \n"))
print("Enter the name of the currency you want to convert this amount to? Available Options: \n")
[print(item) for item in curr_dict.keys()]
curr_name = input("Please enter one of these values: ")
print(f"{amount} INR is equal to  {amount * float(curr_dict[curr_name])} {curr_name}")

