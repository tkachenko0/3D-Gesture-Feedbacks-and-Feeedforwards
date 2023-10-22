import cv2
import numpy as np
import mediapipe as mp

POSE_DESCRIPTOR_LEN = len(mp.solutions.holistic.PoseLandmark) * 4

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

def extract_pose_descriptor(results):
    return np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(POSE_DESCRIPTOR_LEN)
