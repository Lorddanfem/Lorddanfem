# user_name = input('Name: ')
# user_age = input ('Age: ')
# user_location = input ('Location: ')
# user = 'Hello {}, you are {} years old and live in {}'
# print(user.format(user_name, user_age, user_location))

# x = {}
# x[2] = 10
# x[1] = [20,30,40]
# print(x[1][2])

# prime_numbers = [1,3,5,7]
# prime_even = [2,4,6,8]
# prime_numbers.extend(prime_even)
# print('list of added number:', prime_numbers)

# my_tuple = ('a', 'd', 'g', 't', 'u', 'i', 'p')
# print(my_tuple [:])
# print(my_tuple [4:6])
# print(my_tuple[0:4])
# print(my_tuple[-1])

# state_capital = {'Lagos': 'Ikeja', 'Ondo': 'Akure', 'Benue': 'Makundi', 'Imo': 'Owerri', 'Adamawa': 'Yola'}
# print(state_capital)

# print('intial dictionary:', state_capital)
# state_capital['Osun']='Oshogbo'
# print('updated dictionary:', state_capital)

my_list = []
print(my_list)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.insert(2, 15)
print(my_list)
list = [50, 60, 70]
my_list.extend(list)
print(my_list)
del my_list[-1]
print(my_list)
my_list.sort()
print(my_list)
print(my_list[-4])