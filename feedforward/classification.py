import os
import cv2
import numpy as np
import mediapipe as mp


def build_training_data(video_dir: str, window_len: int, target_joint: mp.solutions.holistic.PoseLandmark) -> None:

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
                right_wrist = results.pose_landmarks.landmark[target_joint]
                wrist_coords = [
                    right_wrist.x,
                    right_wrist.y,
                    # right_wrist.z
                ]

                frame_buffer.append(wrist_coords)

                if len(frame_buffer) >= window_len:
                    X_training.append(frame_buffer[:int(window_len/2)])
                    y_training.append(frame_buffer[-1])
                    frame_buffer = frame_buffer[1:]

            cv2.imshow('Video', frame)

        cap.release()

    return np.array(X_training), np.array(y_training)
