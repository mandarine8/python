# Reverse Words Exercise:

input_value = input("Please enter a sentence: ")
print(input_value)

words = input_value.split(" ")
print(words)

words.reverse()
print(words)

new_sentence = ' '.join(words)
print(new_sentence)

# Naive 10 Characters splitter exercise:

# def char_splitter(input):
# Count Characters
# Cut at 10
# Insert \n

#characters = input("entrer une phrase: ")
#nb_characters = len(characters)
#print(nb_characters)

s = "hello toi moi cest tchouptchoup"

#print(s[:10])
#s = s[10:]
#print(s[:10])
#s = s[10:]
#print(s[:10])
#s = s[10:]
#print(s[:10])
#s = s[10:]
#print(s[:10])
#s = s[10:]

aligned_text = ""

while len(s) != 0:
  aligned_text += s[:10]
  if len(s) >= 10:
    aligned_text += "\n"
  s = s[10:]

print(aligned_text)

# print(s[:10])
# print(s[10:])
# print(s[:10] + "n" + s[10:])
# print(characters.split("*"))r
# print(s.split(" ", maxsplit=1))
# print(s.splitlines(10))
