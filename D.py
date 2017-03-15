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

from CodeJam import *
from collections import defaultdict
import string
import random

impossible = "IMPOSSIBLE"


class D(CodeJamProblem):
    def __init__(self):
        super().__init__('D')

    def generate_test_cases(self, input_file):
        with open(input_file) as f:
            for _ in range(int(next(f).strip())):
                next(f)
                yield next(f).strip().split(" ")

    def solve(self, pwds):
        def test(hay, needles):
            return not exists(needles, lambda needle: needle in hay)

        assert len(pwds) <= 50, "no solution for more than that, for now!"
        if exists(pwds, lambda s: len(s) == 1):
            return impossible

        # remove all the passwords that have a repeating letter in them
        pwd = list(filter(lambda pw: len(set(pw)) == len(pw), pwds))

        # if there is x so xy is a password for all y, x must be the last letter in the result
        # if there are x1, x2 so that x1y x2y is a password for all y, there is no solution
        first_to_second = defaultdict(list)
        ends_with = None
        for pw in (pw for pw in pwds if len(pw) == 2):
            first_to_second[pw[0]].append(pw[1])
        if len(pwds) == 50 and len(first_to_second) == 2:
            return impossible
        ends_with = find(first_to_second, lambda l: first_to_second[l] == 25)

        # same logic for 2nd letter in a pair
        second_to_first = defaultdict(list)
        starts_with = None
        for pw in (pw for pw in pwds if len(pw) == 2):
            second_to_first[pw[1]].append(pw[0])
        if len(pwds) == 50 and len(second_to_first) == 2:
            return impossible
        starts_with = find(first_to_second.values(), lambda l: len(l) == 25)

        def randomize():
            choose_from = [x for x in string.ascii_uppercase]
            if ends_with is not None:
                choose_from.remove(ends_with)

            if starts_with is not None:
                r = [starts_with]
                choose_from.remove(starts_with)
            else:
                r = [random.choice(choose_from)]
                choose_from.remove(r[0])

            while len(choose_from) > 0:
                l = random.choice([x for x in choose_from if x not in first_to_second[r[-1]]])
                r.append(l)
                choose_from.remove(l)

            return "".join(r)

        for _ in range(100):
            r = randomize()
            if test(r, pwds):
                return r

        print("Having problem with ", pwds)
        return impossible

    def test(self):
        cases = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'X', 'QQ', 'XYZ GCJ OMG LMAO JK',
                 'AB YZ NM', 'C PYTHON GO PERL RUBY JS', 'SUBDERMATOGLYPHIC UNCOPYRIGHTABLES']
        should_find = [True, False, True, True, True, False, True]
        for expected, case in zip(should_find, cases):
            output = self.solve(case.split(" "))
            if expected:
                assert len(output) == 26, case + "," + output
                assert len(set(output)) == 26, case + "," + output
            else:
                assert output == impossible


d = D()
d.test()
