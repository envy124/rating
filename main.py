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


def get_reward_points_count(player, room):
    foes = [x for x in room.players if x.team_id != player.team_id]
    teammates = [x for x in room.players if x.team_id == player.team_id]

    if len(foes) == 0 or len(teammates) == 0:
        return 0

    foes_rank = sum([x.rank_index for x in foes]) / len(foes)
    teammates_rank = sum([x.rank_index for x in teammates]) / len(teammates)

    if player.state == STATE_VICTORY:
        points = sum(
            [SCORE_TABLE[(x.rank_index + player.rank_index * 9) * 2]
             for x in room.players])
        return max(points, 5)
    else:
        return SCORE_TABLE[(foes_rank * 9 + teammates_rank) * 2 + 1]


def main():
    room = Room()
    room.add_player(Player(0, STATE_VICTORY, 1))
    room.add_player(Player(9, STATE_LOOSE, 2))
    print(get_reward_points_count(room.players[0], room))


main()
