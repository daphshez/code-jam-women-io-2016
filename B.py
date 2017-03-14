"""
The owner of a prestigious ballroom has painted a beautiful circular clock on the dance floor, and a group of 
D dancers numbered 1 through D are about to literally "dance around the clock". They are standing in a circle, 
with dancer 1 at the 12:00 position of the circle and the other dancers going clockwise around the circle in 
increasing numerical order. The number of dancers is even.

The dance will go on for N turns. On the i-th turn (counting starting from 1), the following will happen:

If i is odd, then the dancer currently at the 12:00 position will swap positions with the next dancer in 
clockwise order. Then, going past those two, the next pair of dancers in clockwise order will swap positions, 
and so on, all the way around the ring clockwise, until all dancers have participated in exactly one swap.
If i is even, then the dancer currently at the 12:00 position will swap positions with the next dancer 
in counterclockwise order. Then, going past those two, the next pair of dancers in counterclockwise order 
will swap positions, and so on, all the way around the ring counterclockwise, until all dancers have 
participated in a swap.

For example, this diagram shows the initial state and two turns of a dance with eight people.


Which two dancers will be next to dancer number K when the dance is over?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one 
line with three integers D, K, and N: the total number of dancers, the number of one of the dancers, and 
the number of turns the dance will go on for.

Output

For each test case, output one line containing Case #x: y z, where:

x is the test case number (starting from 1).
y is the number of the dancer who will be standing to dancer number K's left (that is, one step away in 
clockwise order) when the dance is over.
z is the number of the dancer who will be standing to dancer number K's right (that is, one step away in 
counterclockwise order) when the dance is over.
Limits

1 ≤ T ≤ 100.
D is even.
1 ≤ K ≤ D.
Small dataset

4 ≤ D ≤ 10.
1 ≤ N ≤ 10.
Large dataset

4 ≤ D ≤ 108.
1 ≤ N ≤ 108.

Input
3
8 3 1
8 4 2
4 1 8

Output
Case #1: 6 4
Case #2: 1 7
Case #3: 2 4


"""

from collections import Counter

from CodeJam import CodeJamProblem


class B(CodeJamProblem):
    def __init__(self):
        super().__init__('B')

    def generate_test_cases(self, input_file):
        pass

    def solve(self, t):
        pass



a = A()
a.test()
