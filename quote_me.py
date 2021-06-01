import json
from random import randint
import pyperclip

def main():
    file_name = "quotes.json"

    with open(file_name, encoding="Latin-1") as file:
        data = json.load(file)

    quote_int = randint(0,len(data))

    quote = data[quote_int]
    quote_text = quote['text']
    quote_src = quote['from']
    final_str = f"Here's a nice quote for you from {quote_src}:\n{quote_text}"

    print(final_str)
    pyperclip.copy(final_str)

if __name__ == '__main__':
    main()