"""
Problem

Ursula is a big fan of constructing artificial languages. Today, she is starting to work on a language inspired by real 
Polynesian languages. The only rules she has established are:

All words consist of letters. Letters are either consonants or vowels.
Any consonant in a word must be immediately followed by a vowel.
For example, in a language in which a is the only vowel and h is the only consonant, a, aa, aha, aaha, and haha are 
valid words, whereas h, ahh, ahah, and ahha are not. Note that the rule about consonants disallows ending a word in a 
consonant as well as following a consonant with another consonant.

If Ursula's new language has C different consonants and V different vowels available to use, then how many different 
valid words of length L are there in her language? Since the output can be a really big number, we only ask you to 
output the remainder of dividing the result by the prime 109+7 (1000000007).

Solving this problem

This problem has 2 Small inputs and 1 Large input. You must solve the first Small input before you can attempt the 
second Small input. You will be able to retry either of the Small inputs (with a time penalty). You will be able to 
make a single attempt at the Large, as usual, only after solving both Small inputs.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with 
three integers C, V, and L.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y 
is the number of different valid words of length L in the language, modulo the prime 109+7 (1000000007).

Limits

Small dataset 1

T = 15.
C = 1.
V = 1.
1 ≤ L ≤ 15.
Small dataset 2

1 ≤ T ≤ 100.
1 ≤ C ≤ 50.
1 ≤ V ≤ 50.
1 ≤ L ≤ 15.
Large dataset

1 ≤ T ≤ 100.
1 ≤ C ≤ 50.
1 ≤ V ≤ 50.
1 ≤ L ≤ 500.

Input
2
1 1 4
1 2 2

Output
Case #1: 5
Case #2: 6


"""

from collections import Counter

from CodeJam import CodeJamProblem


class C(CodeJamProblem):
    def __init__(self):
        super().__init__('C')

    def generate_test_cases(self, input_file):
        pass

    def solve(self, t):
        pass



