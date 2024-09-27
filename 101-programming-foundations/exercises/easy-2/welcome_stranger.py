def greetings(full_name, work):
    full_name = " ".join(full_name)
    work = work['title'] + ' ' + work['occupation']
    hello = f'Hello, {full_name}! Nice to have a {work} around.'
    return hello


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
