from tkinter import Tk, Canvas, PhotoImage, Text, Scrollbar, Frame, END, Button
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText
from PIL import Image, ImageTk
from pathlib import Path
import time
import tkinter as tk


# def apply_font(widget, font_path, size):
#     custom_font = Font(family="Inter Medium", size=size)
#     widget.configure(font=custom_font)

# Dictionary to store references to the images
image_references = {}

def show_logo_frame(root):
    global image_references
    # ASSETS_PATH = Path(r"/home/pi/capstone/pill-identification/output/frame1/build/assets/frame0")
    ASSETS_PATH =  Path(r"E:\pill-identification\output\frame1\build\assets\frame0")

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

    # canvas.create_text(
    #     276.0,
    #     389.0,
    #     anchor="nw",
    #     text="press the screen to start",
    #     fill="#9C9C9C",
    #     font=("InriaSans BoldItalic", 24)
    # )

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_references["image_1"] = image_image_1
    image_1 = canvas.create_image(
        400.0,
        223.0,
        image=image_image_1
    )
    root.resizable(False, False)
    root.overrideredirect(True)
    
    # exit_image = tk.PhotoImage(file='/home/pi/capstone/pill-identification/image.jpg')
    exit_button = tk.Button(root, borderwidth=0, command=root.destroy)
    exit_button.place(rely=0.01, relx=0.95)


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
        text="Insert the pill into the \n designated pill slot, \n   ensuring proper \n         alignment.",
        fill="#000000",
        font=("Inter Medium", 40)
    )
    
    canvas.create_text(
        60.0,
        20.0,
        anchor="nw",
        text="23:01",
        fill="#EDF5FA",
        font=("InriaSans", 30)
    )
    root.resizable(False, False)
    root.overrideredirect(True)
    
    # exit_image = tk.PhotoImage(file='/home/pi/capstone/pill-identification/image.jpg')
    exit_button = tk.Button(root, borderwidth=0, command=root.destroy)
    exit_button.place(rely=0.01, relx=0.95)

def show_image_capture_frame(root):
    global image_references
    # ASSETS_PATH = "/home/pi/capstone/pill-identification/output/frame2/build/assets/frame0"
    ASSETS_PATH = r"E:\pill-identification\output\frame2\build\assets\frame0"

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
        fill="#000000",
        font=("Inter Medium", 40)
    )

    canvas.create_text(
        60.0,
        20.0,
        anchor="nw",
        text="23:01",
        fill="#EDF5FA",
        font=("InriaSans", 30)
    )
    root.resizable(False, False)
    root.overrideredirect(True)
    
    # exit_image = tk.PhotoImage(file='/home/pi/capstone/pill-identification/image.jpg')
    exit_button = tk.Button(root, borderwidth=0, command=root.destroy)
    exit_button.place(rely=0.01, relx=0.95)

pill_info_widget_ctr = 0
def show_pill_information_frame(root, pill_info):
    global pill_info_widget_ctr
    global image_references
    # ASSETS_PATH = Path(r"/home/pi/capstone/pill-identification/output/frame3/build/assets/frame0")
    ASSETS_PATH = Path(r"E:\pill-identification\output\frame5\build\assets\frame0")

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
    
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_references["image_1"] = image_image_1
    image_1 = canvas.create_image(
        400.0,
        228.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=564.0,
        y=384.0,
        width=54.51066970825195,
        height=53.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=678.0,
        y=388.0,
        width=49.0,
        height=49.0
    )

    # Create label for classification's pill name
    label = tk.Label(
        root, 
        text=pill_info[0], 
        anchor="nw", 
        justify="center", 
        wraplength=400, 
        font=("Koulen", 18), 
        bg="white", 
        fg="#000000"
    )
    
    label.place(
        x=110, 
        y=63
    )

    # Create a widget for classification's pill information 
    pill_info = "Dosage: {}mg\nSpecial Instruction: {}\nPossible side effects: {}\n".format(pill_info[1], pill_info[2], pill_info[3])
    pill_info_widget = Text(
        root, 
        wrap="word", 
        font=("Koulen", 14), 
        width=45, 
        height=7
    )  
    
    pill_info_widget.configure(state='normal')
    pill_info_widget.insert("1.0", pill_info)
    pill_info_widget.configure(state='disabled', highlightthickness=0)
    pill_info_widget.place(x=100, y=155)  # Positioning the text widget at (100, 150)

    # This code assumes root is already defined
    

    # def update_pill_info(pill_info):
    #     global pill_info_widget_ctr
    #     if pill_info_widget_ctr > 0:
    #         pill_info_widget.delete("1.0", END)  # Clear previous content
    #         pill_info_widget = ScrolledText(root, wrap="word", font=("Koulen", 14), width=40, height=6, autohide=True)
    #     else:
    #         pill_info_widget_ctr += 1
    #         pill_info_widget = ScrolledText(root, wrap="word", font=("Koulen", 14), width=40, height=6, autohide=True)
    #     updated_pill_info = "Dosage: {}mg\nSpecial Instruction: {}\nPossible side effects: {}\n".format(pill_info[1], pill_info[2], pill_info[3])
    #     pill_info_widget.insert("1.0", updated_pill_info)
    #     pill_info_widget.place(x=100, y=155)
            
    # update_pill_info(pill_info)


    canvas.create_text(
        60.0,
        20.0,
        anchor="nw",
        text="23:01",
        fill="#EDF5FA",
        font=("InriaSans", 30)
    )
    
    # Load the image using PIL
    # pil_image = Image.open("/home/pi/capstone/pill-identification/image.jpg")  # Replace "your_image_file.jpg" with the path to your image file
    pil_image = Image.open(r"E:\pill-identification\image.jpg")  # Replace "your_image_file.jpg" with the path to your image file
    # Convert PIL image to Tkinter-compatible format
    image = ImageTk.PhotoImage(pil_image)

    # canvas.create_rectangle(
    #     573.0,
    #     221.0,
    #     718.0,
    #     404.0,
    #     fill="#D9D9D9",
    #     outline=""
    # )

    # pil_image = Image.open("/home/pi/capstone/pill-identification/debug.jpg")
    pil_image = Image.open(r"E:\pill-identification\debug.jpg")
    # Resize the image
    new_width = 100
    new_height = 100
    resized_image = pil_image.resize((new_width, new_height))
    image = ImageTk.PhotoImage(resized_image)
    
    canvas.image = image  # Save a reference to prevent garbage collection
    canvas.create_image(
        (573.0 + 728.0) / 2, 
        (221.0 + 415.0) / 2, 
        image=image
    )
    
    root.resizable(False, False)
    root.overrideredirect(True)
    
    # exit_image = tk.PhotoImage(file='/home/pi/capstone/pill-identification/image.jpg')
    exit_button = tk.Button(root, borderwidth=0, command=root.destroy)
    exit_button.place(rely=0.01, relx=0.95)
    

def show_error_frame(root):
    global image_references
    # ASSETS_PATH = Path(r"/home/pi/capstone/pill-identification/output/frame4/build/assets/frame0")
    ASSETS_PATH = Path(r"E:\pill-identification\output\frame4\build\assets\frame0")

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

    canvas.create_text(
        60.0,
        20.0,
        anchor="nw",
        text="23:01",
        fill="#EDF5FA",
        font=("InriaSans", 30)
    )

    canvas.create_text(
        110.0,
        240.0,
        anchor="nw",
        text="Pill cannot be identified.",
        fill="#000000",
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
    
    # exit_image = tk.PhotoImage(file='/home/pi/capstone/pill-identification/image.jpg')
    exit_button = tk.Button(root, borderwidth=0, command=root.destroy)
    exit_button.place(rely=0.01, relx=0.95)

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
    
    pill_info = db.get_pill_info_gui('Trajenta Duo Linagliptin Metformin HCl 1g (Unpacked Side A)')
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
    
