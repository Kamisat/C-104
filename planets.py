import cv2

img = cv2.imread("solar-system.jpg")



cv2.putText(img, "Sun", (90, 100), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0,255,255))

cv2.putText(img, "Mercury", (120, 170), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))

cv2.putText(img, "Venus", (200, 170), cv2.FONT_HERSHEY_COMPLEX, 0.4, (40,255,255))

cv2.putText(img, "Earth", (280, 170), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255,0))

cv2.putText(img, "Mars", (390, 175), cv2.FONT_HERSHEY_COMPLEX, 0.4, (80,255,255))

cv2.putText(img, "Jupiter", (520, 70), cv2.FONT_HERSHEY_COMPLEX, 0.4, (240,255,255))

cv2.putText(img, "Saturn", (770, 120), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,255,255))

cv2.putText(img, "Uranus", (970, 120), cv2.FONT_HERSHEY_COMPLEX, 0.4, (100,255,100))

cv2.putText(img, "Neptune", (1120, 130), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,100,100))

cv2.imwrite("planets_names.jpg",img)



cv2.imshow("Imagem", img)
cv2.waitKey(0)

