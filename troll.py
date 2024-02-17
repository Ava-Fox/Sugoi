from random import choice
class Troll:
    """ I dunno I had an idea """
    def swing_blade(self):
        print("Troll swings blade")

class Gabrielle:
    def bitchy_remarks(self, name="bitch"):
        """Randomize bitchy remarks Gabs can say"""
        remarks = [
            "Yeah, whatever.",
            "Ugh",
            "Fuck off.",
            f"{name}, you're so lame.",
        ]
        print(choice(remarks))