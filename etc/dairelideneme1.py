import numpy as np
import cv2
import math
import pyautogui
import time

capture=cv2.VideoCapture(0)
#capture.open(0)

while capture.isOpened():
      ret,frame=capture.read()

      #cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)
      #cv2.rectangle(frame,(70,0),(570,400),(0,255,0),3)  # Belirtilen noktalar arasini dikdortgen icine alir
      font=cv2.FONT_HERSHEY_SIMPLEX
      #crop_image=frame[0:400,70:570]  #y,x olarak goruntuyu keser
      

      blur=cv2.GaussianBlur(frame,(7,7),0)
      hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

      #mask2=cv2.inRange(hsv,np.array([105,60,50]),np.array([130,255,255])) # Renk secimi

      mask2=cv2.inRange(hsv,np.array([45,70,50]),np.array([80,190,255])) # Renk gercek yesil
      #mask2=cv2.inRange(hsv,np.array([70,80,10]),np.array([90,255,255])) # Renk secimi yesil

      kernel = np.ones((5,5)) # 5e5 1lik matris olusturur.

      erosion=cv2.erode(mask2,kernel,iterations=1)  #Matris ile altinda kalan kismi AND islemine tabi tutar.
      dilation=cv2.dilate(erosion,kernel,iterations=2) #Onceki islem sonucunda elde edilen alani daraltir.
      

      #filtered= cv2.GaussianBlur(dilation,(3,3),0)
      filtered= cv2.GaussianBlur(dilation,(9,9),cv2.BORDER_DEFAULT)
      ret,thresh = cv2.threshold(filtered,220,255,cv2.THRESH_BINARY) #240 En beyazi 255 kadar olsun , 190 dan kucukler gozukmesin
      cv2.imshow("Thresholded",thresh)

      #thresh = cv2.bitwise_not(thresh)
      #cv2.imshow('threshbitwisenot',thresh)

      _,contours,hierarchy = cv2.findContours(thresh, 1, 2)
      noktasayisi=0
      a=0
      b=0
      for nokta in contours:
            cnt = nokta
            x,y,w,h = cv2.boundingRect(cnt)
            if(noktasayisi>=1):
                 a=a+x+w
                 b=b+y+h
            area = cv2.contourArea(cnt)
            if(area>250): #250
                (x,y),radius = cv2.minEnclosingCircle(cnt)
                center = (int(x),int(y))
                #centerx=(320,240)
                radius = int(radius)
                cv2.circle(frame,center,radius,(0,255,0),3)
                #cv2.circle(frame,centerx,radius,(255,0,0),3)
                #cv2.circle(frame,center,3,(255,255,0),3)
                #cv2.drawContours(frame, [cnt], 0, (0,0,255), 3)
                noktasayisi=noktasayisi+1

            """  
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(frame,center,radius,(0,255,0),3)
            cv2.circle(frame,center,3,(255,255,0),3)
            cv2.drawContours(frame, [cnt], 0, (0,0,255), 3)
            """

      #image,contours,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) 
      #sayi=len(contours)


      def fareyonfonksiyonu(b,n):                      
            if(b[0]>n[0] and b[1]>n[1]):
                  return "sol.asagi"
            elif(b[0]>n[0] and b[1]<n[1]):
                  return "sol.yukari"
            elif(b[0]<n[0] and b[1]<n[1]):
                  return "sag.yukari"
            elif(b[0]<n[0] and b[1]>n[1]):
                  return "sag.asagi"

      def klavyeyonfonksiyonu(b,n):                      
            if (b[0]<n[0]):
                  return "sag"
            elif (b[1]<n[1]):
                  return "yukari"
            elif (b[1]>n[1]):
                  return "asagi"
            elif (b[0]>n[0]):
                  return "sol"

      try:
                  
            if noktasayisi == 0:
                   cv2.putText(frame,"DURUM: BEKLEMEDE",(75,30),font,1,(0,0,255),2)
            elif noktasayisi == 1:
   
                  cv2.putText(frame,"DURUM: 1",(75,30),font,1,(0,0,255),2)
                  ekranortanokta=(320,240)
                  parmaknokta=(x+w/2,y+h/2)

                  if(fareyonfonksiyonu(parmaknokta,ekranortanokta)=="sol.asagi"):
                        cv2.putText(frame,"sol.asagi",(75,77),font,1,(0,0,255),2)
                        pyautogui.move(-10,10)
                        #time.sleep(0.0005)
                  elif(fareyonfonksiyonu(parmaknokta,ekranortanokta)=="sag.asagi"):
                        cv2.putText(frame,"sag.asagi",(75,77),font,1,(0,0,255),2)
                        pyautogui.move(10,10)
                        #time.sleep(0.0005)
                  elif(fareyonfonksiyonu(parmaknokta,ekranortanokta)=="sag.yukari"):
                        cv2.putText(frame,"sag.yukari",(75,77),font,1,(0,0,255),2)
                        pyautogui.move(10,-10)
                        #time.sleep(0.0005)
                  elif(fareyonfonksiyonu(parmaknokta,ekranortanokta)=="sol.yukari"):
                        cv2.putText(frame,"sol.yukari",(75,77),font,1,(0,0,255),2)
                        pyautogui.move(-10,-10)
                        #time.sleep(0.0005)
            elif noktasayisi==2:
                  cv2.putText(frame,"DURUM: 2 ",(75,30),font,1,(0,0,255),2)
                  time.sleep(0.2)
                  if noktasayisi==2:
                        pyautogui.doubleClick()
                  #ekranortanokta=(320,240)
                  #parmakortanokta=(a/2,b/2)

                  #if(klavyeyonfonksiyonu(parmakortanokta,ekranortanokta)=="sol"):
                   #     cv2.putText(frame,"sol",(75,77),font,1,(0,0,255),2)
                    #    pyautogui.press('left')
                        #time.sleep(0.0005)
                  #elif(klavyeyonfonksiyonu(parmakortanokta,ekranortanokta)=="yukari"):
                   #     cv2.putText(frame,"yukari",(75,77),font,1,(0,0,255),2)
                    #    pyautogui.press('up')
                        #time.sleep(0.0005)
                  #elif(klavyeyonfonksiyonu(parmakortanokta,ekranortanokta)=="asagi"):
                   #     cv2.putText(frame,"asagi",(75,77),font,1,(0,0,255),2)
                    #    pyautogui.press('down')
                        #time.sleep(0.0005)
                  #elif(klavyeyonfonksiyonu(parmakortanokta,ekranortanokta)=="sag"):
                   #     cv2.putText(frame,"sag",(75,77),font,1,(0,0,255),2)
                    #    pyautogui.press('right')
                        #time.sleep(0.0005)

            elif noktasayisi==3:
                  cv2.putText(frame,"DURUM: 3",(75,30),font,1,(0,0,255),2)
                  #time.sleep(2)
                  #if noktasayisi==3:
                      #  pyautogui.doubleClick()

                  ekranortanokta=(320,240)
                  parmakortanokta=(a/2,b/2)

                  #if(klavyeyonfonksiyonu(parmakortanokta,ekranortanokta)=="sol"):
                        #cv2.putText(frame,"sol",(75,77),font,1,(0,0,255),2)
                        #pyautogui.press('left')
                        #time.sleep(0.0005)
                  if(klavyeyonfonksiyonu(parmakortanokta,ekranortanokta)=="yukari"):
                        cv2.putText(frame,"yukari",(75,77),font,1,(0,0,255),2)
                        pyautogui.press('up')
                        #time.sleep(0.0005)
                  elif(klavyeyonfonksiyonu(parmakortanokta,ekranortanokta)=="asagi"):
                        cv2.putText(frame,"asagi",(75,77),font,1,(0,0,255),2)
                        pyautogui.press('down')
                        #time.sleep(0.0005)
                  #elif(klavyeyonfonksiyonu(parmakortanokta,ekranortanokta)=="sag"):
                        #cv2.putText(frame,"sag",(75,77),font,1,(0,0,255),2)
                        #pyautogui.press('right')
                        #time.sleep(0.0005)

            elif noktasayisi==4:
                  cv2.putText(frame,"DURUM: 4",(75,30),font,1,(0,0,255),2)

                  

            elif noktasayisi==5:
                  cv2.putText(frame,"DURUM: 5",(75,30),font,1,(0,0,255),2)
                  #time.sleep(1)
                  #if noktasayisi==0:
                        #pyautogui.doubleClick()
                  
                  #pyautogui.keyUp('up')
                  #pyautogui.keyDown('down')
                  #pyautogui.keyDown('4')
                  #time.sleep(1)
                  #pyautogui.keyUp('down')
                  #pyautogui.keyUp('4')                                                               #
                  #pyautogui.hotkey('altleft','f4')
                  #time.sleep(5)
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
      #cv2.imshow('Contours',all_image)
      

      if cv2.waitKey(1)==ord('q'):
            break
                              
capture.release()
cv2.destroyAllWindows()
                  



"""
                  cv2.circle(frame,ortanokta,3,[0,255,0],3)
                  cv2.circle(frame,ortanoktaframe,3,[255,255,255],3)
                  cv2.line(frame, ortanoktaframe, ortanokta, [255,0,0], 2)
                  cv2.putText(frame, yonfonksiyonu(ortanokta,ortanoktaframe), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0,0,255], 2)
                  """
























































"""
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
"""