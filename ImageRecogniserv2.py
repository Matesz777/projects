import cv2
import numpy as np
import tensorflow as tf

#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier("C:/Users/matiq/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml")

emotion_model = tf.keras.models.load_model('E:\python\pythonProject\ProjektyNaStudia\models\emotion_detection_model.h5')

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def detectEmotions(img_path):
    try:
        image = cv2.imread(img_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face = gray_image[y:y+h, x:x+w]
            face = cv2.resize(face, (48, 48))
            face = face.astype('float32') / 255.0
            face = np.expand_dims(face, 0)
            face = np.expand_dims(face, -1)

            emotion_predict = emotion_model.predict(face)
            max_index = np.argmax(emotion_predict[0])
            emotion = emotion_labels[max_index]

            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(image, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow('Emotion Detected: ', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("An error accurred: ", e)


path = input("Podaj sciezke do obrazu: ")
detectEmotions(path)

