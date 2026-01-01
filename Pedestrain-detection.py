import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture('vid.mp4')

while cap.isOpened():
 
    ret, image = cap.read()
    print (cap.isOpened())
    if ret:
     
        height, width = image.shape[:2]
        if width > 400:
       
            new_width = 400
            new_height = int((new_width / width) * height)
            image = cv2.resize(image, (new_width, new_height))
        
        (regions, _) = hog.detectMultiScale(image,
                                            winStride=(4, 4),
                                            padding=(4, 4),
                                            scale=1.05)
        
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y),
                          (x + w, y + h), 
                          (0, 255, 0), 2)
        s
        cv2.imshow("Image", image)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
