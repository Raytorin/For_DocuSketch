import unittest
from main import DrawingPlots


class TestCountPath(unittest.TestCase):
    def setUp(self):
        self.drawing_plots = DrawingPlots()

    def test_count_path_limit_10(self):
        count_input_and_output = self.drawing_plots.draw_plots('tests/deviation_test.json', 10)
        self.assertEqual(len(count_input_and_output[0]), count_input_and_output[1])

    def test_count_path_limit_20(self):
        count_input_and_output = self.drawing_plots.draw_plots('tests/deviation_test.json', 20)
        self.assertEqual(len(count_input_and_output[0]), count_input_and_output[1])


if __name__ == '__main__':
    unittest.main()
