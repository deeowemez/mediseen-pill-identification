from tkinter import Tk, Canvas, PhotoImage, Text, Scrollbar, Frame, END, Button
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText
from PIL import Image, ImageDraw, ImageTk
from pathlib import Path
import time
import tkinter as tk
import main

# Dictionary to store references to the images
image_references = {}

def show_logo_frame(root):
    global image_references
    ASSETS_PATH = Path(r"/home/pi/capstone/pill-identification/output/frame1/build/assets/frame0")
    # ASSETS_PATH =  Path(r"E:\pill-identification\output\frame1\build\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    root.configure(bg="#FFFFFF")

    canvas = Canvas(
        root,
        bg="#FFFFFF",
        height=480,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_references["image_1"] = image_image_1
    image_1 = canvas.create_image(
        400.0,
        223.0,
        image=image_image_1
    )
    root.resizable(False, False)
    root.overrideredirect(True)

def show_instructions_frame(root):
    global image_references
    ASSETS_PATH = "/home/pi/capstone/pill-identification/output/frame2/build/assets/frame0"
    # ASSETS_PATH = r"E:\pill-identification\output\frame2\build\assets\frame0"

    def relative_to_assets(path: str) -> str:
        return ASSETS_PATH + "/" + path

    root.configure(bg="#EDF5FA")

    canvas = Canvas(
        root,
        bg="#EDF5FA",
        height=480,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_references["image_1"] = image_image_1
    image_1 = canvas.create_image(
        399.0,
        240.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_references["image_2"] = image_image_2
    image_2 = canvas.create_image(
        714.0,
        381.0,
        image=image_image_2
    )
    
    canvas.create_text(
        160.0,
        160.0,
        anchor="nw",
        text="Insert the pill into the \n designated pill slot, \n   ensuring proper \n         alignment.",
        fill="#212121",
        font=("Inter Medium", 40)
    )
    
    # canvas.create_text(
    #     60.0,
    #     20.0,
    #     anchor="nw",
    #     text="23:01",
    #     fill="#EDF5FA",
    #     font=("InriaSans", 30)
    # )
    root.resizable(False, False)
    root.overrideredirect(True)
    
def show_image_capture_frame(root):
    global image_references
    ASSETS_PATH = "/home/pi/capstone/pill-identification/output/frame2/build/assets/frame0"
    # ASSETS_PATH = r"E:\pill-identification\output\frame2\build\assets\frame0"

    def relative_to_assets(path: str) -> str:
        return ASSETS_PATH + "/" + path

    root.configure(bg="#EDF5FA")

    canvas = Canvas(
        root,
        bg="#EDF5FA",
        height=480,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_references["image_1"] = image_image_1
    image_1 = canvas.create_image(
        415.0,
        240.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_references["image_2"] = image_image_2
    image_2 = canvas.create_image(
        714.0,
        381.0,
        image=image_image_2
    )
    
    canvas.create_text(
        160.0,
        160.0,
        anchor="nw",
        text="Image capture and \n  pill identification \n      in progress",
        fill="#212121",
        font=("Inter Medium", 40)
    )

    # canvas.create_text(
    #     60.0,
    #     20.0,
    #     anchor="nw",
    #     text="23:01",
    #     fill="#EDF5FA",
    #     font=("InriaSans", 30)
    # )
    root.resizable(False, False)
    root.overrideredirect(True)
    

def show_pill_information_frame(root, pill_info):
    global image_references
    ASSETS_PATH = Path(r"/home/pi/capstone/pill-identification/output/frame3/build/assets/frame0")
    # ASSETS_PATH = Path(r"E:\pill-identification\output\frame3\build\assets\frame0")

    
    classification = pill_info[4]
    
    print('in gui show: ', classification)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    def set_widget_location(pill_info):
        print('pill name length: ', len(pill_info[0]))
        if len(pill_info[0]) >= 45:
            widget_y = 105
            widget_height = 10
        else: 
            widget_y = 60
            widget_height = 11
        return widget_y, widget_height
    
    widget_y, widget_height = set_widget_location(pill_info)
    
    
    root.configure(bg="#EDF5FA")

    canvas = Canvas(
        root,
        bg="#EDF5FA",
        height=480,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    
    
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_references["image_1"] = image_image_1
    image_1 = canvas.create_image(
        400.0,
        228.0,
        image=image_image_1
    )
    
    button_image_1 = PhotoImage(
        file=relative_to_assets("reclassify.png"))
    image_references["button_1"] = button_image_1
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: main.simulate_button_press(),
        relief="flat"
    )
    
    button_1.place(
        x=655.0,
        y=378.0,
        width=70.0,
        height=65.0
    )
    
    button_image_2 = PhotoImage(
        file=relative_to_assets("repeat.png"))
    image_references["image_2"] = button_image_2
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: main.repeat_pill_info_audio(classification),
        relief="flat"
    )
    
    button_2.place(
        x=565.0,
        y=378.0,
        width=70.0,
        height=65.0
    )

    # Create label for classification's pill name
    label = tk.Label(
        root, 
        text=pill_info[0], 
        anchor="nw", 
        justify="left", 
        wraplength=400, 
        font=("Koulen", 18), 
        bg="white", 
        # fg="#71b9cb"
        fg="#000000"
    )
    
    label.place(
        x=93, 
        y=10,
    )

    # Create a widget for classification's pill information 
    pill_info = "Dosage: {}mg\nSpecial Instruction: {}\nPossible side effects: {}\n".format(pill_info[1], pill_info[2], pill_info[3])
    pill_info_widget = Text(
        root, 
        wrap="word", 
        font=("Koulen", 14), 
        width=43, 
        height=widget_height,
        fg="#212121"
    )  
    
    pill_info_widget.configure(state='normal')
    pill_info_widget.insert("1.0", pill_info)
    pill_info_widget.configure(state='disabled', highlightthickness=0, padx=4, pady=3)
    pill_info_widget.place(x=90, y=widget_y)  
    
    # Open the image
    pil_image = Image.open("/home/pi/capstone/pill-identification/debug.jpg")

    # Resize the image
    new_width = 170
    new_height = 170
    resized_image = pil_image.resize((new_width, new_height))

    # Create a mask for rounded corners
    mask = Image.new("L", (new_width, new_height), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, new_width, new_height), fill=255, radius=15)

    # Apply the mask to the image
    rounded_image = Image.new("RGBA", (new_width, new_height), 0)
    rounded_image.paste(resized_image, (0, 0), mask)

    # Convert the rounded image to PhotoImage
    rounded_photo = ImageTk.PhotoImage(rounded_image)

    # Display the rounded image on canvas
    canvas.image = rounded_photo  # Save a reference to prevent garbage collection
    canvas.create_image(
        650,
        257,
        image=rounded_photo
    )
    
    root.resizable(False, False)
    root.overrideredirect(True)
    
    # exit_image = tk.PhotoImage(file='/home/pi/capstone/pill-identification/image.jpg')
    exit_button = tk.Button(root, borderwidth=0, command=root.destroy)
    exit_button.place(rely=0.01, relx=0.95)
    

def show_error_frame(root):
    global image_references
    ASSETS_PATH = Path(r"/home/pi/capstone/pill-identification/output/frame4/build/assets/frame0")
    # ASSETS_PATH = Path(r"E:\pill-identification\output\frame4\build\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    root.configure(bg="#EDF5FA")

    canvas = Canvas(
        root,
        bg="#EDF5FA",
        height=480,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_references["image_1"] = image_image_1
    canvas.create_image(
        400.0,
        241.0,
        image=image_image_1
    )

    canvas.create_text(
        240.0,
        150.0,
        anchor="nw",
        text="ERROR!",
        fill="#F30707",
        font=("Inter Bold", 64)
    )

    # canvas.create_text(
    #     60.0,
    #     20.0,
    #     anchor="nw",
    #     text="23:01",
    #     fill="#EDF5FA",
    #     font=("InriaSans", 30)
    # )

    canvas.create_text(
        110.0,
        240.0,
        anchor="nw",
        text="Pill cannot be identified.",
        fill="#212121",
        font=("Inter", 40)
    )

    canvas.create_text(
        230.0,
        370.0,
        anchor="nw",
        text="Please flip the medicine \n         and try again.",
        fill="#EDF5FA",
        font=("Inter", 22)
    )
    root.resizable(False, False)
    root.overrideredirect(True)
    
# Define switch_frame function after the main block
def clear_frame(root, new_frame_func):
    # Clear the current frame
    for widget in root.winfo_children():
        widget.destroy()

    new_frame_func(root)

# Function for initializing GUI
def switch_frames(root, frame_function, delay):
    root.after(delay, lambda: clear_frame(root, frame_function))

def switch_pill_information_frame(root ,delay, pill_info):
    for widget in root.winfo_children():
        widget.destroy()

    show_pill_information_frame(root, pill_info)


if __name__ == "__main__":
    import db
    
    pill_info = db.get_pill_info_gui('RiteMed Glimepiride 2mg (Packed)')
    print(pill_info[0])
    root = Tk()
    root.geometry("800x480")
    
    # root = tb.Window(themename='superhero')
    # root.title('')
    # # root.iconbitmap('/home/pi/capstone/pill-identification/image.jpg')
    # root.geometry('800x480')

    # show_logo_frame(root)
    # show_instructions_frame(root)
    # show_image_capture_frame(root)
    show_pill_information_frame(root, pill_info)
    # show_error_frame(root)
    
    # Start the main loop
    root.mainloop()
    
