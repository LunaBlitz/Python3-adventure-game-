import pyfiglet
from time import sleep


# These functions are for better spacing so the user can read the story easier and to keep redudancey in the code to a minumum.


def story_scroll():
    print('\n\n\n\n\n\n\n\n\n\n\n')
    sleep(2)


def pause():
    print('\n\n')
    sleep(4)


make_more_choices = True
left_or_right = True

print("Welcome to the Adventure game...")
pause()

# Title was edited with pyfiglet.'pyfiglet.print_figlet(text, font='', justify='') <-This portion of code prints the title and formats it in this order: text you want, font, and placement of text. Format must be in this order or you will get an error. If you want the standard font only put the word you want printed and placement of the words.
pyfiglet.print_figlet("The Hallow", "poison", justify='center')

pause()

pyfiglet.print_figlet('HOW TO PLAY ', justify='center')  # print command within pyfgilet that centers the 'how to play' title.

pause()
# Instructions of how to play the game may get some editing later for easier reading.
print("This adventure game places you in a forest where you are trying your best to find your way out. You will be given choices to on what to do. Based on the decisions you make your results could be good or bad. Make the right decisions and you'll get out of the forest alive. To enter your choices you will type one of the choices given and then press enter. Good Luck!")


pause()
sleep(10)  # giving the player more time to read

# Beginning of the game. Will probably edit how the game starts to either illustration of a forest or a better opening to the story.
print("You're playing fetch with your dog named spot and you throw the ball too far and it flies into the forest. Spot goes rushing in after the ball and he disappears into the darkness of the all the trees. You go in after your dog. As you walk past some bushes and over muddy ditches you come to a fork in the forest. Both paths having trees that give a hallway shape inclosure as you look further down to see the end of them. On the left you see woodlan creatures of all kinds moving throughout that path. On the right you see dark shadows passing swiftly from the ground to the branches of the trees. ")

pause()

where_to_go = input("Left or Right? Where would you like to go?")
pause()
# Created a while loop with if statements insde so each choice can give a new part of the story. Also the while loop will help for when the user tries to give inputs that aren't the given choices. It will tell the user they gave an invald option and will loop back to the question and their need for input.
while left_or_right:
    if where_to_go.lower() in ['left', 'Left', 'l', 'L']:
        print("As you walk to the left you see faries and see fairy dust falling from the tree branches. You inhale the dust and begin to sneeze so much that you start to fly. Not gaining any control over yourself you continue to sneese and go higher.")
        break  # break statement forces while loop to stop and go to next loop.

    elif where_to_go.lower() in ['right', 'Right', 'R', 'r']:
        print("You slowly pass by the shadows to not draw attention to yourself. While walking by you hear groans and growling in the distance. You hesitate for a moment and then see a giant dark shadow behind you rushing in forward in your direction.")
        break  # break statement forces while loop to stop and go to next loop.
    else:
        print('Please choose Left or Right')


pause()
# This while loop uses the if statements to present more choices based on the previous choice input from the user. This loop is also created in case the player gives incorrect input so it can loop and ask the questions again.
while make_more_choices:
    if where_to_go.lower() in ['left', 'Left', 'l', 'L']:
        what_to_do = input("Grab a branch or keep flying?")

        if what_to_do.lower() in ['grab a branch', 'Grab a branch', 'GRAB A BRANCH', 'Grab A Branch']:
            print('You grab the branch and eat some from fruit from the branch and slowly float back down again.')
            pause()
            print("You stand for a moment to get your bearings. Then you hear your dog barking in the distance. You run toward his barking and find him stuck under a bush. Once you help him get free you find your way out the forest and go back home safe and sound unsure of if you should ever tell anyone of what happened.")
            break

        elif what_to_do.lower() in ['keep flying', 'KEEP FLYING', 'Keep Flying']:
            print('You keep flying and sneezing until you leave the forest and are in the clouds where you see dragons flying. A dragon comes and flies furiously to come and eat you.')
            print("You Died!")
            break
        else:
            print("please enter one of the following choices. ")
            continue  # forces the while loop to stop here and go back to the beginnning instead of continuing on to the rest of the if statements.

    pause()

    if where_to_go.lower() in ['right', 'RIGHT', 'R', 'r', 'Right']:
        what_to_do = input('Run or face the shadow?')

        if what_to_do.lower() in ['run', 'RUN', 'Run', 'Run!', 'RUN!']:
            print(' You run and trip over a rock and you see the shadow close in on you. It consumes your soul!')
            print("You Died!")
            break  # forces the loop to end and end the story.

        elif what_to_do.lower() in ['face the shadow', 'FACE THE SHADOW', 'Face The Shadow']:
            print("You close your eyes and stand with your chest out to the shadow and it gives a loud screetch and runs the other way.")
            pause()
            print("You stand for a moment to get your bearings. Then you hear your dog barking in the distance. You run toward his barking and find him stuck under a bush. Once you help him get free you find your way out the forest and go back home safe and sound unsure of if you should ever tell anyone of what happened.")
            break  # forces the loop to end and end the story.

        else:
            print("please enter one of the given choices")
            continue


pause()

print('{:^80}'.format("THE END"))
