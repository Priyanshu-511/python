hindi_to_english = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "पानी": "Water",
    "भोजन": "Food",
    "किताब": "Book"
}

def lookup_word(word):
    return hindi_to_english.get(word, "Word not found")

while True:
    user_input = input("Enter a Hindi word to translate (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    print(lookup_word(user_input))
