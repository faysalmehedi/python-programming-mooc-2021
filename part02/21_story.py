# Write your solution here

story = ""
prev_word = ""

while True:
    word = input("Please type in a word: ")
    if word == 'end' or word == prev_word:
        break
    else:
        story += word
        story += " "
        prev_word = word

print(story)
