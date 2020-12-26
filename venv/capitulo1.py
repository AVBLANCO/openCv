######################## LEER IMAGEN ############################

 #importacion del paquete

 import cv2

#prueba para corroborar la importacion adecuada del los paquetes importados

 print ("packege  imported")

#cargamos una imagen usando imread
# esta imagen esta almacenda en el directorio de nuestro proyecto en la carpeta recursos

 img=cv2.imread("../recursos/lena.png")

#usamos el comando imshow para mostrala

cv2.imshow("Output",img)

# waitKey(0)mostrará la ventana infinitamente hasta que se presione cualquier tecla
# (es adecuada para la visualización de imágenes).

 cv2.waitKey(0)


######################### READ VIDEO #############################

#import cv2

#cap = cv2.VideoCapture("recursos/test_video.mp4")
#print(cap)
#while True:
#    success, img =cap.read()
#    cv2.imshow("Video Salida",img)
#    if cv2.waitKey(1)& 0xFF ==ord('q'):
#        break


######################### LEER VIDEO  2  #############################

#import cv2
#frameWidth = 640
#frameHeight = 480
#dim=(frameWidth,frameHeight)
#cap = cv2.VideoCapture("recursos/test_video.mp4")
#print(cap)
#while True:
  #  success, img =cap.read()
#    img = cv2.resize(img, (frameWidth, frameHeight))
 #   img = cv2.resize(img,dim)
#    cv2.rectangle(img, (100, 100), (200, 200), [255, 0, 0], 2)
 #   cv2.imshow("Video Salida",img)
 #   if cv2.waitKey(1)& 0xFF ==ord('q'):
 #       break



######################### READ WEBCAM  ############################
#import cv2
#frameWidth = 640
#frameHeight = 480
#cap = cv2.VideoCapture(0)
#cap.set(3, frameWidth)
#cap.set(4, frameHeight)
#cap.set(10,150)
#while True:
#    success, img = cap.read()
#    cv2.imshow("Result", img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break