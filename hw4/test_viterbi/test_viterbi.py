# mp4.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created Fall 2018: Margaret Fleck, Renxuan Wang, Tiantian Fang, Edward Huang (adapted from a U. Penn assignment)
# Modified Spring 2020: Jialu Li, Guannan Guo, and Kiran Ramnath
# Modified Fall 2020: Amnon Attali, Jatin Arora
# Modified Spring 2021 by Kiran Ramnath (kiranr2@illinois.edu)

"""
This file should not be submitted - it is only meant to test your implementation of the Viterbi algorithm.
"""
import numpy as np
from utils import read_files, get_nested_dictionaries
import math
smoothing_constant = 1e-10

def main():
    test, emission, transition, output = read_files()
    emission, transition = get_nested_dictionaries(emission, transition)
    initial = transition["S"]
    prediction = []

    """WRITE YOUR VITERBI IMPLEMENTATION HERE"""
    # print("emission: ",emission)
    # print()
    # print("transition: ",transition)
    # print()
    backtrack = {}
    probs = {}
    for tag in initial:
        probs[(0,tag)] = math.log(initial[tag]) + math.log(emission[tag][test[0][0]])
        backtrack[(0,tag)] = 0
    print(probs)
    for message in test:
        for i in range(1,len(message)):
            word = message[i]
            for tag in emission:
                rates = float("-inf")
                best = ""
                for prev in transition[tag]:
                    likelihood = math.log(transition[prev][tag]) + probs[(i-1,prev)] + math.log(emission[tag][word])
                    if rates < likelihood:
                        rates = likelihood
                        best = prev
                backtrack[(i,tag)] = (i-1,best)
                probs[(i,tag)] = rates
        best = ""
        rate = float("-inf")
        for tag in emission:
            if rate < probs[len(message)-1,tag]:
                best = tag
                rate = probs[len(message)-1,tag]
        i = len(message)-1
        tuple = (i,best)
        while i >= 0:
            prediction.insert(0,(message[i],tuple[1]))
            tuple = backtrack[tuple]
            i -= 1
    print('Your Output is:',prediction,'\n Expected Output is:',output)


if __name__=="__main__":
    main()
