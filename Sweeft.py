# 1
# my_list = []
# num = int(input('Enter the number: \n'))
# count = 1
# whole_word = ''
# how_many = int(input('How many word do you want to enter: '))
# for _ in  range(how_many):
#     word = input('Enter the word: \n')
#     whole_word += word
#     my_list.append(word)
#     count += 1
# if len(whole_word) < pow(10, 6) and count <= pow(10, 5) and whole_word.islower():
#     unique_word = set(my_list)
#     length = len(unique_word)
#     print(length)
#     my_dict = {}
#     for each in my_list:
#         if each in my_dict:
#             my_dict[each] += 1
#         else:
#             my_dict[each] = 1
#     for each in my_dict:
#         print(my_dict.get(each), end=' ')

# 2
# def bigger_Is_greater(word):
#     index = 0
#     for _ in range(word):
#         try:
#             b = my_list[index - 2]
#             x = my_list[index - 1]
#             if x > b:
#                 if x > my_list[index] and my_list[index] > b:
#                     my_list[index - 1], my_list[index] = my_list[index], my_list[index - 1]
#                     my_list[index - 1], my_list[index - 2] = my_list[index - 2], my_list[index - 1]
#                     result_list.append(' '.join(my_list))
#                     break
#                 else:
#                     my_list[index - 1], my_list[index - 2] = my_list[index - 2], my_list[index - 1]
#                     result_list.append(' '.join(my_list))
#                     break
#         except:
#             result_list.append("no answer")
#         index -= 1
#
# num = int(input("Enter the number: "))
# result_list = list()
# for i in range(num):
#     text = input("enter the word: ")
#     my_list = list()
#     for each in text:
#         my_list.append(each)
#
#     listlength = len(my_list)
#     bigger_Is_greater(listlength)
# print(num)
# answer = ""
# for each_value in result_list:
#     if each_value == " ":
#         continue
#     for space_deleter in each_value:
#         if space_deleter == " ":
#             continue
#         answer += space_deleter
#     print(answer)
#     answer = ""

# 3
import random
text = ''
new_text = ''
for i in range(3):
    for j in range(4):
        text += '. '
    text += '\n'
    for k in range(4):
        char = random.choice('.O')
        new_text += (char + ' ')
    new_text += '\n'

print(new_text.replace('. ', 'O '))










