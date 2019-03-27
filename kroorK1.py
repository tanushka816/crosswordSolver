import sys
import argparse
from parserfail import CrossParser
import logic


def create_parser():
    parser = argparse.ArgumentParser(prog="КРОССВОРД!",
                                    description="""Программа решения кроссворда \n"
                                    На вход в геометрии водаются строки вида '***|*|*'\n
                                    без каких-либо знаков, кроме \n
                                    "+" для обозначения первой буквы перемекающихся слов, \n
                                    "|" для первой буквы слова по вертикали, \n
                                    "-" для первой буквы слова по горизонтали, \n
                                    "." для любой другой буквы, \n
                                    "*" для пустой клеточки""")
    parser.add_argument('--filename',
                        '-f',
                        type=str,
                        help="Расширения файлов код.py геометрия.txt слова.txt")
    parser.add_argument('--directory',
                        '-d',
                        help="Директория в которой хранятся файлы")
    parser.add_argument('--geometry',
                        '-g',
                        help="""На вход в файле геометрия подаются строки вида '***|*|*', \n
                        где '+' первая буква пересекающихся слов \n
                        "|" первая буква слова по вертикали \n
                        "-" по горизонтали \n
                        "." просто буква \n
                        "*" ничего""")
    return parser


def main():
    if sys.argv[1] == '--help':
        prs = create_parser()
        args = prs.parse_args()
    else:
        parser2 = CrossParser()
        parser2.know_geometry(sys.argv[1])
        parser2.know_words(sys.argv[2])
        dictionary_hor = parser2.words_place_hor()
        dictionary_vert = parser2.words_place_vert()
        parser2.form_word_place(dictionary_vert, dictionary_hor)
        parser2.new_view()

    logical = logic.Logic(parser2)
    mat = logical.fill()

    if mat is not None:
        for line in mat:
            print("".join(line))
    else:
        print("Not solvable")

    with open('ans.txt', 'w') as f:
        f.write(logical.mat_str)
    '''with open ('ans.txt', 'w') as f:
        for line in mat:
            f.write("{}".format(line))'''



if __name__ == "__main__":
    main()