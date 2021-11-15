import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_loytaa_pelaajan(self):
        found_player = self.statistics.search("Semenko")
        self.assertEqual("Semenko", found_player.name)

    def test_ei_loyda_olematonta(self):
        found_player = self.statistics.search("Foxy")

        if found_player is None:
            self.assertEqual("true", "true")
        else:
            self.assertEqual("false", "true")

    def test_loytaa_joukkueen(self):
        found_team = self.statistics.team("EDM")
        self.assertEqual(3, len(found_team))
    
    def test_loytaa_kaksi_parasta(self):
        found_players = self.statistics.top_scorers(2)
        self.assertEqual("Gretzky", found_players[0].name)
        self.assertEqual("Lemieux", found_players[1].name)