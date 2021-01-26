import numpy as np
import cv2
import math
import pyautogui
import time

capture=cv2.VideoCapture(0)

while capture.isOpened():
      ret,frame=capture.read()

      #cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)
      cv2.rectangle(frame,(70,0),(570,400),(0,255,0),3)  # Belirtilen noktalar arasini dikdortgen icine alir
      font=cv2.FONT_HERSHEY_SIMPLEX
      crop_image=frame[0:400,70:570]  #y,x olarak goruntuyu keser
      

      blur=cv2.GaussianBlur(crop_image,(3,3),0)
      hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

      #mask2=cv2.inRange(hsv,np.array([105,60,50]),np.array([130,255,255])) # Renk secimi

      #mask2=cv2.inRange(hsv,np.array([110,20,50]),np.array([130,255,255])) # Renk secimi
      mask2=cv2.inRange(hsv,np.array([70,70,10]),np.array([90,255,255])) # Renk secimi yesil

      kernel = np.ones((3,3)) # 5e5 1lik matris olusturur.

      erosion=cv2.erode(mask2,kernel,iterations=1)  #Matris ile altinda kalan kismi AND islemine tabi tutar.
      dilation=cv2.dilate(erosion,kernel,iterations=3) #Onceki islem sonucunda elde edilen alani daraltir.
      

      filtered= cv2.GaussianBlur(dilation,(3,3),0)
      ret,thresh = cv2.threshold(filtered,170,255,cv2.THRESH_BINARY) #En beyazi 255 kadar olsun , 190 dan kucukler gozukmesin


      cv2.imshow("Thresholded",thresh)

      image,contours,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     
      drawing=np.zeros(crop_image.shape,np.uint8)

      def yonfonksiyonu(b,n):                                                       #
            if(b[0]>n[0] and b[1]>n[1]):
                  return "sol.asagi"
            elif(b[0]>n[0] and b[1]<n[1]):
                  return "sol.yukari"
            elif(b[0]<n[0] and b[1]<n[1]):
                  return "sag.yukari"
            elif(b[0]<n[0] and b[1]>n[1]):
                  return "sag.asagi"
      try:
            contour = max(contours,key=lambda x:cv2.contourArea(x))

            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(crop_image,(x,y),(x+w,y+h),(0,0,255),3)

            kosegenmesafe=w+h                                                       #
            ortanokta=(x+w/2+65,y+h/2)
            ortanoktaframe=(320,240)

            hull=cv2.convexHull(contour)
            
            cv2.drawContours(drawing,[contour],-1,(0,255,0),0)
            cv2.drawContours(drawing,[hull],-1,(0,255,0),0)

           # hull=cv2.convexHull(contour,returnPoints=False)
            defects = cv2.convexityDefects(contour,hull)

            count_defects=0

            for i in range(defects.shape[0]):
                  s, e, f, d = defects[i, 0]
                  start = tuple(contour[s][0])
                  end = tuple(contour[e][0])
                  far = tuple(contour[f][0])

                  a = math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)
                  b = math.sqrt((far[0]-start[0])**2 + (far[1]-start[1])**2)
                  c = math.sqrt((end[0]-far[0])**2 + (end[1]-far[1])**2)
                  angle=(math.acos((b**2 + c**2 - a ** 2) / (2*b*c))*180) /3.14

                  if angle >=160:
                        count_defects +=1
                        cv2.circle(crop_image,far,1,[0,0,255],-1)
                  cv2.line(crop_image,start,end,[0,255,0],2)

            if count_defects ==0:
                   cv2.putText(frame,"1",(75,30),font,1,(0,0,255),2)

            elif count_defects==1:
                  cv2.putText(frame,"FARE IMLEC KONTROLU ",(75,30),font,1,(0,0,255),2)

                  cv2.circle(frame,ortanokta,3,[0,255,0],3)
                  cv2.circle(frame,ortanoktaframe,3,[255,255,255],3)
                  cv2.line(frame, ortanoktaframe, ortanokta, [255,0,0], 2)
                  cv2.putText(frame, yonfonksiyonu(ortanokta,ortanoktaframe), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0,0,255], 2)

                  if(yonfonksiyonu(ortanokta,ortanoktaframe)=="sol.asagi"):
                        pyautogui.move(-20,20)
                        time.sleep(0.05)
                  elif(yonfonksiyonu(ortanokta,ortanoktaframe)=="sag.asagi"):
                        pyautogui.move(20,20)
                        time.sleep(0.05)
                  elif(yonfonksiyonu(ortanokta,ortanoktaframe)=="sag.yukari"):
                        pyautogui.move(20,-20)
                        time.sleep(0.05)
                  elif(yonfonksiyonu(ortanokta,ortanoktaframe)=="sol.yukari"):
                        pyautogui.move(-20,-20)
                        time.sleep(0.05)

            elif count_defects==2:
                  cv2.putText(frame,"FARE SOL TIK",(50,50),font,2,(0,0,255),2)
                  pyautogui.click()

            elif count_defects==3:
                  cv2.putText(frame,"FARE SAG TIK",(50,50),font,2,(0,0,255),2)
                  pyautogui.click(button='right')

            elif count_defects>3:
                  cv2.putText(frame,"DORT",(50,50),font,2,(0,0,255),2)
                  #pyautogui.keyUp('up')
                  #pyautogui.keyDown('down')
                  #pyautogui.keyDown('4')
                  #time.sleep(1)
                  #pyautogui.keyUp('down')
                  #pyautogui.keyUp('4')                                                               #
                  pyautogui.hotkey('altleft','f4')
                  time.sleep(5)
            else:
                  pass
      except:
            pass

      #cv2.imshow('Gesture',frame)
      
      
      #cv2.imshow('Gaussian1',blur)
      #cv2.imshow('Dilation',dilation)
      #cv2.imshow('Erosion',erosion)
      #cv2.imshow('Gaussian2',filtered)
      cv2.imshow('ori',frame)
      all_image = np.hstack((drawing,crop_image))
      cv2.imshow('Contours',all_image)

      if cv2.waitKey(1)==ord('q'):
            break
                              
capture.release()
cv2.destroyAllWindows()
                  
