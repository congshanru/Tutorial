words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]


from collections import Counter

word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

print(word_counts['not'])
print(word_counts['eyes'])

morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts['eyes'])

word_counts.update(morewords)
print(word_counts['eyes'])


a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
# Combine counts
c = a + b
print(c)
# Subtract counts
d = a - b
print(d)