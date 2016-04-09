#You can run this code in www.codeskulptor.org
#This is the implement of "Guess the number"
#which is the mini-protect of "An Introduction to Interactive Programming in Python"
import simplegui
import random
import math

num_range = 100
target = 0
remaining = 7

def new_game():
    global target, numrange, remaining
    target = random.randrange(num_range)
    if num_range == 100:
        remaining = 7
    elif num_range == 1000:
        remaining = 10
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", remaining
    print " "

    
def range100():
    global num_range
    num_range = 100
    new_game()
    
def range1000():
    global num_range
    num_range = 1000
    new_game()
   
def get_input(input_num):
    global remaining, target
    number = int(input_num)
    print "Guess was ", int(number)
    remaining = remaining - 1
    print "Number of remaining guesses is", remaining
    if remaining > 0:
        if number == target:
            print "Correct!\n"
            new_game()
        elif number > target:
            print "Lower!\n"
        else:
            print "Higher!\n"
    else:
        if number == target:
            print "Correct!\n"
        else:
            print "You ran out of guesses. The number was", target
            print " "
        new_game()
    

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Guess the number", 300, 200)
frame.add_button("Range is [0,100)", range100, 100)
frame.add_button("Range is [0,1000)", range1000, 100)
frame.add_input("Enter a guess", get_input, 100)

# Start the frame animation
frame.start()
new_game()
