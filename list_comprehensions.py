# Lists Comprehensions
my_list = [i ** 2 for i in range(10)]
print(my_list)

fruits = ["Banana", "Lemon", "Orange", "apple", "Birne"]
list2 = [fruit for fruit in fruits if fruit[0] == "B"]
print(list2)
prices = [25, 2, 3, 48]

# Nested List Comprehensions
fruits_prices = [[fruit, price] for fruit in fruits for price in prices]
print(fruits_prices)
