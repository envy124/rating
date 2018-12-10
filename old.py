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

    print('W: ', win)
    print('L: ', lose)
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

# Test 3            // 1 vs 1 vs 1
w = {'id1': 1}
l = [{'id3': 1}, {'id4': 1}]
print('Test 3: 1 vs 1 vs 1')
get_score(w, l)

# Test 4            // 2 vs 1
w = {'id1': 1, 'id4': 1}
l = [{'id2': 1}]
print('Test 4: 2 vs 1 ')
get_score(w, l)

# Test 5            // 2 vs 2
w = {'id1': 1, 'id4': 1}
l = [{'id2': 1, 'id3': 1}]
print('Test 5: 2 vs 2 ')
get_score(w, l)

# Test 6            // 2 vs 3
w = {'id1': 1, 'id4': 1}
l = [{'id2': 1, 'id3': 1, 'id5': 1}]
print('Test 6: 2 vs 3 ')
get_score(w, l)

# Test 7            // 2 vs 3 vs 2
w = {'id1': 1, 'id7': 1}
l = [{'id2': 1, 'id3': 1}, {'id4': 1, 'id5': 1, 'id6': 1}]
print('Test 7: 2 vs 3 vs 2')
get_score(w, l)

# Test 8            // 1 vs 1 (пастух vs король)
w = {'id1': 1}
l = [{'id2': 10}]
print('Test 8: 1 vs 1 (пастух vs король)')
get_score(w, l)

# Test 8            // 2 vs 2 (пастух, виконт vs король, герцог)
w = {'id1': 1, 'id2': 5}
l = [{'id3': 10, 'id4': 8}]
print('Test 8: 2 vs 2 (пастух, оруженосец vs король, герцог)')
get_score(w, l)

unittest.main()
