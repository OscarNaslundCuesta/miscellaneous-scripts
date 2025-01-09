import requests
from bs4 import BeautifulSoup
import time


def scrape_word_from_spraakbanken(word):
    """
    Scrape the Saldo WS demo page for the given word.
    Print the result if 'ordet saknas i lexikonet' is not present.
    """
    url = f"https://demo.spraakbanken.gu.se/ws/saldo-ws/fl/html?segment={word}"
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues (e.g., 404)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Check if the string "ordet saknas i lexikonet" exists
        if "ordet saknas i lexikonet" not in soup.text:
            print(f"The word '{word}' exists in the lexicon.")

    except requests.exceptions.RequestException:
        # Silently skip words causing a 404 or other HTTP errors
        pass


list1 = ["s", "a", "k", "b", "u"]
list2 = ["s", "i", "a", "k", "t"]
list3 = ["l", "r", "o", "e", "t"]
list4 = ["a", "l", "n", "k", "r"]

list1.sort()
list2.sort()
list3.sort()
list4.sort()

for i1 in range(0, len(list1)):
    for i2 in range(0, len(list2)):
        for i3 in range(0, len(list3)):
            for i4 in range(0, len(list4)):
                word = "".join([list1[i1], list2[i2], list3[i3], list4[i4]])
                print("Processing", word)
                scrape_word_from_spraakbanken(word)
                time.sleep(0.1)
