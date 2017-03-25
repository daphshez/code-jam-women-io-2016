input_folder = 'data'


def float_formatter(f):
    return "%.06f" % f


def exists(seq, cond):
    for x in seq:
        if cond(x):
            return True
    return False


def find(seq, cond):
    for x in seq:
        if cond(x):
            return x
    return None


class CodeJamProblem:
    def __init__(self, name, result_formatter=lambda x: '%s' % x):
        self.name = name
        self.result_formatter = result_formatter

    def generate_test_cases(self, input_file):
        with open(input_file) as f:
            for _ in range(int(next(f).strip())):
                yield self.next_test_case(f)

    # override this! though the default implementation is good if each case is a list of integers on a single line
    def next_test_case(self, f):
        return [int(x) for x in next(f).strip().split()]

    # override this!
    def solve(self, t):
        return 0

    def input_file(self, stage):
        return '%s/%s-%s.in' % (input_folder, self.name, stage)

    def output_file(self, stage):
        return '%s/%s-%s.out' % (input_folder, self.name, stage)

    def run(self, input_file, output_file):
        with open(output_file, 'w') as f:
            for i, t in enumerate(self.generate_test_cases(input_file)):
                f.write("Case #%d: %s\n" % (i + 1, self.result_formatter(self.solve(t))))

    def test(self):
        self.stage('test')
        expected = open("data/%s-test-expected.out" % self.name).read().strip()
        actual = open(self.output_file('test')).read().strip()
        if expected == actual:
            print("Test successful!")
        else:
            print("Test failed!")
            print('expected:')
            print(expected)
            print('actual:')
            print(actual)

    def stage(self, stage):
        self.run(self.input_file(stage), self.output_file(stage))

    def small(self, attempt):
        self.stage('attempt%s' % attempt)

    def large(self):
        self.stage('large')
