import cv2

#############################################
#Definimos variables estaticas
#tamaño de la ventana
frameWidth = 640
frameHeight = 480
#archivo que permte crear la mascara o filtro para las placas
nPlateCascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_russian_plate_number.xml")
print(nPlateCascade)
#area minima del rectangulo que se define para faciliar el reconomcimeot de la placa
minArea = 200
#varaible color del texto
color = (255,0,255)
###############################################

#si es una imagen
#cap=cv2.imread("../recursos/descarga8.jpg")
###############################################
cap = cv2.VideoCapture("recursos/video12.mp4")

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
 #   watches = watch_cascade.detectMultiScale(image_gray, en_scale, 2, minSize=(36, 9), maxSize=(36 * 40, 9 * 40))
    for (x, y, w, h) in numberPlates:
        area = w*h
        # una vez identificado el ectangulo
        if area >minArea:
           #crear una tiqueta o caputra de la placa
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
           #nos llevamos la imagen de la placa despues de capturarla y la almacenamos en una ventana como resultado
            cv2.putText(img,"Placa",(x,y-5),
                        #configuracion parametros de la ventana tamaño y color de la letra
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Resultado", img)

#metodo para almacenar la placa que hemos identificado
    #comando podemos activaar la grabacion del proyecto
    if cv2.waitKey(1) & 0xFF == ord('s'):
        #crear el carchivo el cual va a estar almacenado en esa ruta y va a tener un contador de nombre
        cv2.imwrite("recursos/Scanned/NoPlate_"+str(count)+".jpg",imgRoi)
        #determina las dimensiones
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        #varaibles en la ventada de salida
        cv2.putText(img,"Restulado Almacenado",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Resultado",img)
        cv2.waitKey(500)
        count +=1