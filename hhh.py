my_list = [123, 'spam', 1.23, 'NI']
del my_list[2]  
print(my_list)  # [123, 'spam', 'NI']

another_list = ['abc', my_list, 42]
del another_list[1][2]  # удаляем ‘NI’ из вложенного списка my_list
my_list  # [123, 'spam']

list_one = ['spam', 1, 11, 111]
list_two = [2, 22, 'spam', 222]
list_three = [3, 'spam', 33, 333]
del list_one[0], list_two[2], list_three[1]  # удаляем spam одновременно из трёх списков