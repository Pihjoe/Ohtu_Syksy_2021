class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score = self.p1_score + 1
        else:
            self.p2_score = self.p2_score + 1

    def get_score(self):
        score = ""

        if self.p1_score == self.p2_score:
            score = self.case_tie(score)
        elif self.p1_score >= 4 or self.p2_score >= 4:
            score = self.extra_time(score)
        else:
            score = self.time(score)
        return score

    def case_tie(self, score):
        if self.p1_score == 0:
            score = "Love-All"
        elif self.p1_score == 1:
            score = "Fifteen-All"
        elif self.p1_score == 2:
            score = "Thirty-All"
        elif self.p1_score == 3:                
            score = "Forty-All"
        else:
            score = "Deuce"
        return score

    def extra_time(self, score):
        score_dif = self.get_score_difference()
        
        if score_dif == 1:
            score = "Advantage for Player 1"
        elif score_dif == -1:
            score = "Advantage for Player 2"
        elif score_dif >= 2:
            score = "Winner, Player 1"
        else:
            score = "Winner, Player 2"
        return score
    
    def time(self, score):
        for i in range(1,3):
            if i == 1:
                temp_score = self.p1_score
            else:
                score += "-"
                temp_score = self.p2_score
            
            if temp_score == 0:
                score += "Love"
            elif temp_score == 1:
                score += "Fifteen"
            elif temp_score == 2:
                score += "Thirty"
            else:
                score += "Forty"
        return score
     
    
    def get_score_difference(self):
        return (self.p1_score - self.p2_score)