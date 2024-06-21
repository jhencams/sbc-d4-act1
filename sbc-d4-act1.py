from random import randint

# Function to get player choices
def get_choice(player):
    if player == "P1":
        return int(input("Enter '0' for unfold or '1' for fold: "))
    else:
        return randint(0, 1)

# Function to display choices
def display_choices(p1, c2, c3):
    choices = {0: "unfold", 1: "fold"}
    print(f"P1: {choices[p1]}, C2: {choices[c2]}, C3: {choices[c3]}")

# Function to determine the winner
def determine_winner(p1, c2, c3):
    winning_combinations = {
        (0, 1, 1): "You win",
        (1, 0, 0): "You win",
        (1, 0, 1): "C2 wins",
        (0, 1, 0): "C2 wins",
        (1, 1, 0): "C3 wins",
        (0, 0, 1): "C3 wins"
    }
    result = winning_combinations.get((p1, c2, c3), "It's a tie")
    print(result)

# Get choices
p1 = get_choice("P1")
c2 = get_choice("C2")
c3 = get_choice("C3")

# Display the choices
display_choices(p1, c2, c3)

# Determine and display the winner
determine_winner(p1, c2, c3)
