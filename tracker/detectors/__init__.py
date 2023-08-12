# Mikel Broström 🔥 Yolo Tracking 🧾 AGPL-3.0 license
from boxmot.utils.checks import TestRequirements

tr = TestRequirements()
def get_yolo_inferer():    
    # ultralytics already installed when running track.py
    from .yolov8 import Yolov8Strategy
    return Yolov8Strategy
    