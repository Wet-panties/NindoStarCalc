def definestage(stage):
    rankstage = {'A': 5, 'A+': 9, 'S-': 12, 'S': 13, 'S+': 14}
    for i in rankstage:
        if stage == i:
            stage = rankstage[i]
            return stage
        else:
            pass


def checkelement(element):
    elements = {'вода': 'aqua', 'огонь': 'fire', 'воздух': 'wind', 'инь': 'yin', 'янь': 'yang', 'любая': 'anything'}
    if element == 'ветер':
        element = 'воздух'
    for i in elements:
        if element == i:
            element = elements[i]
            return element
        else:
            pass


rank: str = input('Какого ранга персонаж? (A - S+): ').upper()
elle: str = input('Какая стихия?: ').upper()
# element: str = input('Какой элемент? (A - S+): ')
charstage = definestage(rank)
charelement = checkelement(elle)
print(f'Maximum stars: {charstage}')