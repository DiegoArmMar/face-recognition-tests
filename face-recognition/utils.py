import cv2

def put_points(photo, face_points):
  for fp in face_points.parts():
    cv2.circle(photo, (fp.x, fp.y), 1, (0,0,255), 1)

def print_photo(photo):
  cv2.imshow("face recognition tests", photo)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

