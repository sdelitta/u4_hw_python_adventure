# Create your own adventure with python here
def start_game(): 
    answer = input("Avast, ye weary traveller! Are you ready to start your journey? (yes/no) ")

    if answer.lower().strip() == "yes":
        answer = input("You reach a crossroads. Which way would you like to go? (left/right) ").lower().strip()
        if answer == "left":
            answer = input("Left, eh? My ex wife was a lefty so we'll have you encounter a ferocious beast. How will you respond? (flee/attack) ").lower().strip()

            if answer == "flee":
                answer = input("Coward! Go back to your mother and nurse until you're ready for a challenge! Or are you feeling lucky? (yes/no) ").lower().strip()
                if answer == "yes":
                    return start_game()
                else:
                    print("Well then. piss off!")

            elif answer == "attack":
                answer = input("Such courage! Well'p your bravery seems to have outmatched your wits. The beast hath slain you. How shall your bloody pulp of a carcass proceed? Play again? (yes/no)").lower().strip()
                if answer == "yes":
                    return start_game()
                else:
                    print("Well then. piss off!")

            else:
                answer = input("You fool! That wasn't a valid choice!! Try again? (yes/no) ").lower().strip()
                if answer == "yes":
                    return start_game()
                else:
                    print("Well then. piss off!")

        elif answer == "right":
            answer = input("Right on. Down this path you're greeted by a wizard. He's experimenting with new transportation spells and offers to send you to a destination of your choosing. Do you accept? (yes/no) ").lower().strip()
            if answer == "yes":
                answer = input("The sorcerer is seemingly pleased with your response and begins to spout off what sounds like the nonsensical ramblings of a madman, but only until he asks you for the destination of your choice: a tropical island or the fair princesses chambers  (island/princess").lower().strip()
                if answer == "island":
                    answer = input("The sorcerer laughs maniacally as he aims his staff and casts a beam of piercing blue light your way. As the light fades and your eyes readjust, you find yourself alone on a desserted island, destined to live the rest of your days in starving solitude. Play again? (yes/no) ").lower().strip()
                    if answer == "yes":
                        return start_game()
                    else:
                        print("Well then. piss off!")
                elif answer == "princess":
                    answer = input("The sorcerer fumbles to remember the correct transportation spell and carelessly replaces key phrases with manic gibberish. You find yourself in the chambers of the king, surrounded by dozens of guards who are about to lay waste to your defensless bag of bones, but not before you turn into a newt and croak. Play again? (yes/no) ").lower().strip()
                    if answer == "yes":
                        return start_game()
                    else:
                        print("Well then. piss off!")
                else:
                    answer = input("You fool! That wasn't a valid choice!! Try again? (yes/no) ").lower().strip()
                    if answer == "yes":
                        return start_game()
                    else:
                        print("Well then. piss off!")
        else:
            answer = input("You fool! That wasn't a valid choice!! Try again? (yes/no) ").lower().strip()
            if answer == "yes":
                return start_game()
            else:
                print("Well then. piss off!")
    else:
        print("Well then. Piss off!")
