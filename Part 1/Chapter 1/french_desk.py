import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
# Проверка кол-ва кард в колоде
print(len(deck))
# Достаем 2 первые карты
print(deck[0])
print(deck[1])
# Достаем 5 случайных карт
for i in range(5):
    print(choice(deck))
# С помощью среза извлекаем тузы (с двойки до туза 13 карт, поэтому шаг 13)
print(deck[12::13])
# С методом __getitem__ поддерживается итерирование
i = 0
for card in deck:
    if i < 5:
        print(card)
        i += 1
    else:
        break
# Так же за счет итерирования поддерживается проверка членства
print(beer_card in deck)

"""Сортировка колоды"""
# задаем порядок старшинства мастей
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


# Вспомогательная функция сортировки
def spades_high(card):
    # Получаем индекс элемента в списке с рангами карт
    rank_value = FrenchDeck.ranks.index(card.rank)
    # Возвращаем числовое значение для данной карты, вычисленное по формуле ниже
    return rank_value * len(suit_values) + suit_values[card.suit]


# Выводим список карт на основании значений присвоенных функцией
for card in sorted(deck, key=spades_high):
    print(card)
