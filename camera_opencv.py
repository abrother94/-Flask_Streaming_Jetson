import os
import cv2
from base_camera import BaseCamera
from datetime import datetime


class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')


        while True:
            # read current frame
            # get current DateTime
            font = cv2.FONT_HERSHEY_SIMPLEX
            _, img = camera.read()
            cv2.putText(img,str(datetime.now()),(240,475), font, .5,(2,5,5),2,cv2.LINE_AA)

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
