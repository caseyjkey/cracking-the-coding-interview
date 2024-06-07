import string
import heapq
from collections import defaultdict
# Design a method to find frequency of occurrences of any given word in a book
# What if we were running this multiple times?
text = "Yes, the concordance should work; I had thought there might be a way to list the most frequent words in order of occurrence. My guess is to set ..."
words = text.translate(str.maketrans('', '', string.punctuation))
words = words.split()
wordCounts = defaultdict(int)
for word in words:
    wordCounts[word] += 1
words = [(count, word) for word, count in wordCounts.items()]
print("largest 3 words", heapq.nlargest(3, words))
