import cv2
first_frame=None
face_cascade=cv2.CascadeClassifier("face.xml")
eye_cascade=cv2.CascadeClassifier("eye.xml")


video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,2,3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
               
    

    if first_frame is None:
        first_frame=gray
        continue
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(30)&0xff

    if key==27:
         break


video.release()
cv2.destroyAllWindows

    

