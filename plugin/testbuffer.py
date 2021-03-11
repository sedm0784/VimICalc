import unittest

from vimicalc import calculate, apply


class TotalTests(unittest.TestCase):
    def test_one(self):
        b = """2 + 2
3 * 3
4 / 4""".split('\n')
        self.assertEqual(
            list(calculate(b)),
            [4, 9, 1])

    def test_blank(self):
        b = """2 + 2
3 * 3

4 / 4""".split('\n')
        self.assertEqual(
            list(calculate(b)),
            [4, 9, None, 1])

    def test_total(self):
        b = """2 + 2
3 * 3
No sum
4 / 4

TOTAL: 14""".split('\n')
        self.assertEqual(
            list(calculate(b)),
            [4, 9, None, 1])


class ApplyTests(unittest.TestCase):
    def apply_test(self, total, before, after):
        before_lines = before.split('\n')
        after_lines = after.split('\n')
        apply(total, before_lines)

        self.assertEqual('\n'.join(before_lines),
                         '\n'.join(after_lines))

    def test_add_total(self):
        self.apply_test(
            4,
            """4 => 4""",
            """4 => 4

TOTAL: 4""")

    def test_add_blank(self):
        self.apply_test(
            4,
            """4 => 4
TOTAL: 4""",
            """4 => 4

TOTAL: 4""")

    def test_nop(self):
        self.apply_test(
            4,
            """4 => 4

TOTAL: 4""",
            """4 => 4

TOTAL: 4""")

    def test_negative_nop(self):
        self.apply_test(
            -4,
            """-4 => -4

TOTAL: -4""",
            """-4 => -4

TOTAL: -4""")

