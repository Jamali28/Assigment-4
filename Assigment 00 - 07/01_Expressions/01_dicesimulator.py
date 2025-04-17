
import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Rolled: {die1} + {die2} = {total}")

def main():
    die1 = 10  # Local variable in main()
    print(f"die1 in main() starts as: {die1}")
    
    for i in range(3):
        print(f"Roll {i + 1}:")
        roll_dice()
    
    print(f"die1 in main() ends as: {die1}")

# Call the main() function when this script is run
if __name__ == '__main__':
    main()
    