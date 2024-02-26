# GestureCV
A Python program to control your computer with gestures using computer vision

### Background
I have a habit of watching YouTube videos while I eat, and I wanted a way to control my laptop without touching my touchpad or mouse to avoid getting it dirty with anything that may be on my hands. I also wanted to play around with some Computer Vision tools. In the future, I can see a more polished version of this project as a solution to accessibility issues for users who aren't able to use a traditional mouse and keyboard.

This project uses Google's [MediaPipe](https://developers.google.com/mediapipe/solutions) and  `OpenCV` for the ML hand detection model, and uses `PyAutoGUI` and `webbrowser` to translate the model's detections into interactions with the computer.


## Setup

### Virtual Environment (Optional)

Running the project in a virtual environment may be ideal to avoid conflicts.

To create an environment, clone the repo and inside the directory run the following:

```
python -m venv env
```

**"env"** can be replaced with whatever you would like to name the environment.


After creating the environment run either of the following to activate the environment:

For Windows
```
env\Scripts\activate
```

For Unix or Mac OS
```
source env/bin/activate
```

### Install Dependencies

To install the required dependencies run the following either in the project directory or in a virtual environment:

```
pip install -r requirements.txt
```

## Run 
To run the program run the following either in the project directory or in a virtual environment:

```
python app.py
```

Or:
```
python3 app.py
```

## Docker

I tried to set up Docker with this project but was running into issues getting access to my display and webcam for OpenCV while it runs in the docker container. However, there is a sample dockerfile in the repo.

Create a docker image of the program with:

```
docker build -t gesture-cv . 
```

