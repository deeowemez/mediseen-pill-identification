#!/usr/bin/env python

# Import libraries for running model
# import model
import time
# import pill_detection

# # Import libraries for tts
# import tts
# import sounddevice as sd
# import numpy as np
# import librosa
# import alsaaudio

# # Import libraries for gui
from tkinter import Tk
import tkinter as tk
import gui

# # Import libraries for accessing GPIO pins
# # import buttons
# import RPi.GPIO as GPIO
import threading

# # Import libraries for taking pictures
# import webcam

from tkinter import Tk, Canvas, PhotoImage
from pathlib import Path
import time

# Dictionary to store references to the images
image_references = {}

def show_logo_frame(root):
    global image_references
    # OUTPUT_PATH = Path(__file__).parent
    # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/capstone/pill-identification/output/frame1/build/assets/frame0")
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
    # OUTPUT_PATH = Path(__file__).parent
    # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/capstone/pill-identification/output/frame2/build/assets/frame0")
    ASSETS_PATH = Path(r"E:\pill-identification\output\frame2\build\assets\frame0")

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
    # OUTPUT_PATH = Path(__file__).parent
    # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/capstone/pill-identification/output/frame3/build/assets/frame0")
    ASSETS_PATH = Path(r"E:\pill-identification\output\frame3\build\assets\frame0")

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
    # OUTPUT_PATH = Path(__file__).parent
    # ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/capstone/pill-identification/output/frame4/build/assets/frame0")
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
def switch_frame(root, new_frame_func):
    # Clear the current frame
    for widget in root.winfo_children():
        widget.destroy()

    # Show the new frame
    new_frame_func(root)


# # Database connection information
# pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
# pill_table = "pill_info_table"

# # Initialize ALSA mixer
# mixer = alsaaudio.Mixer()

# # Function for initialzing GPIO
# def gpio_init():
#     GPIO.setmode(GPIO.BCM)

#     buttons = [26,19,13,6]

#     # Set up GPIO pins as inputs
#     GPIO.setup(buttons, GPIO.IN)
    
#     def button_pressed(channel):
#         print(f"Button is pressed on channel {channel}")
        
#         if channel == 26:
#             tts.increase_volume()

#         if channel == 19:
#             tts.decrease_volume()
    
#     for button in buttons:
#         GPIO.add_event_detect(button, GPIO.FALLING, callback=button_pressed, bouncetime=200)

# root = ''

# Function for initializing GUI
def gui_init():
    # global root
    root = tk.Tk()
    root.geometry("800x480")
    show_logo_frame(root)
    root.after(3000, check_classification, root)
    root.mainloop()

def check_classification(root):
    classification = 'Glucophage XR Metformin HCl 750mg (Unpacked)'
    if classification:
        root.after(0, gui.switch_frame, root, gui.show_pill_information_frame)
    else:
        switch_frame(root, show_instructions_frame)
        root.after(0, gui.switch_frame, root, gui.show_error_frame)
    time.sleep(1)

    # Schedule the next check after 1000 ms (1 second)
    # root.after(1000, check_classification, root)

# Create a thread for button detection
# button_thread = threading.Thread(target=gpio_init, daemon=True)
# button_thread.start()

# Create a thread for GUI
# gui_thread = threading.Thread(target=gui_init)
# gui_thread.start()

# Keep the program running indefinitely

if __name__ == "__main__":

    # Keep the program running indefinitely
    try:
        # Create a thread for GUI
        gui_thread = threading.Thread(target=gui_init)
        gui_thread.start()
        
        print('asdf')

        # # Start periodic check for classification
        # classification = 'Glucophage XR Metformin HCl 750mg (Unpacked)'
        # if classification:
        #     print('laskdjf')
        #     root.after(3000, root.destroy)  # Close the window after 3000 milliseconds (3 seconds)
        #     gui.show_logo_frame(root)
        # else:
        #     print('asdf')
        #     root.after(3000, root.destroy)  # Close the window after 3000 milliseconds (3 seconds)
        #     gui.show_instructions_frame(root)
        #     # Schedule the next check after 1000 ms (1 second)
        #     root.after(1000, check_classification)

        # # Start the periodic classification check
        # check_classification()

    except KeyboardInterrupt:
        # GPIO.cleanup()
        print('Exiting...')
    except Exception as e:
        print('An error occurred:', e)
        # GPIO.cleanup()
