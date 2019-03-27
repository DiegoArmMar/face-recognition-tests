import dlib
import cv2
import numpy as np
from os import path

predictor_path = '../resources/models/shape_predictor_68_face_landmarks.dat'
face_recognition_model_path = '../resources/models/dlib_face_recognition_resnet_model_v1.dat'

face_detector = dlib.get_frontal_face_detector()
points_detector = dlib.shape_predictor(predictor_path)
face_recognition = dlib.face_recognition_model_v1(face_recognition_model_path)

def get_face_descriptor(photo_name, scale=1):
  photo = cv2.imread( path.join('../resources/images', photo_name))
  detected_faces = face_detector(photo, scale)

  if 1 != len(detected_faces):
    return None

  face = detected_faces[0]
  points = points_detector(photo, face)
  face_desciptor = face_recognition.compute_face_descriptor(photo, points)
  face_descriptor_list = [df for df in face_desciptor]
  np_array_face_descriptor = np.asarray(face_descriptor_list, dtype=np.float64)
  np_array_face_descriptor = np_array_face_descriptor[np.newaxis, :]

  return np_array_face_descriptor
