import cv2
import mediapipe as mp

def main():
    #captura o video pela webcam
    

    cap = cv2.VideoCapture(0)

    while True:
        _, imagem = cap.read()

        cv2.imshow('Captura', imagem)

        cv2.waitKey(1)

if __name__ == "__main__":
    main()