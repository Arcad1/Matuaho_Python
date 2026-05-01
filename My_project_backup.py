from lesson_header import *

# Variables
number_of_obstacles = 4
obstacle_count = 0
move_speed = 220
warning_distance_cm = 10
eye_colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),]
distance_cup = 0
# Function ideas
# def show_progress(...):
#     ...
def flash_progress():
    if obstacle_count < 4:
        eyes.set_both(0, 0, 255)
        print("{} cups left".format(obstacle_count))
    elif obstacle_count >= 4:
        eyes.set_both(255, 0, 0,)
        print("4 cups passed")

# def choose_move(...):
def choose_move():
    global distance_cm
    global obstacle_count
    global distance_cup
    distance_cm = sonar.get_distance_cm(filtered=True)
    print("Robot is {}cm away from object".format(distance_cm))
    if distance_cm > warning_distance_cm:
        moves.forward(1.0)
        flash_progress()
    else:
        obstacle_count += 1
    if distance_cm >= warning_distance_cm:
        if distance_cup > 10:
            moves.move_left(1.4)
            distance_cup += 1
        else:
            moves.move_right(1.4)
            distance_cup -= 1
            
    

# Loop ideas
# for ...:
#     ...
#
# while ...:
#     read sensor
#     decide what to do
#     move
#     update progress
while obstacle_count < number_of_obstacles:
    choose_move()

# Finish safely when you are done.
# stop_project_robot()
stop_project_robot()
