def greet(language):
    match language:
        case "en":
            return "English: Hi!"
        case "fr":
            return "French: Salut!"
        case "ro":
            return "Romanian: Bună!"
        case "hi":
            return "Hindi: नमस्ते / namaste!"
        case "es":
            return "Spanish: Hola!"
        case "sw":
            return "Swahili: Habari!"
        case "vi":
            return "Vietnamese: CHÀO!"
        case "sm":
            return "Samoan: Malo!"
        case _:
            return "Sorry, language not found."


# TEST
print(greet("en"))  # English: Hi!
print(greet("fr"))  # French: Salut!
print(greet("ro"))  # Romanian: Bună!
print(greet("hi"))  # Hindi: नमस्ते / namaste!
print(greet("es"))  # Spanish: Hola!
print(greet("sw"))  # Swahili: Habari!
print(greet("vi"))  # Vietnamese: CHÀO!
print(greet("sm"))  # Samoan: Malo!
print(greet("ab"))  # Sorry, language not found.
