from tkinter import Tk, Canvas, PhotoImage, Text, Scrollbar
from pathlib import Path
import time
import tkinter as tk
from tkinter.font import Font

# def apply_font(widget, font_path, size):
#     custom_font = Font(family="Inter Medium", size=size)
#     widget.configure(font=custom_font)

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
        46.0,
        24.0,
        anchor="nw",
        text="23:01",
        fill="#EDF5FA",
        font=("InriaSans Bold", 40)
    )
    root.resizable(False, False)

def wrap_text(text, width):
    return '\n'.join(text[i:i+width] for i in range(0, len(text), width))

def prevent_edit(event):
    if text_widget.cget("state") == "disabled":
        return "break"  # Prevent any editing actions

def show_pill_information_frame(root, pill_info):
    global image_references
    ASSETS_PATH = Path(r"/home/pi/capstone/pill-identification/output/frame3/build/assets/frame0")
    # ASSETS_PATH = Path(r"E:\pill-identification\output\frame3\build\assets\frame0")

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
        406.0,
        238.0,
        image=image_image_1
    )

    pill_info_name = wrap_text(pill_info[0], width=50)

    canvas.create_text(
        110.0,
        63.0,
        anchor="nw",
        text=pill_info_name,
        fill="#000000",
        font=("Koulen", 21)
    )

    text = "Dosage: {}mg\n\nSpecial Instruction: {}\n\nPossible side effects: {}\n\n".format(pill_info[1], pill_info[2], pill_info[3])

    text_widget = Text(root, wrap="word", font=("Koulen", 15), bd=0, width=40, height=7)  
    text_widget.configure(state='normal')
    text_widget.insert("1.0", text)
    text_widget.configure(state='disabled', highlightthickness=0)
    text_widget.place(x=100, y=140)  # Positioning the text widget at (100, 150)

    # canvas.create_text(
    #     100.0,
    #     150.0,
    #     anchor="nw",
    #     # text=pill_info_gui,
    #     text="Dosage: {}\n\nSpecial Instruction: {}\n\nPossible side effects: {}\n\n".format(pill_info[1], pill_info[2], pill_info[3]),
    #     fill="#000000",
    #     font=("Koulen", 15),
    #     width=400,
    #     wrap="word"
    # )

    canvas.create_text(
        29.0,
        10.0,
        anchor="nw",
        text="23:01",
        fill="#DADADA",
        font=("InriaSans Bold", 32)
    )

    canvas.create_rectangle(
        573.0,
        221.0,
        718.0,
        404.0,
        fill="#D9D9D9",
        outline=""
    )
    root.resizable(False, False)

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

    canvas.create_text(
        58.0,
        16.0,
        anchor="nw",
        text="23:01",
        fill="#DADADA",
        font=("InriaSans Bold", 40)
    )

    canvas.create_text(
        110.0,
        240.0,
        anchor="nw",
        text="Pill cannot be identified.",
        fill="#000000",
        font=("Inter Medium", 40)
    )

    canvas.create_text(
        280.0,
        370.0,
        anchor="nw",
        text="Please try again",
        fill="#EDF5FA",
        font=("Inter Medium", 22)
    )
    root.resizable(False, False)

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
    
    pill_info = db.get_pill_info_gui('Sucranorm Metformin HCl 850mg (Packed)')
    print(pill_info[0])
    root = Tk()
    root.geometry("800x480")

    # show_logo_frame(root)
    # show_instructions_frame(root)
    show_pill_information_frame(root, pill_info)
    # show_error_frame(root)
    
    # Start the main loop
    root.mainloop()