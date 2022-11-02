import random
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

# f = open('Practice\persistence.txt', 'w')
# Task 1
# for person in people:
#     f.write(person)
#     f.write('\n')

# Task 2
# try:
#     f = open('persistence.txt', 'w')
#     for person in people:
#         f.write(person)
#         f.write('\n')  
# except Exception as e:
#     print(e)

# Task 3
# try:
#     f = open('persistence.txt', 'w')
#     for person in people:
#         f.write(person)
#         f.write('\n')  
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# Task 4
# try:
#     with open('Practice\persistence.txt', 'w') as words:
#         for person in people:
#             # words.write('\n'.join(people))  
#             words.write(person)
#             words.write('\n')  
# except Exception as e:
#     print('Error. Text', e)
# finally:
#     words.close()

# Task 5
try:
    with open('Practice\persistence.txt', 'w') as words:
        for person in people:
            words.write(random.choice(people) + '\n')
except Exception as e:
    print('Error. Text', e)
finally:
    words.close()