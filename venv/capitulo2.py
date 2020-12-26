import cv2
import numpy as np
#cargar la imagen
img = cv2.imread("../recursos/lena.png")
#VAraibales del Kernel es recomendable usar nuemro impares
kernel = np.ones((5,5),np.uint8)

#transformar en escala de Grises
# cvt basicamente convierte la imagen en un color diferente Espacio de clores
#convencion es BGR
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#definimos un efecto de distorcion
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

#mostrar las imagenes
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
#temporizador para la ventana
cv2.waitKey(0)