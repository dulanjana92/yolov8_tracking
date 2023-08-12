# Mikel Broström 🔥 Yolo Tracking 🧾 AGPL-3.0 license

def get_yolo_inferer():    
    # ultralytics already installed when running track.py
    from .yolov8 import Yolov8Strategy
    return Yolov8Strategy
    