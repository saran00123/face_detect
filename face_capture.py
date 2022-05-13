from itertools import count

import cv2
video = cv2.VideoCapture(0)
i = 0
test =0
trained_dataset = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while i < 100 :
    success, frame = video.read()

    if success == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = trained_dataset.detectMultiScale(gray_img)
        print(faces)
        for x, y, w, h in faces :
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0),2)
            text_pos = (x, y)
            test =x
            cv2.putText(frame, "%d"%i, text_pos, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            if test >0 :
                cv2.imwrite('cap_images/image%d.jpg'% i, gray_img)
                i += 1
                print(i)
                break
    cv2.imshow("img",frame)
    cv2.waitKey(2)




