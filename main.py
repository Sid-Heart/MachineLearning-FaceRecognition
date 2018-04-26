import face_recognition as face_recognition
from PIL import Image , ImageTk
import time
import Tkinter

inputImage = 'images.jpg' #raw_input()
image = face_recognition.load_image_file(inputImage)
face_locations = face_recognition.face_locations(image)
print face_locations, image.shape
#img = Image.fromarray(image, 'RGB')

def updateImage(canvas):
    for fset in range(len(face_locations)):
        image[face_locations[fset][0]][min(face_locations[fset][1],face_locations[fset][3]):max(face_locations[fset][1],face_locations[fset][3])]=[255,0,0]
        image[face_locations[fset][2]][min(face_locations[fset][1],face_locations[fset][3]):max(face_locations[fset][1],face_locations[fset][3])]=[255,0,0]
        for i in range(min(face_locations[fset][0],face_locations[fset][2]),max(face_locations[fset][0],face_locations[fset][2])):
            image[i][face_locations[fset][1]]=[255,0,0]
            image[i][face_locations[fset][3]]=[255,0,0]
    im = Image.fromarray(image, 'RGB')
    canvas.image = ImageTk.PhotoImage(im)
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')
    canvas.after(1000, updateImage, canvas)
    print("Updating...")

top = Tkinter.Tk()
canvas = Tkinter.Canvas(top,height=image.shape[0], width=image.shape[1])
updateImage(canvas)
canvas.pack()
top.mainloop()

