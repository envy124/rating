use Math::Round;
use List::Util qw(
    reduce sum
);

$STATE_VICTORY = 2;
$STATE_LOOSE = 1;
$MAX_RANK = 10;

sub group_by_team {
    my (@players) = @_;
    my %grouped_hash = {};
    for (@players) {
        my $player = $_;
        my $team_id = $_->{team_id};
        push @{ $grouped_hash{$team_id} }, $player;
    }
    return %grouped_hash;
}

sub get_score {
    my ($player, $room) = @_;
    my $result = 0;
    my @loosed_players = ();
    my @winned_team = ();

    for my $x (values $room->{players}) {
        if  ($x->{state} eq $STATE_VICTORY) {
            push @winned_team, $x;
        } else {
            push @loosed_players, $x;
        }
    }

    my @foes = grep {$_->{team_id} ne $player->{team_id}} @loosed_players;
    my @loosed_teams = group_by_team(@foes);
    for my $team (@loosed_teams) {
        my $team_rating_sum = sum map {$MAX_RANK + ($_->{rank_index} - $player->{rank_index})} $team;
        my $team_rating = round $team_rating_sum / length @winned_team;
        $result += $team_rating;
    }

    if ($player->{state} == $STATE_VICTORY) {
        print 1;
    } else {
        print 2;
    }
    return $score;
}

sub main {
    my @players = (
        {
            player_id => 1,
            rank_index => 1,
            team_id => 1,
            state => $STATE_VICTORY,
        },
        {
            player_id => 2,
            rank_index => 1,
            team_id => 2,
            state => $STATE_LOOSE,
        },
        {
            player_id => 3,
            rank_index => 5,
            team_id => 3,
            state => $STATE_LOOSE,
        },
        {
            player_id => 4,
            rank_index => 5,
            team_id => 3,
            state => $STATE_LOOSE,
        },
    );
    my $room = {
        row            => 0,
        id             => 0,
        title          => "test_room",
        password       => '',
        host_id        => 1,
        players_count  => 2,
        players        => \@players,
    };
    get_score($players[0], $room);
}

main();