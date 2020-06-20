# Programming Vector to recognize objects using Deep learning
In this program, we will see how to use an object detector with the Vector SDK to enable the robot to detect around 600 objects.

# Vector SDK
The Vector SDK gives access to various capabilities of this robot, such as computer vision, Artificial intelligence, navigation and et. You can design your own programs to make this robot pet imbibed with AI capabilities. Before running this module, install the vector SDK by following the information in this page: https://developer.anki.com/vector/docs/index.html.  
- python3 -m pip install --user anki_vector
# Object Detection using Deep Learning
To detect objects, we will be using FasterRCNN which is trained with Google Open Image dataset. It consist a ResNet with an RPN, and can detect more than 600 object categories. That means, the vector will be able to detect large number of objects. However, we have few more dependecies to make Vector recognize those objects. The following main dependencies are based on my testing platform, but you can change them according to the machine in which you will be implementing.
 - Python 3.6 
 - Tensorflow 1.12.0
 - Keras 2.2.4
 - OpenCV 3

Please download  the object detection module from here, https://drive.google.com/file/d/113-3Kud0Ner2NR4ZiSOnQUOq5C4G16CC/view?usp=sharing and put it inside the data folder.

# Running the Module
Please clone or download this repository into your local machine, but before that you need to authenticate the vector robot.
To authenticate with the robot, type the following into the Terminal window. 

- python3 -m anki_vector.configure

Please note that the robot and your computer should be connected to the same network.
Now, you will be asked to enter your robot’s name, ip address and serial number, which you can find in the robot itself. Also, You will be asked for your Anki login and password which you used to set up your Vector.

IF you see “SUCCESS!” then your robot is connected to your computer, and you can run this module by typing.

- python vector_objectDetection.py

Now, the robot will grab a picture and will analyze the image to discover what all objects are present in the image using a deep learning based object detection algorithm.
