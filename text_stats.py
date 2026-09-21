import string
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
