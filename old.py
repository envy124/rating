import unittest

# {id: Rank} - один игрок или одна команда из одного игрока
# {id: Rank, id: Rank} - одна команда из двух игроков
# [{},{}] - две разные команды
# w - словарь из победителей, содержащий id игрока-победителя и его Ранг
# l - массив из проигравших, содержащий словарь(и) из id игрока-проигравшего и его Ранга
# win - словарь, содержащий id игрока и очки для начисления в его статистик
# lose - словарь, содержащий id игрока и очки для списания из его статистики
# Ранг пастуха начинается с 1, а не с 0 !


def get_score(w, l):
    win = {}
    lose = {}
    for key, val in w.items():
        i = 0
        b = 0
        win[key] = 0
        for i in l:
            a = 0
            for v in i.values():
                a += 10 + (v - val)
            b = round(a / len(w))

            if len(l) > 1:
                win[key] += abs(win[key] - b) if win[key] < b else 0
            else:
                win[key] += b

    for i in l:
        for key, val in i.items():
            a = 0
            for v in w.values():
                a += 10 - (v - val)
            lose[key] = round(a / len(w))

    return {'W': win, 'L': lose}


class RatingTestCase(unittest.TestCase):
    def test_1x1_equal(self):
        w = {'id1': 1}
        l = [{'id2': 1}]
        result = get_score(w, l)
        self.assertEqual(result['W']['id1'], 10)
        self.assertEqual(result['L']['id2'], 10)

    def test_1x2_equal(self):
        w = {'id1': 1}
        l = [{'id2': 1, 'id3': 1}]
        result = get_score(w, l)
        self.assertEqual(result['W']['id1'], 20)
        self.assertEqual(result['L']['id2'], 10)
        self.assertEqual(result['L']['id3'], 10)

    def test_1x1x1_equal(self):
        w = {'id1': 1}
        l = [{'id2': 1}, {'id3': 1}]
        result = get_score(w, l)
        self.assertEqual(result['W']['id1'], 10)
        self.assertEqual(result['L']['id2'], 10)
        self.assertEqual(result['L']['id3'], 10)

    def test_2x1_equal(self):
        w = {'id1': 1, 'id2': 1}
        l = [{'id3': 1}]
        result = get_score(w, l)
        self.assertEqual(result['W']['id1'], 5)
        self.assertEqual(result['W']['id2'], 5)
        self.assertEqual(result['L']['id3'], 10)

    def test_2x2_equal(self):
        w = {'id1': 1, 'id2': 1}
        l = [{'id3': 1, 'id4': 1}]
        result = get_score(w, l)
        self.assertEqual(result['W']['id1'], 10)
        self.assertEqual(result['W']['id2'], 10)
        self.assertEqual(result['L']['id3'], 10)
        self.assertEqual(result['L']['id4'], 10)

    def test_2x3_equal(self):
        w = {'id1': 1, 'id2': 1}
        l = [{'id3': 1, 'id4': 1, 'id5': 1}]
        result = get_score(w, l)
        self.assertEqual(result['W']['id1'], 15)
        self.assertEqual(result['W']['id2'], 15)
        self.assertEqual(result['L']['id3'], 10)
        self.assertEqual(result['L']['id4'], 10)
        self.assertEqual(result['L']['id5'], 10)

    def test_2x3x2_equal(self):
        w = {'id1': 1, 'id2': 1}
        l = [{'id3': 1, 'id4': 1}, {'id5': 1, 'id6': 1, 'id7': 1}]
        result = get_score(w, l)
        self.assertEqual(result['W']['id1'], 15)
        self.assertEqual(result['W']['id2'], 15)
        self.assertEqual(result['L']['id3'], 10)
        self.assertEqual(result['L']['id4'], 10)
        self.assertEqual(result['L']['id5'], 10)
        self.assertEqual(result['L']['id6'], 10)
        self.assertEqual(result['L']['id7'], 10)

    def test_1x1_non_equal(self):
        w = {'id1': 1}
        l = [{'id2': 10}]
        result = get_score(w, l)
        self.assertEqual(result['W']['id1'], 19)
        self.assertEqual(result['L']['id2'], 19)

    def test_2x2_non_equal(self):
        w = {'id1': 1, 'id2': 5}
        l = [{'id3': 10, 'id4': 8}]
        result = get_score(w, l)
        self.assertEqual(result['W']['id1'], 18)
        self.assertEqual(result['W']['id2'], 14)
        self.assertEqual(result['L']['id3'], 17)
        self.assertEqual(result['L']['id4'], 15)


unittest.main()
