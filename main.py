import requests
import re

def get_text(url):
    response = requests.get(url, stream=True, timeout=5)
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        if line:
            for word in re.findall(r'\b\w+\b', line.lower()):
                yield word

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    with open(words_file, 'r') as file:
        words_to_count = {line.strip().lower() for line in file if line.strip()}

    frequencies = {}
    for w in get_text(url):
        if w in words_to_count:
            frequencies[w] = frequencies.get(w, 0) + 1

    return frequencies


if __name__ == "__main__":
    print(main())