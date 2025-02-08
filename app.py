#greeting function 
def greet(name, language="en"):
    greetings = {
        "en": "Hello",
        "es": "Hola", 
        "fr": "Bonjour",
        "de": "Halo"
    }
    return f"{greetings.get(language, 'Hello')}, {name}!"

if __name__ = "__main__":
    user = input("Enter your name: ")
    lang = input("Choose a langauge (en/es/fr/de): ")
    print(greet(user, lang))