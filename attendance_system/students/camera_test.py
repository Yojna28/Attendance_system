import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam", frame)

    # Press 'q' to close
    if cv2.waitKey(300) & 0xFF == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()