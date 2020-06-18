#!/usr/bin/env python3

"""Making Vector to detect 600 objects from Google OpenImageDataset"""
import os
import time
import random
from main.model.detect_odr import object_detection
from PIL import Image
import anki_vector
from anki_vector.util import degrees
import anki_vector.camera

robot = anki_vector.Robot(anki_vector.util.parse_command_args().serial)#, enable_camera_feed=True)
screen_dimensions = anki_vector.screen.SCREEN_WIDTH, anki_vector.screen.SCREEN_HEIGHT
current_directory = os.path.dirname(os.path.realpath(__file__))
image_file = os.path.join(current_directory, 'resources', "latest.jpg")


def detect_labels(image_path):
    """
    This function calls the object detection library to detect 600 objects
    :param image_path:
    :return: class labels
    """
    try:
        classes = object_detection(image_path)
        class_list = []
        for class_names in classes:
           class_list.append(class_names)

        print('Labels: {}'.format(classes))
        return ', '.join(class_list)
    except:
        return 'Sorry, I cannot detect any objects'


def connect_robot():
    print('Connecting vector')
    robot.connect()


def disconnect_robot():
    robot.disconnect()
    print('Disconnected vector')


def stand_by():
    # If necessary, move Vector's Head and Lift to make it easy to see his face
    robot.behavior.set_lift_height(0.0)


def show_camera():
    print('Show camera')
    robot.camera.init_camera_feed()
    robot.vision.enable_display_camera_feed_on_face(True)


def close_camera():
    print('Close camera')
    robot.vision.enable_display_camera_feed_on_face(False)
    robot.camera.close_camera_feed()


def save_image(file_name):
    print('Save image')
    image = robot.camera.latest_image.raw_image.save(file_name, 'JPEG')

def show_image(file_name):
    print('Show image = {}'.format(file_name))

    # Load an image
    image = Image.open(file_name)
    # Convert the image to the format used by the Screen
    print("Display image on Vector's face...")
    screen_data = anki_vector.screen.convert_image_to_screen_data(image.resize(screen_dimensions))
    robot.screen.set_screen_with_image_data(screen_data, 5.0, True)


def robot_say(text):
    print('Say {}'.format(text))
    robot.behavior.say_text(text)


def analyze():
    stand_by()
    show_camera()
    robot_say('Hey surjit. I found something interesting, and I will tell you.')
    time.sleep(1)

    robot_say('I will take a photo of this environment')
    time.sleep(1)
    robot_say('I will analyze using my deep learning based brain')


    save_image(image_file)
    show_image(image_file)
    time.sleep(1)

    robot_say('Hey Surjit, I am trying to find what all objects are there. I will be using Deep learning object detection algorithm')
    text = detect_labels(image_file)
    show_image(image_file)
    robot_say('I can detect {}'.format(text))

    close_camera()
    robot_say('Over, goodbye!')


def main():
    while True:
        connect_robot()
        try:
            analyze()
        except Exception as e:
            print('Analyze Exception: {}', e)

        disconnect_robot()
        time.sleep(random.randint(30, 60 * 5))


if __name__ == "__main__":
    main()
