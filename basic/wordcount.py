

"""Wordcount exercise
Google's Python class

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

def process_file(filename):
  with open(filename, "rU") as my_file:
    my_file_list = my_file.readlines()
  return my_file_list 


def count_words(file_list):
  words_count = {}
  for phrase in file_list:
    lower_phrase = phrase.lower().split()
    for word in lower_phrase:
      if word not in words_count:
        words_count[word] = 1
      else:
        words_count[word] +=1

  return words_count

def print_sorted(dic):
  for key in sorted(dic.keys()):
    print key , ":" , dic[key]
    

def top_count(dic):
  def count(key):
    return dic[key]
  top = sorted(dic, key=count, reverse= True)
  for key in top[:20]:
    print key, dic[key]


def menu_gral():
  menu = ("""
    Hello There!
    What file do you want to process:
    1. Small
    2. Alice
    3. Exit
     """)
  option = raw_input(menu)
  return option

def menu_file():
  menu = ("""
    What do you want to do with this file:
    1. Count words:
    2. Count top words
    3. Return gral menu
     """)
  option = raw_input(menu)
  return option

def main():
  user_choice = menu_gral()
  while True:
    if user_choice == "1":
      my_file_small = process_file("/Users/cristina/source/google-python-exercises/basic/small.txt")
      dictionary_small = count_words(my_file_small)
    
      question = menu_file()
      if question == "1":
        print_sorted(dictionary_small)
      elif question == "2":
        top_count(dictionary_small)
      else:
        user_choice = menu_gral()

    elif user_choice == "2":
      my_file_alice = process_file("/Users/cristina/source/google-python-exercises/basic/alice.txt")
      dictionary_alice = count_words(my_file_alice)

      question = menu_file()
      if question == "1":
        print_sorted(dictionary_alice)
      elif question == "2":
        top_count(dictionary_alice)
      else:
        user_choice = menu_gral()

    else:
      break







if __name__ == '__main__':
  main()
