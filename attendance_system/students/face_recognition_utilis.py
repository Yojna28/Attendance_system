import face_recognition
import os
from .models import Student

def load_known_faces():
    known_encodings = []
    known_names = []

    students = Student.objects.all()

    for student in students:
        if student.image:
            image_path = student.image.path
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(student.name)

                return known_encodings, known_names