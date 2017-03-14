"""
Problem

You just bought your young nephew Andrey a complete set of 26 English wooden alphabet 
letters from A to Z. Because the letters come in a long, linear package, they appear 
to spell out a 26-letter message.

You use N different passwords to log into your various online accounts, and you are 
concerned that this message might coincidentally include one or more of them. Can you 
find any arrangement of the 26 letters, such that no password appears in the message 
as a continuous substring?

Solving this problem

This problem has 2 Small inputs and no Large input. You must solve the first Small input 
before you can attempt the second Small input. You will be able to retry either of the 
Small inputs (with a time penalty).

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each 
consists of one line with an integer N, and then another line with N different strings 
of uppercase English letters P1, P2, ..., PN, which are the passwords.

Output

For each test case, output one line containing Case #x: y, where x is the test case 
number (starting from 1) and y is a permutation of the entire uppercase English alphabet 
that contains no password as a continuous substring, or the word IMPOSSIBLE if there 
is no such permutation.

Limits

1 ≤ T ≤ 100.
1 ≤ length of Pi ≤ 26, for all i. (Each password is between 1 and 26 letters long.)
Pi ≠ Pj for all i ≠ j. (All passwords are different.)
Small dataset 1

N = 1.
Small dataset 2

1 ≤ N ≤ 50.




Input 
 	
7
1
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1
X
1
QQ
5
XYZ GCJ OMG LMAO JK
3
AB YZ NM
6
C PYTHON GO PERL RUBY JS
2
SUBDERMATOGLYPHIC UNCOPYRIGHTABLES



Output 
 
Case #1: QWERTYUIOPASDFGHJKLZXCVBNM
Case #2: IMPOSSIBLE
Case #3: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Case #4: ABCDEFGHIKLMNOPQRSTUVWXYJZ
Case #5: ZYXWVUTSRQPOMNLKJIHGFEDCBA
Case #6: IMPOSSIBLE
Case #7: THEQUICKBROWNFXJMPSVLAZYDG



"""

from collections import Counter

from CodeJam import CodeJamProblem


class D(CodeJamProblem):
    def __init__(self):
        super().__init__('D')

    def generate_test_cases(self, input_file):
        pass

    def solve(self, t):
        pass



