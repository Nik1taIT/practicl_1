numbers = input("Введіть числа по яким треба вирухувати суму(числа пишіть через пробіл):")
sum_of_numbers = sum(int(num) for num in numbers.split())
print(sum_of_numbers)