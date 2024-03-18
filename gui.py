from tkinter import Tk, Canvas, PhotoImage
from pathlib import Path

def relative_to_assets(path: str) -> Path:
    return Path(__file__).parent / "output/frame1/build/assets/frame0" / Path(path)

def show_logo_frame(root):
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
    canvas.create_image(
        400.0,
        223.0,
        image=image_image_1
    )

def show_instructions_frame(root):
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
    canvas.create_image(
        415.0,
        240.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(
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

def switch_frame(root, new_frame_func):
    # Clear the current frame
    for widget in root.winfo_children():
        widget.destroy()

    # Show the new frame
    new_frame_func(root)

if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x480")
    root.mainloop()
    show_logo_frame(root)
    # show_instructions_frame()
    # show_pill_information_frame()
    # show_error_frame()