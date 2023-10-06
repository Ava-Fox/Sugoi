import textwrap
import story_script as ss 

#Prompt user if wanna play/what your name is 
print(textwrap.fill(ss.intro))
your_name = input('''\n"What's your name, hotshot?"\n> ''')

invite_to_practice = f'''
    "I like your stuff, {your_name.title()}. What do you think about coming over to my band's next practice to jam?"
    ''' #An explination of what happens next, he invites you over to meet the band, you choose yes or no

print(textwrap.dedent(invite_to_practice))
print(textwrap.fill(ss.realization))
    #starting game???

prompt = "\n> do you wanna go? (yes/no) "
answer = input(prompt)

if answer != "no":
    #He takes you to band practice
    band_practice = "\nA section explaining what band practice is like and meeting secondary characters and explaining how hot they are"
    print(band_practice)
        
else:
   #End game
    back_out = '''
        \nYou realize you're too much of a loser to be cool and you drop all of your stuff in your rush to escape, embarrasing yourself thoroughly.
        '''
    print(textwrap.dedent(back_out))

