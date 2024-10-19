def sum_even_numbers(numbers):
    return sum(filter(lambda x: x % 2 == 0, numbers))

numbers_list = [1, 2, 3, 4, 5, 6]
result = sum_even_numbers(numbers_list)
print(f"The sum of even numbers is: {result}")
