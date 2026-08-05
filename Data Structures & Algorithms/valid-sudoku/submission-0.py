from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_index = 0

        struct = {
          'r': {},
          'c': {},
          's': {}
        }

        while row_index < 9:
            row = board[row_index]
            struct['r'][row_index] = row

            for i in range(len(row)):
                if struct['c'].get(i) is None:
                    struct['c'][i] = []
                struct['c'][i].append(row[i])

                square_index = (row_index // 3) * 3 + (i // 3)

                if struct['s'].get(i) is None:
                    struct['s'][i] = []
                struct['s'][square_index].append(row[i])

            row_index += 1

        for row in struct['r'].values():
            has_duplicates = len([item for item, count in Counter(x for x in row if x != '.').items() if count > 1]) > 0
            if has_duplicates:
                print('r')
                return False

        for row in struct['c'].values():
            has_duplicates = len([item for item, count in Counter(x for x in row if x != '.').items() if count > 1]) > 0
            if has_duplicates:
                print('c')
                return False       

        for row in struct['s'].values():
            has_duplicates = len([item for item, count in Counter(x for x in row if x != '.').items() if count > 1]) > 0
            if has_duplicates:
                print('s')
                return False 

        return True        