import cv2

def run_camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Press Q to close camera", frame)

        # wait 1 ms and check key
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

        cap.release()
        cv2.destroyAllWindows()