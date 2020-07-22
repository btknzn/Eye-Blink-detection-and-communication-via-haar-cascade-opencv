import numpy as np
import cv2
import time


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
counter = 0
now =0
timecounter = 0
passcyclee=0
reachtime = time.time()
systemTupel=("","elma","armut","çilek","muz","ananas","nar","uzum","seftali","kayısı","kiraz","")
cv2.destroyAllWindows()
impulse=0
while 1:
    if counter ==11:
        counter=1
        timecounter=int(time.time())
        reachtime=timecounter+10
        
    now = int(time.time())      
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    if (np.size(faces)==0):
        roi_gray=gray
        roi_color=img
        
    eyes = eye_cascade.detectMultiScale(roi_gray)
                        
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    time.sleep(0.01)   
    if (counter==0 and np.size(eyes)<4):
        timecounter = int(time.time())
        reachtime = timecounter+10
    if (np.size(eyes)<4):
        time.sleep(0.1)
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if(np.size(eyes)<4 and impulse==1):
            counter=counter+1
            impulse=0
    if(np.size(eyes)>4):
        impulse=1
        
    if (now>reachtime):
        print(systemTupel[counter])
        counter=0
        timecounter=int(time.time())
        reachtime=timecounter+10
        time.sleep(4)
    
    print("kalan süre" +str(round(reachtime-now)))
    print(counter)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()




