from lesson_header import *
from storage import *
# Variables
number_of_obstacles = 5
obstacle_count = 0
move_speed = 220
warning_distance_cm = 17
eye_colours = [
     eyes.set_both(255, 0, 0,),
     eyes.set_both(0, 255, 0,),
     eyes.set_both(0, 0, 255,),
     eyes.set_both(255, 255, 0,),
     eyes.set_both(255, 0, 255,)
]
distance_cup = 0
# Function ideas

def get_eye_colour(self, sensor_value):
    return self.sensor_to_colour.get(sensor_value, "OFF")
# def show_progress(...):
#     ...
def flash_progress():
    global obstacle_count
    global eye_colours
    if obstacle_count < 4:
        eyes.set_both(0, 0, 255)
        print("---------{} cups left----------".format(obstacle_count))
    elif obstacle_count >= 4:
        print("done")
        eyes.set_both(255, 0, 0)
        with open("test.txt") as f:
            print(f.read)
    
        with open("test.txt", "a") as f:
            f.write(f"\n {cups_passed()}")

# def choose_move(...):
def choose_move():
    global distance_cm
    global obstacle_count
    global distance_cup
    global warning_distance_cm
    distance_cm = sonar.get_distance_cm(filtered=True)
    print("Robot is {}cm away from object".format(distance_cm))
    if distance_cm > warning_distance_cm:
        moves.forward(0.6)
    else:
        obstacle_count += 1
        flash_progress()
        if distance_cup == 0:
            moves.move_right(1.4)
            distance_cup += 1
        else:
            moves.move_left(1.4)
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
