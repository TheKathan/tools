import cv2
import config
import picamera
import datetime
import socket
import sys

def detect_faces(image):
    haar_faces = cv2.CascadeClassifier(config.HAAR_FACES)
    detected = haar_faces.detectMultiScale(image, scaleFactor=config.HAAR_SCALE_FACTOR, 
                minNeighbors=config.HAAR_MIN_NEIGHBORS, 
               minSize=config.HAAR_MIN_SIZE, 
                flags=cv2.CASCADE_SCALE_IMAGE)
    
    return detected

if __name__ == "__main__":

    while True:
	count=0
    	image2 = cv2.imread(sys.argv[1])
	image = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

	faces = detect_faces(image)
    	
	if len(faces) != 0:
        	for (x,y,w,h) in faces:
            		now = datetime.datetime.now()
			cv2.imwrite('/home/pi/bin/faces/'+socket.gethostname()+'-face-'+str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'-'+str(now.hour)+'-'+str(now.minute)+'-'+str(now.second)+'-'+str(now.microsecond)+'.jpg', image[y: y + h, x: x + w])
            		count=count+1
        	print count, 'faces where found'   	

	if cv2.waitKey(10) == 27:
            break
