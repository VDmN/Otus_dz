import random

def list_random(xxx):   # Перемешивание спика и каждого его элемента.
    for j in range(len(xxx)):
        xxx[j] = random.sample(xxx[j], len(xxx[j]))
    random.shuffle(xxx)
    return xxx


spis_0 = [
        'ue7Ятatc0OKб',
        'DЪукТЫjsчГлvwю',
        'А5XPхсжdNФшЬBъ',
        'Нx2GRVЖzБиД9',
        'вфЦQ|rЕВiЩ4цС',
        'ClqHokIЮКИ',
        'm+J&эh,Ё3ЗО',
        'E6YыШ1МПьL',
        'S.bёгЛWЙдерйf',
        'ZУРMнnзyAапмU',
        'яЭЧ8FоХgTpщ'
    ]
