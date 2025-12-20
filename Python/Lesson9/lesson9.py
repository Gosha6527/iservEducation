from tkinter import *
# from PIL import ImageTk, Image

# imgs = {1:Image.open("images/image1.png")
#         2:Image.open("images/image2.png")
#         3:Image.open("images/image3.png")
#         4:Image.open("images/image4.png")}

root = Tk()
root.title("Коитики")
root.geometry("800x720")
root.resizable(width = False, height = True)

canvas = Canvas(width=50, height=50, bg="grey")
canvas.place(relx=0.25, rely=0.1)



# img1 = imgs[1],resize((150,150))
# img1 = ImageTk.PhotoImage(img1) 

# img2 = imgs[2],resize((150,150))
# img2 = ImageTk.PhotoImage(img2) 

# img3 = imgs[3],resize((150,150))
# img3 = ImageTk.PhotoImage(img3)

# img4 = imgs[4],resize((150,150))
# img4 = ImageTk.PhotoImage(img4)

# variant = {1: img1,
#            2: img2,
#            3: img3,
#            4: img4}

# var = IntVar()
# var.set(0)

# b1 = Radiobutton(width = 150, height=150, indicatoron=0, variable=var, value=1, image=img1)
# b1.place(relx=0.1, rely=0.75)


sc1 = Scale(from_ = 50, to=400, length= 400)
sc1.place(relx=0.18, rely=0.1)

sc2 = Scale(from_ = 50, to=400, length= 400, orient="horizontal")
sc2.place(relx=0.25, rely=0.07)










root.mainloop()