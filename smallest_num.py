number_input=input("enter the numbers by space:")
number_split=number_input.split()
smallest=int(number_split[0])
for num in number_split[1:]:
    if int(num)<=smallest:
        smallest=int(num)
print("the smallest number is:",smallest)