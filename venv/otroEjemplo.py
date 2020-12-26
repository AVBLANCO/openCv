import cv2
#reconocimiento de los caracteres de la placa
import pytesseract
#ruta de tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#almacenar la placa
placa = []
#cagar la imagen a analizar
image = cv2.imread('../recursos/auto001.jpg')
#image = cv2.imread('../recursos/auto2.png')
#image = cv2.imread('../recursos/descarga8.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#atenuar el ruido
gray = cv2.blur(gray, (3, 3))
#engrozar areas blancas
canny = cv2.Canny(gray, 150, 200)
canny = cv2.dilate(canny, None, iterations=1)
#version vieja de cv2
# _,cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# trabajar con los contornos
cnts, _ = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(image,cnts,-1,(0,255,0),2)
for c in cnts:
    area = cv2.contourArea(c)
    #identificar un rectangulo
    x, y, w, h = cv2.boundingRect(c)
    epsilon = 0.09 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
#condicion de que tenga 4 vertices
    if len(approx) == 4 and area > 9000:
        print('area=', area)
        # cv2.drawContours(image,[approx],0,(0,255,0),3)
        aspect_ratio = float(w) / h
        #2.4
        if aspect_ratio > 2.4:
            placa = gray[y:y + h, x:x + w]
            text = pytesseract.image_to_string(placa, config='--psm 11')
            print('PLACA: ', text)
            cv2.imshow('PLACA', placa)
            cv2.moveWindow('PLACA', 780, 10)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(image, text, (x - 20, y - 10), 1, 2.2, (0, 255, 0), 3)

cv2.imshow('Image', image)
cv2.moveWindow('Image', 45, 10)
#el proceso siga activo hasta precionar una tecla
cv2.waitKey(0)