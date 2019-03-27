import unittest
import kroorK1
from parserfail import CrossParser
import logic
import sys
import coverage


def fill_source(geometry_name, words_name):
    parser = CrossParser()
    parser.know_geometry(geometry_name)
    parser.know_words(words_name)
    dictionary_hor = parser.words_place_hor()
    dictionary_vert = parser.words_place_vert()
    parser.form_word_place(dictionary_vert, dictionary_hor)
    parser.new_view()

    logical_source = logic.Logic(parser)
    mat_source = logical_source.fill()
    if mat_source is not None:
        return str(mat_source)
    else:
        return ''


def get_information(file_name):
    with open(file_name, mode='r', encoding='cp1251') as f:
        final_str = f.read()
    return final_str


class TestGo(unittest.TestCase):

    def test_everything_is_okay(self):
        self.assertEqual(fill_source("geo2.txt", "wr2.txt"), get_information("test_a2.txt"))

    def test_no_variants(self):
        self.assertEqual(fill_source("geo5.txt", "wr2.txt"), get_information("test_f.txt"))

    def two_word_one_line(self):
        self.assertEqual(fill_source("geo6.txt", "wr6.txt"), get_information("test_a6.txt"))

    def test_big_crossword(self):
        self.assertEqual(fill_source("geometry1.txt", "words1.txt"), get_information("test_a1.txt"))


if __name__ == "__main__":
    unittest.main()