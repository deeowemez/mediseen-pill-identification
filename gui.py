from tkinter import Tk, Canvas, PhotoImage
from pathlib import Path
import time
import tkinter as tk

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

    canvas.create_text(
        276.0,
        389.0,
        anchor="nw",
        text="press the screen to start",
        fill="#9C9C9C",
        font=("InriaSans BoldItalic", 24)
    )

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_references["image_1"] = image_image_1
    image_1 = canvas.create_image(
        400.0,
        223.0,
        image=image_image_1
    )
    # root.resizable(False, False)


def show_instructions_frame(root):
    global image_references
    ASSETS_PATH = Path(r"/home/pi/capstone/pill-identification/output/frame2/build/assets/frame0")
    # ASSETS_PATH = Path(r"E:\pill-identification\output\frame2\build\assets\frame0")

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
        107.0,
        152.0,
        anchor="nw",
        text="Insert the pill into the\n  designated pill slot,\n    ensuring proper\n        alignment.",
        fill="#000000",
        font=("Inter Medium", 60)
    )

    canvas.create_text(
        46.0,
        24.0,
        anchor="nw",
        text="23:01",
        fill="#EDF5FA",
        font=("InriaSans Bold", 40)
    )

def show_pill_information_frame(root):
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

    canvas.create_text(
        37.0,
        63.0,
        anchor="nw",
        text="Glucophage XR Metformin HCl \n(Unpacked)",
        fill="#000000",
        font=("Koulen Regular", 36)
    )

    canvas.create_text(
        79.0,
        238.0,
        anchor="nw",
        text="Dosage: \n\nSpecial Instruction: \n\nPossible side effects: \n\n",
        fill="#000000",
        font=("Koulen Regular", 24)
    )

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
        272.0,
        203.0,
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
        125.0,
        241.0,
        anchor="nw",
        text="Pill cannot be identified.",
        fill="#000000",
        font=("Inter Medium", 48)
    )

    canvas.create_text(
        211.0,
        328.0,
        anchor="nw",
        text="Please try again",
        fill="#EDF5FA",
        font=("Inter Medium", 24)
    )

# Define switch_frame function after the main block
def clear_frame(root, new_frame_func):
    # Clear the current frame
    for widget in root.winfo_children():
        widget.destroy()

    # Show the new frame
    new_frame_func(root)

# Function for initializing GUI
def switch_frames(root, frame_function, delay):
    root.after(delay, lambda: clear_frame(root, frame_function))

def check_and_show_pill_information(root, delay, classification):
    # classification = 'asldkfjalks'  # Replace with your actual classification logic
    print('clasdf:', classification)
    if classification:  # Assuming classification is True if pill is identified
        root.after(delay, lambda: clear_frame(root, show_pill_information_frame, 1))


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    show_logo_frame(root)
    # show_instructions_frame(root)
    # show_pill_information_frame(root)
    # show_error_frame(root)
    # # Start by showing the error frame
    # switch_frame(root, show_logo_frame)

    # # Schedule the function to check condition and switch frames
    # root.after(1000, check_condition_and_switch, root)

    # # Start the main loop
    root.mainloop()