import textwrap # Format text
import bext # Change terminal colors
import story_script as ss 

bext.fg("purple")

#Prompt user if wanna play/what your name is 
print(textwrap.fill(ss.intro))
name = input('''\n"What's your name, hotshot?"\n> ''').title()

invite_to_practice = f'''
    "I like your stuff, {name.title()}. What do you think about coming over to my band's next practice to jam?"
    ''' #An explination of what happens next, he invites you over to meet the band, you choose yes or no

print(textwrap.dedent(invite_to_practice))
print(textwrap.fill(ss.realization))
    #starting game???

prompt = "\n> Do you wanna go? (yes/no) "
answer = input(prompt)

if answer == "no" or answer == "n":
   #End game
    back_out = '''
        \nYou realize you're too much of a loser to be cool and you drop all of your stuff in your rush to escape, embarrasing yourself thoroughly.
        '''
    print(textwrap.dedent(back_out))

else:
    #He takes you to band practice
    band_practice = "\nA section explaining what band practice is like and meeting secondary characters and explaining how hot they are"
    print(textwrap.fill(ss.band_practice))

    instrument = input("\n> What do you play? ")
    
    # Section that's too long: 
    andy_meet = f'''
    'Ah, the {instrument}! What lovely tunes the {instrument} produces!', he says while staring directly into your soul. 'I don't believe we've met before, I'm Andy." You've definitely met before, but you tell him your name anyways.
'''
    print(textwrap.fill(andy_meet))

    print(textwrap.fill(ss.andy_description))

    griffin_buts_in = f'''
    'I told {name} she could come to practice today, heard her in the practice rooms - she's pretty good.' Griffin says, giving you a chance to take a carefully measured inhale and survey your surroundings. 
'''
    print(textwrap.fill(griffin_buts_in))
    print(textwrap.fill(ss.house_description))
    print(textwrap.fill(ss.gabby_and_avery))
    options = '''
    Option 1: “Uh, hi everybody! I’m a big fan, and Avery I really like your nipples.”

    Option 2: “Hi everyone, I’m excited to jam!”
'''
    while True:
        answer = input(textwrap.dedent(options) + "> ")
        if answer in ['1', '2']:
            break
    
    if answer == '1':
        print(textwrap.fill(ss.nipples))
    else:
        response = f'''
        “Jam? I thought she was just here to watch.”
Gabrielle doesn’t even look up from her glasses as she cuts you with her tongue.
“Well, she is a musician. We could potentially use a {instrument} player” says Griffin. 
“Everybody in our school is a musician, and our band already seems too full.” She sighs, “But fine, I guess we could see how today goes.”

        '''
        print(textwrap.fill(response))
    
    print(textwrap.fill(ss.intro_practice_room))
    options = """
    1: Sit in the chair
    2: Explore the room
    3: Stay put
"""
    print(textwrap.fill(options))
    
    
    while True:
        answer = input("> ")
        if answer in ['1','2','3']:
            break
    
    if answer == '1':
        print(textwrap.fill(ss.practice1))
    elif answer == '2':
        print(textwrap.fill(ss.practice2))
    else:
        print(textwrap.fill(ss.practice3))
    
