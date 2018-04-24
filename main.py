import face_recognition as face_recognition
from skimage import data
from PIL import Image
import StringIO

inputImage = raw_input()
image = face_recognition.load_image_file(inputImage)
face_locations = face_recognition.face_locations(image)
print face_locations, image.shape

for fset in range(len(face_locations)):
    image[face_locations[fset][0]][min(face_locations[fset][1],face_locations[fset][3]):max(face_locations[fset][1],face_locations[fset][3])]=[255,0,0]
    image[face_locations[fset][2]][min(face_locations[fset][1],face_locations[fset][3]):max(face_locations[fset][1],face_locations[fset][3])]=[255,0,0]
    for i in range(min(face_locations[fset][0],face_locations[fset][2]),max(face_locations[fset][0],face_locations[fset][2])):
        image[i][face_locations[fset][1]]=[255,0,0]
        image[i][face_locations[fset][3]]=[255,0,0]

img = Image.fromarray(image, 'RGB')
img.show()