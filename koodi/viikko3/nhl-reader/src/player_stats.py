from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nation):
        players = []
        for player in self.reader.get_players():
            if player.nationality == nation:
                players.append(player)

        players.sort(key=self.goals_and_assists, reverse=True)
        return players

    def goals_and_assists(self, player):
        return player.goals + player.assists
