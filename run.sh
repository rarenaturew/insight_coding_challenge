#!/usr/bin/env bash

if [ $# -eq 0 ] ; then
  python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt 
  python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt 
else
  echo "  "
  echo "       Performing the option with data munging........ "
  python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1_$1.txt  1 
  python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2_$1.txt  1
fi


cat<<END2 


*******************************************************************************
*                                                                             *
*                                  DONE !                                     *
*                                                                             *
*                                                                             *
*                       MORE OPTIONS ARE POSSIBLE:                            *
*                                                                             *
*  Functionality:                                                             *
*  Taking ./tweet_input/tweets.txt as the input file, to perform the counts   *
*  for all words, and to produce running median for number of unique words    *
*  in each line of the input files.                                           *
*  Outputs are in the folder ./tweet_output.                                  *
*                                                                             *
*  Usage: run.sh <option>                                                     *
*         The default situation is "no option": no data munging.              *
*                                                                             *
*         If <option> is not empty: the program will convert capital letters  *
*                                   into lower cases, and ignore empty lines. *
*                                   Try: " run.sh 1 "                         *
*                                                                             *
*******************************************************************************
END2

