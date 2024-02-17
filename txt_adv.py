import bext

bext.fg("purple") #Make text purple

player = {
    "name": "",
    "instrument": "",
}

def hello():
    print("hello, world")

def intro():
    """Introduce player, gather name, choose instrument"""
    instrument = _choose_instrument()
    name = _get_name()
    invite_to_practice(name, instrument)
    
def _choose_instrument():
    """Let player choose which instrument to play"""
    instruments = ["bass", "drums", "guitar", "flute"]
    print("You're practicing your instrument in music school when a hot guy catches you play.")
    print("What do you play?")
    instrument = input("> ").lower()
    if instrument in instruments:
        # Reference these instruments specifically later in story
        # Maybe the "hot guy" specifically remarks about it?
        if instrument == "drums":
            print("That's great! We really need two drummers!")
        elif instrument == "guitar":
            print("Wowee string instruments great")
        elif instrument == "bass":
            print("Congrats you chose the right one!")
    player["instrument"] = instrument.lower()
    return instrument

def _get_name():
    """get player name"""
    print("He asks you what your name is.")
    print('''"What's your name, hotshot?"''')
    name = input("> ")
    player['name'] = name.title()
    return name

def invite_to_practice(name, instrument):
    """  """

if __name__ == "__main__":
    intro()
    print(player)