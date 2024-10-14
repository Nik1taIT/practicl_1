number = int(input("Enter a four-digit number: "))
digits = [int(digit) for digit in str(number)]
digits_sum = sum(digits)
print(f"{' + '.join(map(str, digits))} = {digits_sum}")