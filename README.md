# Evaluating the computation versus communication trade-off on IoT-like nodes for speech recognition applications
Term project for Energy Aware Computing (18-743) at Carnegie Mellon University
Namrita Murali and Marie Shaw

In an era of smart homes and smart devices, embedded devices are becoming increasingly common as a form of data collection and processing. Moreover, an increasing number of smart home devices are being controlled by voice input, which makes audio processing on embedded devices crucial. In order to process these large datasets, devices need to determine whether to perform complex Machine Learning algorithms on the device or offload them to a server. Since these devices are energy and network constrained, there are energy and time tradeoffs between processing locally or externally. This paper analyzes how performance and energy consumption varies when performing speech recognition processing locally on an embedded device or externally on a server. 

# Motivation 
There are around 23.14 billion connected devices in the world in 2018, and that number is projected to more than triple by the year 2025\cite{b1}. These connected devices are responsible for collecting and processing data, but are both power and network constrained. Small embedded devices with limited power and memory that perform heavy machine learning computation face very slow performance and poor battery life. With more and more of these connected devices appearing in people's homes and many other environments, there is a need to process huge amounts of data with high performance. The choice of performing machine learning computation on an embedded device or sending the data to an external server for processing is crucial to the tradeoff between energy consumption and performance. Doing the computation on-board consumes more energy for computation, while doing it online consumes more energy for communication.

Speech recognition is a very common application of IoT data processing, Almost one in five Americans has access to a smart speaker, like a Google Home or Amazon Alexa \cite{b2}. Many other connected devices are voice controlled, and require speech processing on device in order to interpret commands.

# Milestones and Goals
The goal of this project is to analyze how energy and processing performance vary when data processing occurs on an embedded device and when it occurs on an external server, specifically related to speech recognition applications. 

The first phase will be to run the application locally on the Raspberry Pi and measure the power consumption and time it takes to run. This phase will be run in successive iterations to determine the average power consumption and time for the application. The application will involve recording data using the Raspberry Pi microphone, but the recording of the data will be separate from this initial phase.

The second phase will be to send the audio samples via WiFi to a server, and run the application on the server, and measure the power consumption of both the Raspberry Pi and the server and the time it takes to run including the communication time. This phase will also be run in successive iterations to determine the average power consumption and time for the application. 

We will then graphically compare the power consumption on two applications.

Further work can either compare the power consumption and performance of this same experiment on different speech recognition engines, or the power consumption and performance different applications.

# Hardware
We will use a Raspberry Pi as the embedded system to collect data and perform local processing. Raspberry Pis are easy to obtain and are very commonly used as a part of IoT systems, so they are good candidates for analysis. 
To process the speech externally, the Pi will need to talk to a server on the cloud. To do this we will need an internet connection, so we will use a Raspberry Pi 3.

We also will need a microphone to gather speech as an input. We will mostly likely use a USB microphone, as they seem to be commonly used for development with Raspberry Pis.

To measure the power usage of the Pi, we need a wall outlet power meter or an USB power meter. 

# Software
CMU Sphinx is an open-source large vocabulary, speaker-independent continuous speech recognition engine. It is specifically tuned for handheld and mobile devices, but it can work on desktop devices as well. It provides an API for processing and decoding audio files. The main advantages of using PocketSphinx are that is is very stable, allows for reentrant decoding, and significantly reduced memory consumption than other speech recognition engines. While we are not measuring the energy consumption across different engines, it is beneficial that it has a smaller memory footprint so that we are able to run it on the Raspberry Pi.



