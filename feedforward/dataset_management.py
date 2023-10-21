import numpy as np
import cv2
import os
from .configs import CAMERA_INDEX

def clear_folder(path: str) -> None:
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))


def create_folder_if_not_exists(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def delete_files_with_prefix(path: str, prefix: str) -> None:
    for file in os.listdir(path):
        if file.startswith(prefix):
            os.remove(os.path.join(path, file))


def register_videos(data_path: str, prefix: str, num_videos: int, num_frames_per_video: int) -> int:
    cap = cv2.VideoCapture(CAMERA_INDEX)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    for idx_video in range(num_videos):

        video_filename = os.path.join(data_path, f"{prefix}{idx_video}.mp4")
        writer = cv2.VideoWriter(
            video_filename, cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))

        for idx_frame in range(num_frames_per_video):
            ret, frame = cap.read()

            if idx_frame == 0:
                cv2.putText(frame, f'Starting Video #{idx_video+1}', (120, 200),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                cv2.imshow('Video', frame)
                cv2.waitKey(3000)
            else:
                cv2.imshow('Video', frame)

            writer.write(frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        writer.release()

    cap.release()
    cv2.destroyAllWindows()


def apply_random_rotation(image: cv2.typing.MatLike) -> cv2.typing.MatLike:
    angle = np.random.randint(-10, 10)  # degrees
    M = cv2.getRotationMatrix2D(
        (image.shape[1] / 2, image.shape[0] / 2), angle, 1)
    augmented_image = cv2.warpAffine(
        image, M, (image.shape[1], image.shape[0]))
    return augmented_image


def apply_panning(image: cv2.typing.MatLike, direction='left') -> cv2.typing.MatLike:
    if direction == 'left':
        panned_image = np.roll(image, -1, axis=1)
    elif direction == 'right':
        panned_image = np.roll(image, 1, axis=1)
    return panned_image


def augment_dataset_rotation(dataset_path: str, prefix_to_add: str) -> None:
    video_names = os.listdir(dataset_path)

    for idx_video, video_name in enumerate(video_names):
        cap = cv2.VideoCapture(os.path.join(dataset_path, video_name))

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        print(f"Processing video #{idx_video+1} / {len(video_names)}...")

        new_video_path = os.path.join(dataset_path, f"{prefix_to_add}{video_name}")
        writer = cv2.VideoWriter(new_video_path, cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb = apply_random_rotation(frame_rgb)

            writer.write(frame_rgb)

        writer.release()

        cap.release()

