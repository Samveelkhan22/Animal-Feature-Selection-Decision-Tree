#player.py
class Player:
    """This is an abstract class"""

    def __init__(self):
        pass

    def answer_question(self,feature):
        raise Exception("not implemented")

    def answer_animal_question(self,animal):
        raise Exception("not implemented")

class InputPlayer(Player):
    """This is a guessing game player which asks answers to questions
    from the keyboard"""

    def __init__(self):
        super().__init__()

    @classmethod
    def _input_yes_no(cls):
        """asks input to enter Y (yes) or N (no).  Returns True if yes
        is entered, and False if no is entered.

        """

        while True:
            print("Enter (y/n):")
            ans = input("Answerer: ")
            ans = ans.lower()
            if ans == "y" or ans == "yes": return True
            if ans == "n" or ans == "no": return False

    def answer_feature_question(self,feature):
        return self._input_yes_no()

    def answer_animal_question(self,animal):
        return self._input_yes_no()

class DataPlayer(Player):
    """This is a guessing game player which asks answers to questions
    based on the data"""
    
    def __init__(self,animal,animal_map):
        super().__init__()
        self.animal = animal
        self.animal_map = animal_map

    def answer_feature_question(self,feature,print_answer=True):
        answer = self.animal_map[feature]
        answer = "yes" if answer else "no"
        if print_answer: print("Answerer: %s" % answer)
        return answer == "yes"

    def answer_animal_question(self,animal,print_answer=True):
        answer = animal == self.animal
        answer = "yes" if answer else "no"
        if print_answer: print("Answerer: %s" % answer)
        return answer == "yes"
