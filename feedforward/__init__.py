# This is an optional package-level initialization file.
# You can include code here that should run when the package is imported.

from .dataset_management import augment_dataset_rotation, delete_files_with_prefix, register_videos, create_folder_if_not_exists, clear_folder
from .drawing import draw_pose_landmarks, draw_frame, prob_viz
from .classification import build_training_data
from .detection import mediapipe_detection, extract_descriptor
from .configs import CAMERA_INDEX

__all__ = [
    'CAMERA_INDEX',
    'augment_dataset_rotation',
    'delete_files_with_prefix',
    'create_folder_if_not_exists',
    'clear_folder',
    'register_videos',
    'draw_pose_landmarks',
    'build_training_data',
    'mediapipe_detection',
    'extract_descriptor',
    'draw_frame',
    'prob_viz'
]
