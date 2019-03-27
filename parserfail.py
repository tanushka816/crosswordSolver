from collections import defaultdict


class CrossParser:
    def __init__(self):  # Для всего кода: 0 - вертикаль, 1 - горизонталь
        self.geometry = []  # лист таплов [('*', '|', '*'), ('-', '.', '.'), ('*', '.', '*')]
        self.source_word = []  # исходные слова
        self.use_symbols = ('+', '|', '-', '.', '*')
        self.place_in_g = {0: {}, 1: {}}
        self.stat_geometry = []

    def know_words(self, file):
        """
        достаёт слова
        """
        with open(file, mode='r', encoding='cp1251') as f:
            raw_str = f.read()
            self.source_word = raw_str.replace(' ', '').split(',')

    def know_geometry(self, file):
        """
        достаёт геометрию
        """
        with open(file, mode='r', encoding='cp1251') as f:
            for l in f:
                raw_str = l.replace("\n", "")  # из-за переноса строки
                raw_tuple = tuple(raw_str)
                for ll in raw_tuple:
                    if ll not in self.use_symbols:
                        raise Exception("Please, use only known symbols")
                self.geometry.append(raw_tuple)

    def words_place_hor(self, vert=False):
        place_dict = {}
        raw_list = []
        k = 0
        i_m = len(self.geometry)
        for i in range(i_m):
            for j in range(len(self.geometry[i])):
                if (not self.geometry[i][j] == "*") and (
                        j < len(self.geometry[i]) - 1 and not self.geometry[i][j + 1] == "*"):
                    raw_list.append((i, j))
                    k += 1
                else:
                    if not len(raw_list) == 0:
                        if vert:
                            place_dict.setdefault(k + 1, []).append(raw_list[0][::-1])
                        else:
                            place_dict.setdefault(k + 1, []).append(raw_list[0])
                        raw_list = []
                        k = 0
        return place_dict

    def words_place_vert(self):
        self.geometry = list(zip(*self.geometry))
        result = self.words_place_hor(True)
        self.geometry = list(zip(*self.geometry))
        return result

    def form_word_place(self, vert_d, gor_d):
        """
        формирует полный словарь для расположений слов с их длинами для new_view
        """
        self.place_in_g[0] = vert_d  # {0:{3:(1,0), 4:(0,3), 3:(0,5)}, 1:{7:(1,0), 5:(3,0)}}
        self.place_in_g[1] = gor_d

    def new_view(self):
        for k in self.place_in_g:
            for kk in self.place_in_g[k]:
                for kkk in self.place_in_g[k][kk]:
                    self.stat_geometry.append((kkk, k, kk,))