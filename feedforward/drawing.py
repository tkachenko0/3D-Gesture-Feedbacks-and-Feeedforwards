import mediapipe as mp
import cv2
from matplotlib import pyplot as plt


def draw_pose_landmarks(image, results):
    mp.solutions.drawing_utils.draw_landmarks(
        image,
        results.pose_landmarks,
        mp.solutions.holistic.POSE_CONNECTIONS,
        mp.solutions.drawing_utils.DrawingSpec(
            color=(80, 22, 10), thickness=2, circle_radius=4),
        mp.solutions.drawing_utils.DrawingSpec(
            color=(80, 44, 121), thickness=2, circle_radius=2)
    )


def draw_frame(frame_index, landmarks_list):
    plt.clf()
    body_landmarks = landmarks_list[frame_index]

    x = [lm.x for lm in body_landmarks.landmark]
    y = [lm.y for lm in body_landmarks.landmark]

    plt.scatter(x, y, s=20, c='blue')

    connections = [(11, 12), (12, 24), (24, 23), (23, 11),
                   (11, 13), (13, 15), (15, 17),
                   (12, 14), (14, 16), (16, 18),
                   (11, 25), (25, 23),
                   (24, 26), (26, 28), (28, 30),
                   (23, 27), (27, 29), (29, 31)]

    for connection in connections:
        plt.plot([x[connection[0]], x[connection[1]]], [
                 y[connection[0]], y[connection[1]]], c='blue')

    plt.axis('off')

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().invert_yaxis()


def prob_viz(res, actions, input_frame):
    colors = [(245, 117, 16), (117, 245, 16), (16, 117, 245)]
    output_frame = input_frame.copy()
    for num, prob in enumerate(res):
        cv2.rectangle(output_frame, (0,60+num*40), (int(prob*100), 90+num*40), colors[num], -1)
        cv2.putText(output_frame, actions[num], (0, 85+num*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
    return output_frame