# Gesture-Based Interaction with Feedforward

## Introduction

Within the scope of the User Interface Technologies (UIT) course, we have embarked on the development of a 3D feed- forward system, aimed at gestural interaction via webcam to allow users to interface with the computer through gestures, receiving visual feedback in real time to facilitate the learning and execution of movement sequences.

## V Arrows 

![Example gesture "pushup"](./gifs/pushup.gif)

## V GIFs

![Example Gifs version](./gifs/video-gifs.gif)

## Getting Started (Development)

1. Clone the repository and `cd` into it:

    ```bash
    git clone https://github.com/tkachenko0/3d-Gesture-Feedbacks-and-Feeedforwards.git
    # cd into the project directory
    cd 3D-Gesture-Feedbacks-and-Feeedforwards
    ```

2. Create a virtual environment:

    ```bash
    python3.9 -m venv <YOUR-VENV-NAME>
    ```

3. Activate the virtual environment:

    ```bash
    source <YOUR-VENV-NAME>/bin/activate
    ```

4. Install the dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

5. Setup your environment variables in the `.properties` file:

    ```
    touch .properties
    ```

    ```properties
    # Example of the .properties file
    CAMERA_INDEX=1 # the index of the camera to use
    ```

> **Note:** If you install new dependencies, make sure to update the `requirements.txt` file:

```bash
pip3 freeze > requirements.txt
```

## References

- [Mediapipe](https://google.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)
- [Tensorflow](https://www.tensorflow.org/)