number = 4259
digits = [int(digit) for digit in str(number)]
digits_sum = sum(digits)
print(f"{' + '.join(map(str, digits))} = {digits_sum}")