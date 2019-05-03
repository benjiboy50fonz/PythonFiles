class ScoreCommands():

    """
This file works after a LOT of trial and error. It is not possible to get rid of the 'score' parameter.
I tried numerous times and have failed all of them. TODO: Try to find a way!
STATUS: WORKING
    """
    #import actioncommandgroups

    @classmethod
    def IncreaseScore(self, score, value):
        try:
            score += int(value)
        except (NameError, AttributeError):
            print('Error Score Commands')
        return score

    @classmethod
    def PrintScore(self, score):
        print(str(score))

    @classmethod
    def IncreaseScoreMega(self, score):
        score = self.IncreaseScore(score, 500)
        return score

    @classmethod
    def IncreaseScoreLarge(self, score):
        score = self.IncreaseScore(score, 200)
        return score

    @classmethod
    def IncreaseScoreStandard(self, score):
        score = self.IncreaseScore(score, 150)
        return score

    @classmethod
    def IncreaseScoreSmall(self, score):
        score = self.IncreaseScore(score, 50)
        return score



