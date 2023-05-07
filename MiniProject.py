from tkinter import*
root=Tk()
root.title("Mini Project")
root.geometry("700x500")
root["bg"]="White"

frame1=Frame(root,bg="#4682b4")
frame1.grid(row=0,column=0) 

frame_name=Label(frame1,text="Frame 1",bg="#4682b4",width=50)
frame_name.grid(pady=10)

frame2=Frame(root,bg="#9c6b1d")
frame2.grid(row=1,column=0)

frame2_name=Label(frame2,text="Dealers Score",bg="#9c6b1d",width=50)
frame2_name.grid(pady=20)

frame3=Frame(root,bg="#999999")
frame3.grid(row=1,column=1)

frame3_name=Label(frame3,text="Frame 3",width=50,bg="#999999")
frame3_name.grid(pady=20)

frame4=Frame(root,bg="#ff7f50")
frame4.grid(row=2,column=1)

frame4_name=Label(frame4,text="Frame 4",bg="#ff7f50",width=50)
frame4_name.grid(pady=41)


frame5=Frame(root,bg="#6bc942")
frame5.grid(row=2,column=0)

frame5_name=Label(frame5,text="Actions",width=50,bg="#6bc942")
frame5_name.grid(pady=5)

hit_button=Button(frame5,text="Hit",width=20,bg="#4682b4")
hit_button.grid(padx=5,pady=5)

stand_button=Button(frame5,text="Stand",width=20,bg="Grey")
stand_button.grid(padx=5,pady=5)




root.mainloop()