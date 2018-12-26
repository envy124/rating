$STATE_VICTORY = 2;
$STATE_LOOSE = 1;

sub group_by {
    my %grouped = @_;
    for (@queries) {
        my ($k,$v) = %$_;
        push @{ $grouped{$k} }, $v;
    }
    return %grouped;
}

sub get_score {
    my ($player, $room) = @_;
    my $result = 0;
    my @loosed_teams = ();
    my @winned_team = ();

    for $x ($room->{players}) {
        if  ($x->{state} eq $STATE_VICTORY) {
            # push @winned_team $x;
        } else {
            # my $team = group_by(grep {$_->{team_id} eq x->{team_id}} $room->{players});
            # print $team;
        }
    }

    if ($player->{state} == STATE_VICTORY) {
        print 1;
    } else {
        print 2;
    }

    print $player;
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
        players        => @players,
    };
    get_score($players[0], $room);
}

main();