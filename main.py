import face_recognition as face_recognition
from PIL import Image , ImageTk
import Tkinter
import cv2

videoCApture = cv2.VideoCapture(0)

#print "Enter The Unknown Image To Mark "
inputImage = "obama.jpg"#raw_input()
image = face_recognition.load_image_file(inputImage)
#face_locations = face_recognition.face_locations(image)
#print face_locations, image.shape
#img = Image.fromarray(image, 'RGB')

print "Enter File NAme of Known People (Single Line Seperated By Spaces)"
knownImages = raw_input().split(' ')
print "Enter Original NAme OF Unknown Peoples (Single Line Seperated By Spaces)"
knownNames =raw_input().split(' ')
knownImagesPreEncoded = []

#Logging Known NAmes, FIles Of People
print knownNames," And ",knownImages

#Create Encoding For All The Known Images
for knownImage in knownImages:
    tempImageBinary = face_recognition.load_image_file(knownImage)
    image2Learn =(face_recognition.face_encodings(tempImageBinary))
    if(len(image2Learn)!=1):
        if image2Learn == 0:
            print ("Unable To Recogonize Image", knownImage, "COntains",len(image2Learn), "FAces")  #Some Error Checking To MAke Recogonition Correct
            exit()
        else:
            print ("MAke SUre There is JUst One FAce", knownImage, "COntains",len(image2Learn), "FAces")  #Some Error Checking To MAke Recogonition Correct
            exit()
    knownImagesPreEncoded.append((face_recognition.face_encodings(tempImageBinary))[0])

#Filenames Are Useless To Keep Track Of
del knownImages


def updateImage(root,canvas):
    #Get the Image From VIdeo Camera
    ret, frame = videoCApture.read()
    #Scale It DOwn For Speed
    small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
    #set this Image as MAin  IMage
    image = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    #identify Image
    face_locations = face_recognition.face_locations(image)
    #convert JUst the Detected PArt As New Image
    face_encodings = face_recognition.face_encodings(image, face_locations)
    #Store the Recogonised TAg in this Temp Of NAmes
    tempReco = []

    for i in range(len(face_encodings)):
        peopleBools = face_recognition.compare_faces(knownImagesPreEncoded, face_encodings[i])
        tempReco.append("Unknown")
        print peopleBools
        for j in range(len(peopleBools)):
            if peopleBools[j] and tempReco[i]=="Unknown":
                tempReco[i]=knownNames[j]
            elif peopleBools[j]:
                tempReco[i]=tempReco[i] + " OR " + knownNames[j]


    #Create Boxes And Text ..... GUI PArt ......
    for fset in range(len(face_locations)):
        image[face_locations[fset][0]][min(face_locations[fset][1],face_locations[fset][3]):max(face_locations[fset][1],face_locations[fset][3])]=[255,0,0]
        image[face_locations[fset][2]][min(face_locations[fset][1],face_locations[fset][3]):max(face_locations[fset][1],face_locations[fset][3])]=[255,0,0]
        for i in range(min(face_locations[fset][0],face_locations[fset][2]),max(face_locations[fset][0],face_locations[fset][2])):
            image[i][face_locations[fset][1]]=[255,0,0]
            image[i][face_locations[fset][3]]=[255,0,0]
    im = Image.fromarray(image, 'RGB')
    canvas.image = ImageTk.PhotoImage(im)
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')
    for fset in range(len(face_locations)):
        canvas.create_text((face_locations[fset][1]+face_locations[fset][3])/2,min(face_locations[fset][0],face_locations[fset][2]),fill="white",font="Times 20 italic bold",text=tempReco[fset])
    #............................................
    #CApture New Image As Soonn AS the Processing Finishes
    canvas.after(1, updateImage, root,canvas)
    print("Updating...")

#Create A WIndow
top = Tkinter.Tk()
#Add CAnvas To Window To DIsplay RGB Image
canvas = Tkinter.Canvas(top,height=image.shape[1], width=image.shape[0])
#Update CAnvas As Fast As Possible
updateImage( top,canvas)
#Pack CAnvas
canvas.pack()
#LIsten For Evwnts
top.mainloop()

#Release Video Permission
videoCApture.release()