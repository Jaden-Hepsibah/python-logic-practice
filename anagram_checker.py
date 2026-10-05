word = input("Enter a word: ").lower()
word1 = input("Enter another word: ").lower()

if sorted(word) == sorted(word1):
  print("This is anagram")
else:
  print("This is not anagram")