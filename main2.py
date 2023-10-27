import tkinter as tk

root = tk.Tk()

# Create a PhotoImage object from the image file.
background_image = tk.PhotoImage(file="delete.png")

# Set the background property of the Tk widget to the PhotoImage object.
root.config(bg=background_image)

root.mainloop()
