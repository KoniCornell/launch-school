# Question 1
numbers = [1, 2, 3]
#numbers[6] = 5 # out of range error

# Question 2 - check string ends with !
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(str1[-1] == '!') 
print(str2[-1] == '!')

# print(str1.endswith("!"))  # True
# print(str2.endswith("!"))  # False

# Question 3
famous_words = "seven years ago..."
start_with = "Four score and " 
new_string = f"Four score and {famous_words}"
print(new_string)
print(start_with + famous_words)

# Question 4
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
print(munsters_description.capitalize())
# print(munsters_description[0].upper() + munsters_description[1:].lower())

# Question 5
munsters_description = "The Munsters are creepy and spooky."
print(munsters_description.swapcase())

# Question 6
# check if Dino appears in the given strings
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
print('Dino' in str1)
print('Dino' in str2)

# Question 7
# add the family pet, "Dino"
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append('Dino')
flintstones.extend(['Happy', 'Fred', 'Barney'])
#flintstones += ['Happy', 'Fred', 'Barney']
print(flintstones)

# Question 8
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

advice = advice.split('house')
print(advice[0])

# Question 10
advice = "Few things in life are as important as house training your pet dinosaur."
advice = advice.split('important')

#advice = advice.replace('important', 'urgent')
print('urgent'.join(advice))