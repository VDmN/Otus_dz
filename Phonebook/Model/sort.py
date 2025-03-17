class SortDict:

    @staticmethod
    def get_sorted_dict(s):
        '''Сортировка словаря по имени value[0] и раздача ключей по порядку следования
        '''
        s = sorted(s.values(), key=lambda k: k[0].lower())
        return {j + 1: s[j] for j in range(len(s))}
