import textwrap
import story_script as ss 

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

if answer != "no":
    #He takes you to band practice
    band_practice = "\nA section explaining what band practice is like and meeting secondary characters and explaining how hot they are"
    print(textwrap.fill(ss.band_practice))

    instrument = input("\n> What do you play? ")
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

        
else:
   #End game
    back_out = '''
        \nYou realize you're too much of a loser to be cool and you drop all of your stuff in your rush to escape, embarrasing yourself thoroughly.
        '''
    print(textwrap.dedent(back_out))

