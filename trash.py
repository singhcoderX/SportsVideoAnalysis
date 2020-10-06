import cv2
import numpy as np
import matplotlib.pyplot as plt
def getCoordinateFromPerspectiveTransform(p,matrix):
    px = (matrix[0][0]*p[0] + matrix[0][1]*p[1] + matrix[0][2]) / ((matrix[2][0]*p[0] + matrix[2][1]*p[1] + matrix[2][2]))
    py = (matrix[1][0]*p[0] + matrix[1][1]*p[1] + matrix[1][2]) / ((matrix[2][0]*p[0] + matrix[2][1]*p[1] + matrix[2][2]))
    p_after = (int(px), int(py))
    return p_after
left_img = cv2.imread("left.jpg")#field image frame input
left_field = cv2.imread("left_field.jpg")#output image
p1 = (678,384)
cv2.circle(left_img,p1,5,(0,0,255),cv2.FILLED)

cv2.imwrite("modifiedLeft.jpg",left_img)
width,height ,a= left_img.shape
print("width=",width,"height=",height)
pts = np.float32([[51,303],[818,159],[1025,957],[1277,208]])#points marked for image perspective
pts1 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts,pts1)

p = (678,384) # your original point
p_after = getCoordinateFromPerspectiveTransform(p,matrix) #this is the coordinate
print(p_after)
cv2.circle(left_field,p_after,10,(0,0,255),cv2.FILLED)
cv2.imwrite("Left_fieldd.jpg",left_field)
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