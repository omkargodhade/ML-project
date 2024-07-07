from subprocess import call
import subprocess
from tkinter import *
import tkinter as t
import webbrowser

root = t.Tk()

root.title('Face Recognition System')
root.geometry('800x500')

l = Label(root,text="Face Recognition System",bg= 'black', fg='white',font= ('times New Roman','30',"bold") ).pack()

l1 = Label(root,text="Step:1 - Add Faces",bg= 'red', fg='white',font= ('times New Roman','10',"bold") ).place( x=50 , y=150)
l1 = Label(root,text="Step:2 - Mark Attendance",bg= 'red', fg='white',font= ('times New Roman','10',"bold") ).place( x=350 , y=100)
l1 = Label(root,text="Step:3 - Open streamlit ",bg= 'red', fg='white',font= ('times New Roman','10',"bold") ).place( x=650 , y=150)



def run(args):
     call(["python" , "C:\\Users\\godha\\OneDrive\\Documents\\FaceRecoginationProject\data\\add_faces.py"])

def r1(args):
     call(["python" , "C:\\Users\\godha\\OneDrive\\Documents\\FaceRecoginationProject\\data\\test.py"])

def r2(args):
    #  call(["python" , "C:\\Users\\godha\\OneDrive\\Documents\\FaceRecoginationProject\\data\\app.py"])
     subprocess.run("streamlit run C:\\Users\\godha\\OneDrive\\Documents\\FaceRecoginationProject\\data\\app.py" )

                
pic1 = PhotoImage(file= "C:\\Users\\godha\\OneDrive\\Pictures\\frc\\face-recognition-concept-vector-23120345.png")
photo = pic1.subsample(5,5)
btn1 = Button(root,image = photo,cursor='hand2',command=lambda:run(photo),borderwidth=0).pack(side=LEFT)


pic2 = PhotoImage(file= "C:\\Users\\godha\\OneDrive\\Pictures\\frc\\OIP.png")
photo1 = pic2.zoom(1,1)
btn1 = Button(root,text= "Attendance",image = photo1,cursor='hand2', command= lambda:r1(photo1),borderwidth=0).pack(side=LEFT,padx=70)

pic3 = PhotoImage(file= "C:\\Users\\godha\\OneDrive\\Pictures\\frc\\database.png")
photo2=  pic3.subsample(7,7)
btn1 = Button(root,text='Go to DataBase',image = photo2,cursor='hand2', command= lambda:r2(photo2),borderwidth=0).pack(side=RIGHT,padx=5)


root.mainloop()