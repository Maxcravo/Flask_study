import cv2 as cv

def camera_capture():
  cap = cv.VideoCapture(0)
  while True:
    ret, img = cap.read()
    cv.imshow("video", img)
    
    if (cv.waitKey(10) & 0xFF == ord("q")):
      break
 
