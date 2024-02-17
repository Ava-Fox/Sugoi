import sys
import bext
import textwrap as tw
from time import sleep

bext.fg("purple") #Make text purple

# I'll hold information about the player here
player = {}

# Hello world for good luck
def hello():
    print("hello, world")

def intro():
    """Introduce player, gather name, choose instrument"""
    _choose_instrument()
    _get_name()
    _invite_to_practice()

def get_player_input():
    bext.fg("cyan")
    answer = input("> ")
    bext.fg("purple")
    return answer
    
def _choose_instrument():
    """Let player choose which instrument to play"""
    instruments = ["bass", "drums", "guitar", "flute"]
    print("You're practicing your instrument in music school when a hot guy catches you play.")
    print("What do you play?")
    instrument = get_player_input().lower()
    if instrument in instruments:
        # Reference these instruments specifically later in story
        # Maybe the "hot guy" specifically remarks about it?
        if instrument == "drums":
            print("That's great! We really need two drummers!")
        elif instrument == "guitar":
            print("Wowee string instruments great")
        elif instrument == "bass":
            print("Congrats you chose the right one!")
        else:
            print("I always wanted a flute in my rock band")
    else:
        # Generic answer for other instruments
        print(f"What lovely tunes you play with your {instrument}")
    player["instrument"] = instrument.lower()

def _get_name():
    """get player name"""
    print("He asks you what your name is.")
    print('''"What's your name, hotshot?"''')
    name = get_player_input()
    player['name'] = name.title()

def _invite_to_practice():
    """  """
    prompt = f"Well, I like your stuff {player['name']}. What do you say about coming over to my band's next practice to jam?"
    prompt2 = '''
    You realize who you're talking to. Reality shifts and everything comes into focus as you find yourself conversing with the one and only Griffen R., the hottest, most talented, most popular guitarist in the school's most beloved band.
'''
    print(tw.fill(prompt))
    print(tw.fill(prompt2))
    print("Would you like to go? Y/N")
    while True:
        answer = get_player_input().upper()
        options = ['Y','N']
        if answer in options:
            break
    if answer == 'N':
        prompt = '''
        You realize you're too much of a loser to be cool and you drop all of your stuff in your rush to escape, embarrasing yourself thoroughly.
        '''
        sleep(2)
        print(tw.fill(prompt))  
        sys.exit()


if __name__ == "__main__":
    intro()
    print(player)