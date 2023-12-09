import os
import cv2
import numpy as np
import mediapipe as mp


def build_training_arrow_data(video_dir: str, window_len: int, target_joints: list[mp.solutions.holistic.PoseLandmark]) -> None:

    holistic = mp.solutions.holistic.Holistic()

    X_training = []
    y_training = []

    video_paths = [os.path.join(video_dir, video_name)
                   for video_name in os.listdir(video_dir)]

    for idx_video, video_path in enumerate(video_paths):
        cap = cv2.VideoCapture(video_path)
        print(f"Processing video #{idx_video+1}...")

        frame_buffer = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(frame_rgb)

            if results.pose_landmarks:
                data = []
                for target_joint in target_joints:
                    target_coords = results.pose_landmarks.landmark[target_joint]
                    target_input = [target_coords.x,  target_coords.y]
                    data += target_input

                nose_coords = results.pose_landmarks.landmark[mp.solutions.holistic.PoseLandmark.NOSE]
                nose_input = [nose_coords.x, nose_coords.y]
                data += nose_input
                
                frame_buffer.append(data)

                if len(frame_buffer) >= window_len:
                    X_training.append(frame_buffer[:int(window_len/2)])
                    y_training.append(frame_buffer[-1][:len(target_joints)*2])
                    frame_buffer = frame_buffer[1:]

            cv2.imshow('Video', frame)

        cap.release()

    return np.array(X_training), np.array(y_training)
