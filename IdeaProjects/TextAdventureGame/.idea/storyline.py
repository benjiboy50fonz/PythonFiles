from actioncommandgroups import StoryMethods
from Miscellaneous.weaponclasses import Weapons

# Import Above Here
print('Welcome to the text adventure game, Iosis!\n\nPlease enjoy the game, and remember! Your progress will NOT be saved!')
name_input = raw_input('\n\nWhat would you like to name your character?: ')
gender_input = raw_input('\nIs ' + ' a male or female? (Please enter \'male\' or \'female\'{Default is male!}): ')

pistol = Weapons()
ar = Weapons()
char = StoryMethods(str(name_input), gender_input)


# Begin Storyline with commands! (Below)

char.BeginStory(char)

#except (TypeError, SyntaxError, NameError, ValueError):
 #   print("I do not know how you messed this up, but I was ready for it. Please restart the game!")
  #  exit()
