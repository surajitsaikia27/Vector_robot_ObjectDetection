#Programming Vector to recognize objects
In this program, we will see how to use an object detector with the Vector SDK to enable the robot to detect around 600 objects.

# Vector SDK
The Vector SDK gives access to various capabilities of this robot, such as computer vision, Artificial intelligence, navigation and et. You can design your own programs to make this robot pet imbibed with AI capabilities. Before running this module, install the vector SDK by following the information in this page: https://developer.anki.com/vector/docs/index.html.  
# Object Detection using Deep Learning
To detect objects, we will be using FasterRCNN which is trained with Google Open Image dataset. It consist a ResNet with an RPN, and can detect more than 600 object categories. That means, the vector will be able to detect large number of objects. However, we have few more dependecies to make Vector recognize those objects. The following dependencies are based on my testing platform, but you can change them according to the machine in which you will be implementing.
 - Tensorflow 1.12.0
 - Keras 2.2.4
 - OpenCV 3
