from itertools import count

import cv2
video = cv2.VideoCapture(0)
i = 0
test =0
name = "saran"
while i < 100 :
    success, frame = video.read()

    if success == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.putText(frame, "%d"%i, (0,0), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
        cv2.imwrite('cap_images/'+name+" "+str(i + 1)+".jpg", gray_img)
        #print(name+" "+str (i))
        i += 1
        print(i)
    cv2.imshow("img",frame)
    cv2.waitKey(1)
