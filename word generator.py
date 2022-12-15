import random
# random word generating function
def random_words():
  # list to keep random words
  words = []

  # generate a certain number of words
  for i in range(100):
    # make a word
    word = ""
    for j in range(10):
      # create the word from random letters and random special characters
      if random.random() < 0.5:
        # create letters
        word += chr(ord('a') + int(random.random() * 26))
      # create capital letters
      elif random.random() < 0.33:
        word += chr(ord('A') + int(random.random() * 26))
      # create special characters
      else:
        word += chr(ord('!') + int(random.random() * 15))
    # add the generated word to the list
    words.append(word)

  
  return words

# generate random words
words = random_words()

# creating new file 
with open("newfile.txt", "w") as f:
  # write the words to the file
  for word in words:
    f.write(word + "\n")
