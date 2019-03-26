import cv2

color = (0,0,255)
radius = 1
margin = 1

def put_points(photo, face_points):
  for fp in face_points.parts():
    cv2.circle(photo, (fp.x, fp.y), radius, color, margin)

def put_bounding_boxes(photo, detected_faces):
  for face in detected_faces:
    left, top = (int(face.left()), int(face.top()))
    right, bottom = (int(face.right()), int(face.bottom()))
    cv2.rectangle(photo, (left, top), (right, bottom), color, margin)

def print_photo(photo):
  cv2.imshow("face recognition tests", photo)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

