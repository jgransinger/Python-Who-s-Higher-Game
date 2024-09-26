import random
from game_data import data

#place new person in a function and assign a variable to each
def assign_new_people():
        person1 = data[random.randint(0,len(data) - 1)]
        person2 = data[random.randint(0,len(data) - 1)]
        people = [person1, person2]
        return people

#compare the follower counts
def compare_followers(people):
    print(people[0])   #CHANGE TO SENTENCES WHEN WORKING
    print(people[1])   #CHANGE TO SENTENCES WHEN WORKING
    if people[0]['follower_count'] > people[1]['follower_count']:
        higher_follower_count = 0
        print(f"{people[0]['name']} has more followers")   #DELETE WHEN WORKING
    elif people[1]['follower_count'] > people[0]['follower_count']:
        higher_follower_count = 1
        print(f"{people[1]['name']} has more followers")    #DELETE WHEN WORKING
    else:
        print("Something went wrong")    #DELETE WHEN WORKING
        higher_follower_count = "Something went wrong"    #FIX FIX FIX
    return higher_follower_count

#Player guesses who has more followers
def game():
    winner = compare_followers(assign_new_people())
    choice = int(input("Guess who has a higher follower count. Type '0' or '1': "))
    if choice == winner:
        print("CORRECT.\n")

        play_again()
        # Enter code to keep score / add a point
        ## ENTER CODE TO KEEP THE GAME GOING / PERFORM PERSON SWAP
    else:
        print("WRONG. Game Over.")
        ## ENTER CODE FOR GAME OVER. GIVE FINAL SCORE, play again, ETC.

#Person B become person A, person A becomes random then person B
def new_person_swap(people):
    people[0] = people[1]
    people[1] = data[random.randint(0,len(data) - 1)]
    return people

def play_again():
    game()

## START GAME
game()
