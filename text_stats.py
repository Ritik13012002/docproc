# with open("article.txt","r",encoding="utf-8")as file:
#     text = file.read().split()
#     print(f"length of longest word in text is: {len(max(text,key = len))}")

from collections import Counter
import string
with open("article.txt","r",encoding="utf-8")as text_file:
    text = text_file.read()
text = text.lower()

text = text.translate(str.maketrans("", "", string.punctuation))

frequency = {}
for word in text.split():
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word]=1

print(frequency)

# frequency = Counter(text.split())
# print(frequency)
# top10 = frequency.most_common(3)
# print(top10)
# for word,count in top10:
#     print(word,count)

sorted_frequency = sorted(frequency.items(),key=lambda x:x[1],reverse=True)
print(sorted_frequency[:10])
