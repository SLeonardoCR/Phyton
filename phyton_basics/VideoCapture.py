import cv2, time

video = cv2.VideoCapture(0)

a=1

while True:
    a=a+1
    check, frame = video.read()

    print(check)
    print(frame)

    #We wait 3 seconds and then we show the image on a window
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)


    #Wait a key to close the window
    key=cv2.waitKey(17)

    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()