# Hour 05 - Global Variables (Simple Version)
# Global variables can be used anywhere in the program

print("GLOBAL VARIABLES - Easy Examples")
print("=" * 38)

# Example 1: Simple global variable
print("\n1. Global variable for school name:")
school_name = "Happy Elementary"  # This is global

def show_student_info(student_name):
    print(student_name, "goes to", school_name)

def show_teacher_info(teacher_name):
    print(teacher_name, "teaches at", school_name)

show_student_info("Amy")
show_student_info("Ben")
show_teacher_info("Ms. Johnson")

# Example 2: Global counter
print("\n2. Global counter:")
visitor_count = 0  # Global variable

def new_visitor(name):
    global visitor_count  # Tell Python we want to change the global variable
    visitor_count = visitor_count + 1
    print("Welcome", name, "! You are visitor number", visitor_count)

new_visitor("Alice")
new_visitor("Bob")
new_visitor("Carol")

# Example 3: Global game score
print("\n3. Global game score:")
total_score = 0  # Global variable

def add_points(points):
    global total_score
    total_score = total_score + points
    print("Added", points, "points. Total score:", total_score)

def show_final_score():
    print("Final score is", total_score)

add_points(10)
add_points(25)
add_points(5)
show_final_score()

# Example 4: Global settings
print("\n4. Global settings:")
game_difficulty = "Easy"  # Global variable
player_lives = 3         # Global variable

def show_game_status():
    print("Difficulty:", game_difficulty)
    print("Lives left:", player_lives)

def change_difficulty(new_difficulty):
    global game_difficulty
    game_difficulty = new_difficulty
    print("Changed difficulty to", game_difficulty)

def lose_life():
    global player_lives
    player_lives = player_lives - 1
    print("Lost a life! Lives left:", player_lives)

show_game_status()
change_difficulty("Hard")
lose_life()
show_game_status()

print("\nRemember: Global variables can be used in any function!")