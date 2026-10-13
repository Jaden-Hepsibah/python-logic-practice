word = input("Enter a word: ")

vowels= 0
consonant= 0
vowel= ["a","e","i","o","u"] 
for ch in word:
  if ch.isalpha():
    if ch in vowel:
      vowels+=1
    else:
      consonant+=1
print(vowels)
print(consonant)
