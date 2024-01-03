from PIL import Image
import os

def crop_image(file_path):
    imapge = Image.open(file_path)
    cropped_image = imapge.crop((0, 0, 381, 145))
    cropped_image.save(file_path)
    
directory = "C:/Users/fjdj0/Desktop/positive/9"
for filename in os.listdir(directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        file_path = os.path.join(directory, filename)
        crop_image(file_path)
        