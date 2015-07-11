import sys

def word_count(in_file,option):
  """Returns a word/count dictionary for this in_file."""
  # word_count_dict is the word:count dictionary. 
  word_count_dict = {}  # Map each word to its count
  input_file = open(in_file, 'r')
  for line in input_file:
    words = line.split()
    for word in words:
      # if option !=0, do munging by convert to lower cases:
      if option != 0:
        word = word.lower()
      # if we're seeing this word for the first time:
      if not word in word_count_dict:
        word_count_dict[word] = 1
      else:
        word_count_dict[word] = word_count_dict[word] + 1
  input_file.close() 
  return word_count_dict


def print_words(in_file, out_file, option):
  """Prints one per line '<word> <count>' sorted by word for the given file."""
  word_count_dict = word_count(in_file,option)
  # sort the words: i.e. the keys of the dictionary
  sorted_words = sorted(word_count_dict.keys())
  output_file = open(out_file, 'w')
  for word in sorted_words:
    output_file.write("{:<50}  {:<25}\n".format(word, word_count_dict[word]))
  output_file.close()



def main():
  """ Do word count from input_file and output the result to output_file
      in a alphabetical order."""
  if (len(sys.argv) == 3) or (len(sys.argv) == 4):
    in_file  = sys.argv[1]
    out_file = sys.argv[2]
    option = 0 # default option: no data munging
    if len(sys.argv)==4:
      option = 1 # do data munging by converting letters to lower cases
    print_words(in_file, out_file, option)
  else:
    print 'usage: word_tweeted.py input_file output_file <option>'
    print '       default option is no option: no data munging'
    print '       if option is not empty: convert to lower cases'
    sys.exit(1)


if __name__ == '__main__':
  main()
