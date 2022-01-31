from cv2 import cv2
import time


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

""" Using a cam"""

cam = cv2.VideoCapture(0)
# Assigning frame dimensions and improving brightness
cam.set(3, 640)
cam.set(4, 480)
cam.set(10, 100)

img_counter = 0
start_time = 0
while True:
    ret, frame = cam.read()
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    current_time = time.time()
    fps = 1 / (current_time - start_time)
    start_time = current_time

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

        cv2.putText(frame, f"FPS: {int(fps)}", (520, 40), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 255, 0), 3)
        cv2.imshow("Video", frame)

    if cv2.waitKey(10) % 256 == 27:
        print('Escape pressed. Closing the application')
        break
    elif cv2.waitKey(10) % 256 == 32:
        """Press space to save the Detected frame"""
        img_location = f"C:Users/user/Pictures/Camera Roll/ opencv_frame_{img_counter}.png"
        cv2.imwrite(img_location, frame)
        print(f"{img_location} saved")
        img_counter += 1
cam.release()
cv2.destroyAllWindows()