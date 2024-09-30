# Question !
'''
write a program that outputs The Flintstones Rock! 10 times, 
with each line prefixed by one more hyphen than the line above it.
'''
def flintstones(words):
    for i in range(1,11):
        print(('-' * i) + words)


word: str = 'The Flintstones Rock!'

flintstones(word)

# Question 10
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))