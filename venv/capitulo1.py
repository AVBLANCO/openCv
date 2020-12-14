# importacion del paquete
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
