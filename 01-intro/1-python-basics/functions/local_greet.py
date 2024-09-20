def locale_language(locale): # finds language code
    return locale[0:2]

def extract_region(locale): # finds region code
    return locale[3:5]

def greet(language): # greets based on argument of language code
    match language:
        case "en":
            return "Hi!"
        case "fr":
            return "Salut!"
        case "ro":
            return "Bună!"
        case "hi":
            return "नमस्ते"
        case "es":
            return "Hola!"
        case "sw":
            return "Habari!"
        case "vi":
            return "CHÀO!"
        case "sm":
            return "Malo!"
        case _:
            return "Sorry, language not found."

def local_greet(locale):
    if locale_language(locale) == "en": 
    # if en is language code check for specific regions to greet
        match extract_region(locale):  # match-case for locales region
            case "US":
                return "Hey!"
            case "GB":
                return "Hello!"
            case "AU":
                return "G'day!"
            case _:  # en language code but region code not specified
                return "Hi!"
    else: # language code != 'en'
        return greet(locale_language(locale))
        # use previous function as argument for language code

# TEST
print(local_greet("en_US.UTF-8"))  # Hey!
print(local_greet("en_GB.UTF-8"))  # Hello!
print(local_greet("en_AU.UTF-8"))  # G'day!
print(local_greet("en_NZ.UTF-8"))  # Hi!
print(local_greet("fr_FR.UTF-8"))  # Salut!
print(local_greet("fr_CA.UTF-8"))  # Salut!
print(local_greet("fr_MA.UTF-8"))  # Salut!
print(local_greet("ro_MA.UTF-8"))  # Buna!
print(local_greet("hi_MA.UTF-8"))  # नमस्ते
print(local_greet("ab_MA.UTF-8"))  # Language not found.