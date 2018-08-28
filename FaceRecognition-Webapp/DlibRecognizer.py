import cv2
import numpy as np
import dlib


class DlibRecognizer():
    def __init__(self, prediction_model_path = 'data/shape_predictor_5_face_landmarks.dat', recognition_model_path ='data/dlib_face_recognition_resnet_model_v1.dat'):
        self.known_faces = dict()
        self.predictor = dlib.shape_predictor(prediction_model_path)
        self.recognizer = dlib.face_recognition_model_v1(recognition_model_path)

    def enroll(self, imageBuffer, name):
        vec = self._face2vec(imageBuffer)
        self.known_faces[name] = vec

    def recognize(self, imageBuffer):
        vec = self._face2vec(imageBuffer)
        best_match_name = 'unknown'
        best_match_score = 0.36
        for name, descriptor in self.known_faces.items():
            # code goes here
            best_match_name = 'unknown'
            
        return best_match_name

    def _face2vec(self, imageBuffer):
        dataFromBuffer = np.frombuffer(imageBuffer, dtype=np.uint8)
        image = cv2.imdecode(dataFromBuffer, cv2.IMREAD_COLOR)

        faceDetection = dlib.rectangles()
        faceDetection.append(dlib.rectangle(5,5,image.shape[0]-5, image.shape[1]-5))
        faceLMDetection = self.predictor(image,faceDetection[0])
        vec = self.recognizer.compute_face_descriptor(image,faceLMDetection)
        
        return vec
