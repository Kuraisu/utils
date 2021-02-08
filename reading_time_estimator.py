import bs4
import urllib.request
import re

# Words per minute
WPM = 200
WORD_LENGTH = 5

def extract_text(url):
    html = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    return texts


def is_visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif isinstance(element, bs4.element.Comment):
        return False
    elif element.string == "\n":
        return False
    return True

def filter_visible_text(page_texts):
    return filter(is_visible, page_texts)


def count_words_in_text(text_list, word_length):
    total_words = 0
    for current_text in text_list:
        total_words += len(current_text)/word_length
    return total_words

def estimate_reading_time(url):
    texts = extract_text(url)
    filtered_text = filter_visible_text(texts)
    total_words = count_words_in_text(filtered_text, WORD_LENGTH)
    print(texts)
    print(filtered_text)
    print(total_words)
    return total_words/WPM

print(estimate_reading_time("https://www.notion.so/13ef2d4adb94486c9e22a0604f21bf22"))
