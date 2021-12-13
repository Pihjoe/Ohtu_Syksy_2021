from matchers import *

class QueryBuilder:
    def __init__(self, matchers = All()):
        self.matchers = matchers

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self.matchers))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self.matchers))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self.matchers))


    def build(self):
        return self.matchers