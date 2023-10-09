import cv2
import numpy as np
from matplotlib import pyplot as plt
import mediapipe as mp
import matplotlib.animation as animation

mp_holistic = mp.solutions.holistic  # Holistic model
mp_drawing = mp.solutions.drawing_utils  # Drawing utilities
landmarks_list = []

def mediapipe_detection(image, model):
    # COLOR CONVERSION BGR 2 RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # COLOR COVERSION RGB 2 BGR
    return image, results

def draw_styled_landmarks(image, results):
    # Draw face connections
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
                              mp_drawing.DrawingSpec(
                                  color=(80, 110, 10), thickness=1, circle_radius=1),
                              mp_drawing.DrawingSpec(
                                  color=(80, 256, 121), thickness=1, circle_radius=1)
                              )
    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(
                                  color=(80, 22, 10), thickness=2, circle_radius=4),
                              mp_drawing.DrawingSpec(
                                  color=(80, 44, 121), thickness=2, circle_radius=2)
                              )
    # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                              mp_drawing.DrawingSpec(
                                  color=(121, 22, 76), thickness=2, circle_radius=4),
                              mp_drawing.DrawingSpec(
                                  color=(121, 44, 250), thickness=2, circle_radius=2)
                              )
    # Draw right hand connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                              mp_drawing.DrawingSpec(
                                  color=(245, 117, 66), thickness=2, circle_radius=4),
                              mp_drawing.DrawingSpec(
                                  color=(245, 66, 230), thickness=2, circle_radius=2)
                              )
    
def draw_frame(frame_index):
    plt.clf()
    body_landmarks = landmarks_list[frame_index]

    # Extract the x and y coordinates of the landmarks
    x = [lm.x for lm in body_landmarks.landmark]
    y = [lm.y for lm in body_landmarks.landmark]

    # Draw landmarks as points
    plt.scatter(x, y, s=20, c='blue')

    # Draw the connecting lines between the landmarks
    connections = [(11, 12), (12, 24), (24, 23), (23, 11),  # Head
                   (11, 13), (13, 15), (15, 17),  # Left Arm
                   (12, 14), (14, 16), (16, 18),  # Right Arm
                   (11, 25), (25, 23),  # Spine
                   (24, 26), (26, 28), (28, 30),  # Left Leg
                   (23, 27), (27, 29), (29, 31)]  # Right Leg

    for connection in connections:
        plt.plot([x[connection[0]], x[connection[1]]], [y[connection[0]], y[connection[1]]], c='blue')

    plt.axis('off')

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().invert_yaxis()

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    # Set mediapipe model 
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():

            # Read feed
            ret, frame = cap.read()

            # Make detections
            image, results = mediapipe_detection(frame, holistic)
            print(results)

            # Extract body landmarks and append them to the list
            body_landmarks = results.pose_landmarks
            if body_landmarks:
                landmarks_list.append(body_landmarks)

            # Draw landmarks
            draw_styled_landmarks(image, results)

            # Show to screen
            cv2.imshow('OpenCV Feed', image)

            # Break gracefully
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

        # Creation of the .gif
        fig = plt.figure()
        ani = animation.FuncAnimation(fig, draw_frame, frames=len(landmarks_list), interval=100)
        output_gif = 'stickman_animation.gif'
        ani.save(output_gif, writer='imagemagick', fps=10)

        print(f'GIF saved as {output_gif}')