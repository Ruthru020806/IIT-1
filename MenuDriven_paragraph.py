paragraph = input("Enter a Paragaraph:")
words = paragraph.split()
doc_length = 0
for _ in words:
    doc_length += 1
word_counts = {}
repetitive_words = []
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
for word in word_counts:
    if word_counts[word] > 1:
        repetitive_words.append(word)
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
reversed_longest = ""
index = len(longest_word) - 1
while index >= 0:
    reversed_longest += longest_word[index]
    index -= 1
print("\n-----------------------Repetitive Words-----------------------------\n")
for key, value in sorted(word_counts.items(),key= lambda item: item[1]):
   if(value > 1):
      print(f"({key}:{value})")
print(f"Repetitive Words: {repetitive_words}")
print("Length of Documentation:",doc_length)
print("Longest Word:",longest_word)
print("Reversed Longest Word:",reversed_longest)
