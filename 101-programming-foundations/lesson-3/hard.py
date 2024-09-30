# Question 2 What does the last line in the following code output?
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)     # [1, 2]
print(dictionary)   # {'first': [1, 2]}


