import os
import shutil

path = input('Enter A Valid Path : ')


directories = ['./Documents', './Audios', './Videos', './Applications', './Compressed', './Images', './Coursera']


document_ext = ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt', '.csv']
audio_ext = ['.mp3', '.wav', '.m4a']
video_ext = ['.mp4', '.avi', '.mov', '.flv']
application_ext = ['.exe', '.msi']
compressed_ext = ['.zip', '.rar', '.gz']
images_ext = ['.jpg', '.jpeg', '.png']


for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)


for filename in os.listdir(path):

    filepath = os.path.join(path, filename)
    
    if filename.startswith("Coursera"):
        shutil.move(filepath, directories[6])

    elif any(filename.endswith(ext) for ext in document_ext):
        shutil.move(filepath, directories[0])

    elif any(filename.endswith(ext) for ext in audio_ext):
        shutil.move(filepath, directories[1])

    elif any(filename.endswith(ext) for ext in video_ext):
        shutil.move(filepath, directories[2])

    elif any(filename.endswith(ext) for ext in application_ext):
        shutil.move(filepath, directories[3])

    elif any(filename.endswith(ext) for ext in compressed_ext):
        shutil.move(filepath, directories[4])

    elif any(filename.endswith(ext) for ext in images_ext):
        shutil.move(filepath, directories[5])

    