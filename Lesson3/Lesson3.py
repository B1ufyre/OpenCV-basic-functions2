import cv2
Pikachu = cv2.imread("Pikachu.png")
"""
ColourChange = cv2.cvtColor(Pikachu, cv2.COLOR_BGR2RGB)
cv2.imshow("Window1", ColourChange)
cv2.waitKey(0)
ColourChange2 = cv2.cvtColor(Pikachu, cv2.COLOR_BGR2HSV)
cv2.imshow("Window2", ColourChange2)
cv2.waitKey(0)
GreyScale = cv2.cvtColor(Pikachu, cv2.COLOR_BGR2GRAY)
cv2.imshow("Window3", GreyScale)
cv2.waitKey(0)
print(Pikachu.shape)
print(Pikachu[274,175])
Pikachu[274, 175] = sum(Pikachu[274, 175]) * 0.33
print(Pikachu[274,175])
for i in range(414):
    for j in range(418):
        Pikachu[i,j] = sum(Pikachu[i,j]) * 0.33
cv2.imshow("Window4", Pikachu)
cv2.waitKey(0)
Rotation = cv2.rotate(Pikachu, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Window5", Rotation)
cv2.waitKey(0)
"""
EdgeDetection = cv2.Canny(Pikachu, 1250, 1529)
cv2.imshow("Window6", EdgeDetection)
cv2.waitKey(0)