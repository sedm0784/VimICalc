import unittest

from vimicalc import calculate_line, processed_line, original_line

class CalculateLineTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
            calculate_line("2 + 3"),
            5)

    def test_divide(self):
        self.assertEqual(
            calculate_line("4 / 2"),
            2)

    def test_brackets(self):
        self.assertEqual(
            calculate_line("3 * (2 + 2)"),
            12)

    def test_multiple(self):
        self.assertEqual(
            calculate_line("The 2nd: 9 / 3"),
            3)


class ProcessLineTests(unittest.TestCase):
    def test_line(self):
        self.assertRegex(
            processed_line("4+4", 8),
            r'^4\+4\s+=> 8$')

    def test_with_result(self):
        self.assertRegex(
            processed_line("4+4 => 9", 8),
            r'^4\+4\s+=> 8$')

    def test_negative(self):
        self.assertRegex(
            processed_line("-4 => -4", -4),
            r'^-4\s+=> -4$')

    def test_missing_blank(self):
        self.assertRegex(
            processed_line("3 * 3=> 9", 9),
            r'^3 \* 3\s+=> 9$')

    def test_start_of_line(self):
        self.assertEqual(
            processed_line("=> 5", None),
            "")


class OriginalLineTests(unittest.TestCase):
    def test_original_line(self):
        self.assertEqual(original_line("4 * 4 => 16"), "4 * 4")

    def test_missing_blank(self):
        self.assertEqual(original_line("4 * 4=> 16"), "4 * 4")

    def test_nop(self):
        self.assertEqual(original_line("4 * 4"), "4 * 4")

    def test_start_of_line(self):
        self.assertEqual(original_line("=> 4"), "")
