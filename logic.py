class Logic:

    def __init__(self, parser_argument):
        self.parser = parser_argument
        self.words = parser_argument.stat_geometry
        self.l_words = parser_argument.source_word
        self.m = len(parser_argument.geometry)
        self.n = len(parser_argument.geometry[0])
        self.mat_str = ""

    def get_next_word(self, word_length, num_current_word):
        """
        возвращает слово-кандидат и его позицию в words
        """

        for i in range(num_current_word+1, len(self.l_words)):
            if len(self.l_words[i]) == word_length:
                return(i, self.l_words[i])
     
    def fill(self):
        """
        заполнение
        в stack[] будут координаты слов и направление
        в (х, у) - координаты начала
        в vector - направление: 0 - вертикаль
        если на первом шаге кроссворд нельзя продолжить - возвр. None
        если не на первом - пробуем заполнить чем-нибудь другим
        """

        mat = [['_' for i in range(self.n)] for i in range(self.m)]
        stack = []
        i = 0
        num_current_word = -1
        while i < len(self.words):
            (x, y) = self.words[i][0]
            vector = self.words[i][1]
            word_length = self.words[i][2]
            next_word = self.get_next_word(word_length, num_current_word)
            if next_word is None:
                if i == 0:
                    return None
                changed_pos, num_current_word = stack.pop()
                for p in changed_pos:
                    mat[p[0]][p[1]] = '_'
                i -= 1
                continue
            num_current_word, string = next_word
            changed_pos = []
            if vector == 1:
                for j in range(word_length):
                    if mat[x][y+j] == '_': # если клетка кроссворда не заполнена
                        mat[x][y+j] = string[j] # пишем туда следующую букву
                        changed_pos.append((x, y+j)) # запоминаем измененную позицию
                    elif mat[x][y+j] != string[j]: # если заполнена и буква там не та
                        for p in changed_pos:
                            mat[p[0]][p[1]] = '_' # стираем все измененные буквы
                        break
                if j == word_length-1: # если вдруг смогли дописать слово до конца
                    stack.append((changed_pos, num_current_word))
                    i += 1
                    num_current_word = -1
            else:
                for j in range(word_length):
                    if mat[x+j][y] == '_':
                        mat[x+j][y] = string[j]
                        changed_pos.append((x+j, y))
                    elif mat[x+j][y] != string[j]:
                        for p in changed_pos:
                            mat[p[0]][p[1]] = '_'
                        break
                if j == word_length-1:
                    stack.append((changed_pos, num_current_word))
                    i += 1
                    num_current_word = -1
        self.mat_str = str(mat)
        return mat