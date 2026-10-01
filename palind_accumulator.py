word = input("Enter a word/number:  ").lower()
reversed_word = ""
for ch in word:
  reversed_word = ch + reversed_word
print(reversed_word)

if word == reversed_word:
  print("this is palindrome")

else:
  print("this is not plaindrome")