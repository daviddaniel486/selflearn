"""
File: carrace.py
----------------
This program simulates a car racing game.
"""
import time


def main():
# Set a null variable
    command = ''
    started = False

# While command is true, play game...
    while True:
# get input from player
        command = input('> ').lower()
# if player's input is start...get car to start.
        if command == 'start':
            position = 8
            boost_count = 0
# To avoid repetition of response, we use a boolean variable to ensure that the car only starts once.
            if started:
                print("Car's already started")
                print()
            else:
                started = True
                start_time = time.time()
                print("Car started...")
                print(f"You are {position}th position")
            elapsed = round(time.time() - start_time)
            if elapsed > 10:
                print("Player 1, you're far behind.")

#if player's input is stop...get car to stop.
        elif command == 'stop':
            if not started:
                print("Car's already stopped")
            else:
                started = False
                print("Car's stopped.")
        elif command == "boost":
            if started :
                print("...Nitros boost")
                boost_count += 1
                if boost_count >= 1:
                    time.sleep(5)
                if boost_count == 3:
                    position -= 1
                    print(f"You are now {position}th position")
                    boost_count = 0
            if not started:
                print("Car's not started")
            elif command == "Pause" :
                print("Game paused....")

#if player's input is help, display prompt.
        elif command == 'help':
            print(
            """
Start - To start the car.
Stop - To stop the car.
Pause - To pause the game.
Boost - Enter "boost" every 10 secs to avoid crash
Quit - To quit the game.
            """)
        elif command == 'quit':
            break
        else:
            print("Sorry, I don't understand that")
        elapsed = round(time.time() - start_time)
        race_duration = 300
        if elapsed == race_duration :
            print("You're close to the finish line...")
            time.sleep(10)
            print("Finished!!")
            print(f"You're {position}th position.")









































































































if __name__ == '__main__':
    main()