# with open("article.txt","r",encoding="utf-8")as file:
#     text = file.read().split()
#     print(f"length of longest word in text is: {len(max(text,key = len))}")

from collections import Counter
import string
with open("article.txt","r",encoding="utf-8")as text_file:
    text = text_file.read()
text = text.lower()

text = text.translate(str.maketrans("", "", string.punctuation))

# frequency = Counter(text.split())
# print(frequency)
# top10 = frequency.most_common(3)
# print(top10)
# for word,count in top10:
#     print(word,count)

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text
def load_text(file_path):
    with open(file_path, "r",encoding = "utf-8") as file:
        return file.read()

def word_count(text):
    text = clean_text(text)
    return len(text.split())

def unique_word_count(text):
    text = clean_text(text)
    return len(set(text.split()))

if __name__ == "__main__":
    text = load_text("article.txt")
    print(f"Word count: {word_count(text)} Unique word count: {unique_word_count(text)}")
