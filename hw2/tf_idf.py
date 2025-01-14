# tf_idf_bayes.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Justin Lizama (jlizama2@illinois.edu) on 09/28/2018
# Modified by Jaewook Yeom 02/02/2020
# Modified by Kiran Ramnath 02/13/2021
"""
This is the main entry point for the Extra Credit Part of this MP. You should only modify code
within this file for the Extra Credit Part -- the unrevised staff files will be used when your
code is evaluated, so be careful to not modify anything else.
"""

import numpy as np
import math
from collections import Counter, defaultdict
import time
import operator


def compute_tf_idf(train_set, train_labels, dev_set):
    """
    train_set - List of list of words corresponding with each mail
    example: suppose I had two mails 'like this city' and 'get rich quick' in my training set
    Then train_set := [['like','this','city'], ['get','rich','quick']]

    train_labels - List of labels corresponding with train_set
    example: Suppose I had two mails, first one was ham and second one was spam.
    Then train_labels := [1, 0]

    dev_set - List of list of words corresponding with each mail that we are testing on
              It follows the same format as train_set

    Return: A list containing words with the highest tf-idf value from the dev_set documents
            Returned list should have same size as dev_set (one word from each dev_set document)
    """
    # TODO: Write your code here
    train_docs = len(train_set) # total num of docs in train set
    train_words = Counter() # num of docs in train set containing word w
    out = []
    # go through each document in train_set
    for doc in train_set:
        words_in_doc = []
        # find all unique words in doc
        for word in doc:
            words_in_doc.append(word)
        # increment train_words by 1 for each unique word in doc
        for word in words_in_doc:
            train_words[word] += 1
    # development time
    for doc in dev_set:
        doc_words = len(doc) # total num of words in doc
        words = Counter() # num of times word w appears in doc
        for word in doc:
            words[word] += 1
        # iterate through
        output_word = ""
        tf_idf = 0
        for word in words:
            compare = words[word]/doc_words * math.log(train_docs/(1+train_words[word]))
            if tf_idf < compare:
                output_word = word
                tf_idf = compare
        out.append(output_word)

    # return list of words (should return a list, not numpy array or similar)
    return out
