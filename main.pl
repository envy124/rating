sub get_reward_points {
    my ($player, $room) = @_;
    print $player;
}

sub main {
    my $players = (
        %{
            player_id => 1,
            rank_index => 1,
            team_id
        },
        %{
            player_id => 2,
            rank_index => 1,
        },
        %{
            player_id => 3,
            rank_index => 5,
        },
        %{
            player_id => 4,
            rank_index => 5,
        },
    )
    my $room = {
        row            => 0,
        id             => 0,
        title          => "test_room",
        password       => '',
        host_id        => 1,
        players_count  => 2,
        players        => { $player_id => { %{$h->server->data->{players}->{$player_id}} } },
    };
    get_reward_points($pla)
}