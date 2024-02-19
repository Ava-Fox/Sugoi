import sys
import bext
import textwrap as tw
from time import sleep
from troll import Troll, Gabrielle

bext.fg("purple") #Make text purple

# I'll hold information about the player here
player = {}
troll = Troll()
gabrielle = Gabrielle()

def run_game():
    """Where main game logic goes"""
    # troll.swing_blade()
    intro()
    # gabrielle.bitchy_remarks(player['name'])
    practice()

def intro():
    """Introduce player, gather name, choose instrument"""
    _choose_instrument()
    _get_name()
    _invite_to_practice()

def get_player_input():
    """Change player input color and return answer"""
    bext.fg("cyan")
    answer = input("> ")
    print()
    bext.fg("purple")
    return answer
    
def _choose_instrument():
    """Let player choose which instrument to play"""
    instruments = ["bass", "drums", "guitar", "flute"]
    prompt = '''
    You're practicing your instrument in music school when a hot guy catches you play.
'''
    print(tw.fill(prompt))
    print()
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
    print()
    print('''"What's your name, hotshot?"''')
    name = get_player_input()
    player['name'] = name.title()

def _invite_to_practice():
    """See if player wants to continue game or not"""
    prompt = f'''"Well I like your stuff, {player['name']}. What do you say about coming over to my band's next practice to jam?"\n'''
    prompt2 = '''
    You realize who you're talking to. Reality shifts and everything comes into focus as you find yourself conversing with the one and only Griffen R., the hottest, most talented, most popular guitarist in the school's most beloved band.
    '''
    print(tw.fill(prompt))
    print(tw.fill(prompt2))
    print("\nWould you like to go? (Y/N)")
    while True:
        answer = get_player_input().upper()
        options = ['Y','N']
        if answer in options:
            break
    if answer == 'N':
        prompt = '''
    You realize you're too much of a loser to be cool and you drop all of your stuff in your rush to escape, embarrassing yourself thoroughly.
        '''
        # Pause for dramatic effect
        sleep(1)
        print(tw.fill(prompt))  
        sys.exit()

def practice():
    """Where practice sequence goes"""
    _introductions()
    _compare_inst()
    options = ['1', '2']
    p = '''Will you...
    1. Consider your surroundings?
    2. Focus on conversation?
    '''
    print(p)
    choice = player_choice(options)
    if choice == '1':
        _survey_room()
    else:
        ...

    # _survey_room()

def _introductions():
    """..."""
    options = ['1', '2']
    print("~~~ The day arrives and you find yourself approaching Griffin’s house. ~~~~~\n")
    prompt = "If you were a pirate you would certainly be shivering your timbers, because as you walk through the front door and enter the foyer you are greeted by a cluster of very beautiful people."
    print(tw.fill(prompt))
    prompt = '''Will you...
    1. Introduce yourself?
    2. Be introduced?
'''
    print(prompt)
    while True:
        answer = get_player_input()
        if answer in options:
            break
    if answer == '1':
        p = f'''You tell everyone what your name is. When you’re finished, Griffin includes, “I told {player['name']} she could come to practice today, heard her in the practice rooms - she's pretty good.” 
Just then, a pair of finely manicured hands flash into your vision, and then you see who they belong to.  'Hi', he says, 'I’m Andy. I play drums, what about you?”
'''
    else:
        p = f'''There’s an awkward silence as everyone turns to look at you. After a beat Griffin says, “Hi {player['name']}, everyone this is {player['name']}. I told her she could come to practice today. I caught her playing in the practice rooms, she’s pretty good.” Just then, a pair of finely manicured hands flash into your vision, and then you see who they belong to.  'Hi', he says, 'I’m Andy. I play drums, what about you?”
        '''
    
    print(tw.fill(p))

    p = '''
    1. Tell him what you play
    2. Answer his question
    '''
    print(p)
    get_player_input()

def _compare_inst():
    """..."""
    i = player['instrument']
    inst = ["drums", "guitar", "bass", "flute"]
    if i in inst:
        if i == inst[0]:
            p = '''
When you tell him you play drums too, the brightness extinguishes from his eyes. He looks over to Griffin and asks, “You invited another drummer over? What gives? Now I gotta go grab the second drum set from storage!” This exchange gives you an opportunity to survey the room.
'''
        elif i == inst[1]:
            p = '''
Calling from across the room, “We definitely don’t need three guitarists in this band, what were you thinking inviting her over?” This exchange gives you an opportunity to survey the room.
'''
        elif i == inst[2]:
            p = '''
Someone remarks, “Two bassists? Awkward. I guess we could make it work…” Andy calls back, “Be nice, everyone knows bass doesn’t even matter anyways. Having two would at least make it more noticeable we even have one in the band.” This exchange gives you an opportunity to survey the room.
'''
        elif i == inst[3]:
            p = '''
“Nice, a flutist! We need one for our next album!” He smiles, stealing your breath away, because he's left you no choice but to look at his magnificent face. Delicate, faded freckles speckle his cheeks, shadowed by brilliant blades of bright red hair. Proportions nothing short of perfect; this dude certainly is symmetrical.
'''  
    print(tw.fill(p))
       
def _survey_room():
    """..."""
    p = '''
  "House" is a little too back-alley of a word to describe the place
you find yourself in. Lathered in deep red carpetry, a tone that
complements Andy's hair, and milky marble walls with deep green velvety
furniture, you're scared even breathing will soil the place's
solemnity. 
'''
    print(tw.fill(p))
    p = '''
1. Continue looking.
2. Back to conversation.
'''
    print(p)
    options = ['1', '2']
    choice = player_choice(options)
    if choice == '1':
        p = '''
1. Who's in the chair?
2. Who's at the window?
''' 
        print(p)
        choice = player_choice(options)
        if choice == '1':
            p = '''
Lounging on one of the Brunswick armchairs sits Gabrielle LastNameHere, lazily cleaning her glasses. She looks up and gives you a half-nod. A curly blonde lock of her hair falls to slightly obstruct her vision; she blows it away nonchalantly and refocuses on her spectacles. 
'''
        else:
            p = '''
The window is half obscured by a finely chiseled form, surveying the view. It may just be backlighting, but you could swear you could make out the outline of every single muscle through his shirt. As he turns towards the commotion, you understand why his figure was so exquisitely defined - because he actually wasn’t wearing one at all.  
'''
        print(tw.fill(p))
    else:
        print("BACK TO CONVO")

def player_choice(options):
    while True:
        answer = get_player_input()
        if answer in options:
            break
    return answer


if __name__ == "__main__":
    run_game()