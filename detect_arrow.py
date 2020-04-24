import cv2
import imutils
import numpy as np
import os
raw_data = ''
with open('compare.csv','r') as f:
    raw_data = f.read()
range_extend_x = 25
range_extend_y = 25
lines = raw_data.split('\n')
lines = [line for line in lines if line !='']
count =0
for line in lines:
    words = line.split(',')
    file_name =  words[0]
    x_min =  int(words[1])
    y_min =  int(words[2])
    x_max =  int(words[3])
    y_max =  int(words[4])
    file_name = file_name.replace('./datadu/','')
    
    img = cv2.imread(file_name)
    cropped_img = img[max(0,y_min-range_extend_y):min(480,y_max+range_extend_y), max(x_min-range_extend_x,0):min(x_max+range_extend_x, 640)]
    image_obj = cropped_img
    gray = cv2.cvtColor(image_obj, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (1, 1), 0)
    thresh = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY)[1]
    
    thresh =np.bitwise_not(thresh)
    # cv2.imshow('a', thresh)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



    cnts = cv2.findContours(thresh.copy(), cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for cnt in cnts:
        approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
        if len(approx) == 3:
            cv2.drawContours(cropped_img, [cnt], -1, (0, 255, 0), 2)
            
        
        
    cv2.imwrite(str(count)+'.jpg',cropped_img)
    count+=1
    # if count==5:
    #     break