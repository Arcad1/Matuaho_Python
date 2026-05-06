from lesson_header import *

eye_colours = {
     eyes.set_both(255, 0, 0,),
     eyes.set_both(0, 255, 0,),
     eyes.set_both(0, 0, 255,),
     eyes.set_both(255, 255, 0,),
     eyes.set_both(255, 0, 255,)
}

def write_log(message):
    log_file = open("robot_testing.md", "a")

    log_file.write(message + "\n")
    log_file_close()


sensor_readings =[1, 2, 5, 3, 2]

for sensor_value in sensor_readings:
    eye_colour = sensor_to_colour.get(sensor_value, "OFF")

    debug_message = (
        "Sensor: " + str(sensor_value) + 
        " -> Eye Colour: " + eye_colour
    )

    print(debug_message)

    write_log(debug_message)

print("Debug log written to robot_testing.md")
