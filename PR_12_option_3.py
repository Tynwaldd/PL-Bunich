#Блок_А
def reverse_number(n):
    if n < 0:
        print('-', end='')
        n = -n
    
    if n < 10:
        print(n, end='')
    else:
        print(n % 10, end='')
        reverse_number(n // 10)

number = int(input("Введите число: "))
if number == 0:
    print(0)
else:
    reverse_number(number)

#Блок_Б
def print_odd_position_numbers(position=1):
    number = int(input())
    
    if number == 0:
        return

    if position % 2 != 0:
        print(number)

    print_odd_position_numbers(position + 1)

print_odd_position_numbers()

