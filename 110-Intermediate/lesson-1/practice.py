# problem 1
fruits = ("apple", "banana", "cherry", "date", "banana")
print(fruits.count('banana')) # 2

# problem 2
numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers)) # 5 (no duplicates in a set)

# problem 3
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a | b
print(a.union(b))
# print(c)

# problem 4
names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)

# problem 5
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}
get_ages = list(ages.values())
print(sum(get_ages))
# print(sum(ages.values()))

# minimum age
min_age = min(ages.values())

for name, age in ages.items():
    if age == min_age:
        print(f'The minimum age is "{name}" : {age}')

# problem 7
words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)

# problem 8
statement = "The Flintstones Rock"


# dictionary with letter freaquency (case sensitive)
letter_freq = {}
for letter in statement:
    if letter == ' ':
        continue
    letter_freq[letter] = statement.count(letter)

print(letter_freq)

# problem 9 list comprehensions
print([num for num in [1, 2, 3] if num > 1]) # [2, 3]

# problem 10
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

# problem 11
lst = [1, 2, 3, 4, 5]
print(lst[:2])

# problem 12
frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)  ## This will raise an error: AttributeError
print(frozen)
