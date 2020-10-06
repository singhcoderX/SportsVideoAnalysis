import cv2
import numpy as np
import matplotlib.pyplot as plt
def getCoordinateFromPerspectiveTransform(p,matrix):
    px = (matrix[0][0]*p[0] + matrix[0][1]*p[1] + matrix[0][2]) / ((matrix[2][0]*p[0] + matrix[2][1]*p[1] + matrix[2][2]))
    py = (matrix[1][0]*p[0] + matrix[1][1]*p[1] + matrix[1][2]) / ((matrix[2][0]*p[0] + matrix[2][1]*p[1] + matrix[2][2]))
    p_after = (int(px), int(py))
    return p_after

left_img = cv2.imread("left.jpg")       #input left image of player input image
left_field = cv2.imread("left_field.jpg")       # Field output mask
p1 = (678,384)              # (x,y) of the player detected
# p2 = (561,302)
# p3 = (675,319)
# p4 = (931,233)
cv2.circle(left_img,p1,5,(0,0,255),cv2.FILLED)
# cv2.circle(left_img,p2,5,(0,255,0),cv2.FILLED)
# cv2.circle(left_img,p3,5,(255,0,0),cv2.FILLED)
# cv2.circle(left_img,p1,5,(255,0,255),cv2.FILLED)
# person_points = []
# person_points.append(list(p1))
# person_points.append(list(p2))
# person_points.append(list(p3))
# person_points.append(list(p4))
# print(person_points)
# cv2.imwrite("modifiedLeft.jpg",left_img)
width,height ,a= left_img.shape            # width and height of input image
print("width=",width,"height=",height)
pts = np.float32([[51,303],[818,159],[1025,957],[1277,208]])  #manually find out 4 corners in left image
pts1 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # respective point mapping in transformation 
matrix = cv2.getPerspectiveTransform(pts,pts1)  #see arguments

p = (678,384) # your original point
p_after = getCoordinateFromPerspectiveTransform(p,matrix) #this is the coordinate
print(p_after)
cv2.circle(left_field,p_after,10,(0,0,255),cv2.FILLED)    #it will make a circle on field map directly
cv2.imwrite("Left_fieldd.jpg",left_field)           #print output image with location of player marked
# result  =[[0,0] for x in range(0,4)]
# print(result)
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]
result = cv2.warpPerspective(left_img,matrix,(width,height))
cv2.imwrite('leffft.jpg',result)
# cv2.imshow("result",result)
# cv2.waitKey(0)