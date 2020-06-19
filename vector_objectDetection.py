#!/usr/bin/env python3

"""Making Vector to detect 600 objects from Google OpenImageDataset"""
import time
from main.model.detect_odr import object_detection
from PIL import Image
import anki_vector
from anki_vector.util import degrees
import anki_vector.camera

robot = anki_vector.Robot(anki_vector.util.parse_command_args().serial)#, enable_camera_feed=True)
screen_dimensions = anki_vector.screen.SCREEN_WIDTH, anki_vector.screen.SCREEN_HEIGHT
image_file = "detect.jpg"


def detect_labels(image_path):
    """
    This function calls the object detection library to detect 600 objects
    :param image_path:
    :return: class labels
    """
    try:
        classes = object_detection(image_path)
        if len(classes) == 0:
            return 'no objects'
        class_list = []
        for class_names in classes:
           class_list.append(class_names)

        print('Labels: {}'.format(classes))
        return ', '.join(class_list)

    except:
        return 'no objects'


def connect_robot():
    robot.connect()
    print('Connecting vector')


def disconnect_robot():
    robot.disconnect()
    print('Disconnected vector')


def display_camera():
    robot.camera.init_camera_feed()
    robot.vision.enable_display_camera_feed_on_face(True)


def close_camera():
    print('Close camera')
    robot.vision.enable_display_camera_feed_on_face(False)
    robot.camera.close_camera_feed()


def save_image(file_name):
    print('Save image')
    image = robot.camera.latest_image.raw_image.save(file_name, 'JPEG')


def display_image(file_name):
    print('display image = {}'.format(file_name))
    image = Image.open(file_name)
    screen_data = anki_vector.screen.convert_image_to_screen_data(image.resize(screen_dimensions))
    robot.screen.set_screen_with_image_data(screen_data, 5.0, True)


def vector_speaks(text):
    print('Vector: {}'.format(text))
    robot.behavior.say_text(text)


def detect():
    display_camera()
    vector_speaks('Hey, I am going to find some objects, and will tell you what I found')
    vector_speaks('I will take a photo of this environment, and  will analyze using my deep learning based brain')
    time.sleep(1)
    save_image(image_file)
    display_image(image_file)

    vector_speaks('Wait a minute. I am trying to find some objects, I will let you know now.')
    text = detect_labels(image_file)
    display_image(image_file)
    vector_speaks('I can detect {}'.format(text))

    close_camera()


if __name__ == "__main__":
    while True:
        connect_robot()
        try:
            detect()
        except Exception as e:
            print('Exception Handled', e)

        disconnect_robot()
