import cv2
import numpy as np
raw_data = ''
with open('compare.csv','r') as f:
    raw_data = f.read()
range_extend_x = 25
range_extend_y = 25
lines = raw_data.split('\n')
lines = [line for line in lines if line !='']
for line in lines:
    words = line.split(',')
    file_name =  words[0]
    x_min =  int(words[1])
    y_min =  int(words[2])
    x_max =  int(words[3])
    y_max =  int(words[4])
    file_name = file_name.replace('./datadu/','')
    if file_name=='snapshot_640_480_2.jpg':
        img = cv2.imread(file_name)
        cropped_img = img[max(0,y_min-range_extend_y):min(480,y_max+range_extend_y), max(x_min-range_extend_x,0):min(x_max+range_extend_x, 640)]
        image_obj = cropped_img
        gray = cv2.cvtColor(image_obj, cv2.COLOR_BGR2GRAY)

        kernel = np.ones((4, 4), np.uint8)
        dilation = cv2.dilate(gray, kernel, iterations=1)

        blur = cv2.GaussianBlur(dilation, (5, 5), 0)


        thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

        # Now finding Contours         ###################
        contours = cv2.findContours(
            thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        coordinates = []
        for cnt in contours:
            
            [point_x, point_y, width, height] = cv2.boundingRect(cnt)
            approx = cv2.approxPolyDP(       cnt, 0.07 * cv2.arcLength(cnt, True), True)
            print('asfasfasfasf')
            if len(approx) == 3:
                coordinates.append([cnt])
                cv2.drawContours(image_obj, [cnt], 0, (0, 0, 255), 3)
            
         
        cv2.imshow('as,i',thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




        break