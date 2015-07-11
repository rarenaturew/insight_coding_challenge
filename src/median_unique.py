'''
This program is to calculate the running median of "number of unique words in a tweet". 
As new tweet comes in, the median need to be updated. 

The basic structure is to use a dictionary (num_count_dict) to hold {num_of_unique_words:count}.
The running median can then be calculated from this dictionary. 
The time complexity of the calculation of the median from the dictionary, is O(1), 
and the input file is read and processed line by line, 
therefore, the program is scalable: the duration of the execution is proportional to the size of the input file.

Author: Daoyan Wang
July 2015
'''

import sys

def num_count(in_file, out_file,option):
    ''' find the running median of the number of unique words in tweets. '''
    ''' option == 0 : no data munging; 
        option != 0 : convert letters to lower cases, and ignore empty lines. '''
    # num_count_dict is a num_of_unique_words:count dictionary.
    # This dictionary  map each possible num_of_unique_words with its count in the in_file.
    # The important point is that this dictionary corresponds to an ordered sequence from which
    # we calculate the median. For example, num_count_dict = {3:2, 4:3, 2:4} corresponds to
    # the ordered sequence: [2,2,2,2,3,3,4,4,4] whose median can be calculated as median=3.
    num_count_dict = {}  
    N_lines = 0 # number of lines: i.e. number of tweets
    input_file  = open(in_file, 'r')
    output_file = open(out_file, 'w')
    for line in input_file:
        # if option != 0, data munging by converting to lower case
        if option != 0:
            line = line.lower()
        unique_words = set(line.split()) # elements are unique in a set
        num_of_unique_words = len(unique_words)
        # if option != 0, ignore the empty lines
        if num_of_unique_words == 0 and option != 0:
            continue
        N_lines = N_lines + 1
        # if a new num_of_unique_words appears for the first time
        if not num_of_unique_words in num_count_dict:
            num_count_dict[num_of_unique_words] = 1
            # sort the keys, so that the keys are always sorted.
            # Since the length of this dictionary is very short anyway,
            # sorting takes very little time, and we only need to
            # perform very few sorting operations.
            sorted_keys= sorted(num_count_dict.keys())
        else:
            num_count_dict[num_of_unique_words] = num_count_dict[num_of_unique_words] + 1
        running_median = get_median(num_count_dict, sorted_keys, N_lines)
        #output_file.write(str(running_median)+'\n')
        output_file.write("%.2f\n" % running_median)
    input_file.close() 
    output_file.close()




def get_median(num_count_dict, sorted_keys, N_lines):
    ''' calculate the median, given a key/count dictionary, a sorted key list and 
        the total number of counts (N_lines) '''
    if ( N_lines != int(N_lines) ) or (N_lines <= 0) :
        print 'ERROR: N_lines should be an integer that is >= 1'
        sys.exit(1)
    elif N_lines == 1:
        the_median = sorted_keys[0]
    elif N_lines % 2 == 0:
        the_median = ( value_at(N_lines/2, num_count_dict, sorted_keys) \
                     + value_at(N_lines/2 + 1, num_count_dict, sorted_keys) )/2.0
    else:
        the_median = value_at( (N_lines + 1)/2, num_count_dict, sorted_keys )  
    return the_median



def value_at(position,num_count_dict,sorted_keys):
    ''' Given the position of a num_of_unique_words in the ordered sequence, 
        find the num_of_unique_words  '''
    if len(num_count_dict) == 0:
        return 0.0 
    p = 0 # to accumulate the number of counts from smallest num_of_unique_words in the ordered sequence
    for k in sorted_keys: # note: the keys of the dictionary are sorted 
        p = p + num_count_dict[k]
        if (p >= position) : # found it!!!! 
            the_value = k # this is the value at 'position' of the ordered sequence 
            break
    if p < position: #If this happens after the "for" loop, "position" is too large: out of the dictionary
          print "ERROR: position is out of the range of the dictionary (position > N_lines)"
          sys.exit(1)
    return the_value



def main():
    if (len(sys.argv) == 3) or (len(sys.argv) == 4):
        in_file  = sys.argv[1]
        out_file = sys.argv[2]
        option = 0
        if len(sys.argv)==4:
            option = 1 
        num_count(in_file, out_file,option)
    else:
        print 'usage: median_unique.py input_file output_file <option>'
        print '       default option is no option: no data munging'
        print '       if option is not empty: convert to lower cases, and ignore empty lines'
        sys.exit(1)



if __name__ == '__main__':
    main()
