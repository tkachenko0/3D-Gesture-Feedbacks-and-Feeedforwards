import mediapipe as mp

def draw_pose_landmarks(image, results):
    mp.solutions.drawing_utils.draw_landmarks(
        image, results.pose_landmarks, mp.solutions.holistic.POSE_CONNECTIONS,
        mp.solutions.drawing_utils.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
        mp.solutions.drawing_utils.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
    )
    