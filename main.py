import unittest
from collections import defaultdict

SCORE_TABLE = [
    5, -2,	10, -2,	20, -2,	30, -2,	40, -2,	50, -2,	60, -2,	70, -2,	80, -2,
    5, -2,	5, -2,	10, -2,	20, -2,	30, -2,	40, -2,	50, -2,	60, -2,	70, -2,
    5, -2,	5, -2,	5, -2,	10, -2,	20, -2,	30, -2,	40, -2,	50, -2,	60, -2,
    5, -2,	5, -2,	5, -2,	5, -2,	10, -2,	20, -2,	30, -2,	40, -2,	50, -2,
    5, -4,	5, -2,	5, -2,	5, -2,	5, -2,	10, -2,	20, -2,	30, -2,	40, -2,
    5, -6,	5, -4,	5, -2,	5, -2,	5, -2,	5, -2,	10, -2,	20, -2,	30, -2,
    5, -8,	5, -6,	5, -4,	5, -2,	5, -2,	5, -2,	5, -2,	10, -2,	20, -2,
    5, -16,	5, -8,	5, -6,	5, -4,	5, -2,	5, -2,	5, -2,	5, -2,	10, -2,
    5, -32,	5, -16,	5, -8,	5, -6,	5, -4,	5, -2,	5, -2,	5, -2,	5, -2
]

LINE_LENGTH = 18
ROW_LENGTH = int(len(SCORE_TABLE) / LINE_LENGTH)

STATE_VICTORY = 2
STATE_LOOSE = 1
STATE_DISCONNECT = 5

RANKS = [
    'Shepherd',
    'Esquire',
    'Knight',
    'Baron',
    'Viscount',
    'Earl',
    'Marquis',
    'Duke',
    'Prince',
    'King',
]

MAX_RANK = 10


class Player:
    def __init__(self, rank_index, state, team_id):
        self.rank_index = rank_index
        self.rank = RANKS[rank_index]
        self.state = state
        self.team_id = team_id


class Room:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)


def group_players_by_team(players):
    teams = defaultdict(list)
    [teams[x.team_id].append(x) for x in players]
    return [team for key, team in teams.items()]


def get_score(player, room):
    result = 0
    loosed_teams = group_players_by_team(
        [x for x in room.players if x.state != STATE_VICTORY])
    winned_team = [x for x in room.players if x.state == STATE_VICTORY]

    if player.state == STATE_VICTORY:
        for team in loosed_teams:
            points = round(sum([MAX_RANK + (x.rank_index - player.rank_index)
                                for x in team]) / len(winned_team))
            result += abs(result - points)
    else:
        result = round(sum([MAX_RANK - (x.rank_index - player.rank_index)
                            for x in winned_team]) / len(winned_team))
    return result


def main():
    room = Room()
    room.add_player(Player(0, STATE_VICTORY, 1))
    room.add_player(Player(9, STATE_LOOSE, 2))
    print(get_score(room.players[0], room))


class RatingTestCase(unittest.TestCase):
    def test_1x1_equal(self):
        room = Room()
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_LOOSE, 2))

        self.assertEqual(get_score(room.players[0], room), 10)
        self.assertEqual(get_score(room.players[1], room), 10)

    def test_1x2_equal(self):
        room = Room()
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_LOOSE, 2))
        room.add_player(Player(0, STATE_LOOSE, 2))

        self.assertEqual(get_score(room.players[0], room), 20)
        self.assertEqual(get_score(room.players[1], room), 10)
        self.assertEqual(get_score(room.players[2], room), 10)

    def test_1x1x1_equal(self):
        room = Room()
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_LOOSE, 2))
        room.add_player(Player(0, STATE_LOOSE, 3))

        self.assertEqual(get_score(room.players[0], room), 10)
        self.assertEqual(get_score(room.players[1], room), 10)
        self.assertEqual(get_score(room.players[2], room), 10)

    def test_2x1_equal(self):
        room = Room()
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_LOOSE, 2))

        self.assertEqual(get_score(room.players[0], room), 5)
        self.assertEqual(get_score(room.players[1], room), 5)
        self.assertEqual(get_score(room.players[2], room), 10)

    def test_2x2_equal(self):
        room = Room()
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_LOOSE, 2))
        room.add_player(Player(0, STATE_LOOSE, 2))

        self.assertEqual(get_score(room.players[0], room), 10)
        self.assertEqual(get_score(room.players[1], room), 10)
        self.assertEqual(get_score(room.players[2], room), 10)
        self.assertEqual(get_score(room.players[3], room), 10)

    def test_2x3_equal(self):
        room = Room()
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_LOOSE, 2))
        room.add_player(Player(0, STATE_LOOSE, 2))
        room.add_player(Player(0, STATE_LOOSE, 2))

        self.assertEqual(get_score(room.players[0], room), 15)
        self.assertEqual(get_score(room.players[1], room), 15)
        self.assertEqual(get_score(room.players[2], room), 10)
        self.assertEqual(get_score(room.players[3], room), 10)
        self.assertEqual(get_score(room.players[4], room), 10)

    def test_2x3x2_equal(self):
        room = Room()
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(0, STATE_LOOSE, 2))
        room.add_player(Player(0, STATE_LOOSE, 2))
        room.add_player(Player(0, STATE_LOOSE, 3))
        room.add_player(Player(0, STATE_LOOSE, 3))
        room.add_player(Player(0, STATE_LOOSE, 3))

        self.assertEqual(get_score(room.players[0], room), 15)
        self.assertEqual(get_score(room.players[1], room), 15)
        self.assertEqual(get_score(room.players[2], room), 10)
        self.assertEqual(get_score(room.players[3], room), 10)
        self.assertEqual(get_score(room.players[4], room), 10)
        self.assertEqual(get_score(room.players[5], room), 10)
        self.assertEqual(get_score(room.players[6], room), 10)

    def test_1x1_non_equal(self):
        room = Room()
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(9, STATE_LOOSE, 2))

        self.assertEqual(get_score(room.players[0], room), 19)
        self.assertEqual(get_score(room.players[1], room), 19)

    def test_2x2_non_equal(self):
        room = Room()
        room.add_player(Player(0, STATE_VICTORY, 1))
        room.add_player(Player(4, STATE_VICTORY, 1))
        room.add_player(Player(9, STATE_LOOSE, 2))
        room.add_player(Player(7, STATE_LOOSE, 2))

        self.assertEqual(get_score(room.players[0], room), 18)
        self.assertEqual(get_score(room.players[1], room), 14)
        self.assertEqual(get_score(room.players[2], room), 17)
        self.assertEqual(get_score(room.players[3], room), 15)


unittest.main()
