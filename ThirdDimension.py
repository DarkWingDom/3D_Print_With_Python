# Challenge 2 - Program to output 3D OpenScad files
# Dominic Whelan
# Nov.08, 2021

from tkinter import *
import openscad as op

root = Tk()
root.title("Third Dimension")
root.configure(background="gray23")

# Functions


def primary_color_pick():
    entry = Primary_Color_Entry.get()
    if entry == "1":
        color = op.rgb(0, 0, 215)
        return color
    if entry == "2":
        color = op.rgb(215, 0, 0)
        return color
    if entry == "3":
        color = op.rgb(0, 215, 0)
        return color
    if entry == "4":
        color = op.rgb(255, 255, 0)
        return color
    if entry == "5":
        color = op.rgb(0, 0, 0)
        return color
    if entry == "6":
        color = op.rgb(255, 255, 255)
        return color
    if entry == "7":
        color = op.rgb(180, 180, 200)
        return color


def secondary_color_pick():
    entry = Secondary_Color_Entry.get()
    if entry == "1":
        color = op.rgb(0, 0, 215)
        return color
    if entry == "2":
        color = op.rgb(215, 0, 0)
        return color
    if entry == "3":
        color = op.rgb(0, 215, 0)
        return color
    if entry == "4":
        color = op.rgb(255, 255, 0)
        return color
    if entry == "5":
        color = op.rgb(0, 0, 0)
        return color
    if entry == "6":
        color = op.rgb(255, 255, 255)
        return color
    if entry == "7":
        color = op.rgb(180, 180, 200)
        return color


def tertiary_color_pick():
    entry = Tertiary_Color_Entry.get()
    if entry == "1":
        color = op.rgb(0, 0, 215)
        return color
    if entry == "2":
        color = op.rgb(215, 0, 0)
        return color
    if entry == "3":
        color = op.rgb(0, 215, 0)
        return color
    if entry == "4":
        color = op.rgb(255, 255, 0)
        return color
    if entry == "5":
        color = op.rgb(0, 0, 0)
        return color
    if entry == "6":
        color = op.rgb(255, 255, 255)
        return color
    if entry == "7":
        color = op.rgb(180, 180, 200)
        return color


def button_click_1():
    op.cyl(10, 20)
    primary_color_pick()
    cylinder = op.result()

    op.cone(10, 10)
    secondary_color_pick()
    op.translate(0, 0, 20)
    cone = op.result()

    op.union([cylinder, cone])
    top_rocket = op.result()

    op.cone(20, 10)
    op.translate(0, 0, -5)
    tertiary_color_pick()
    cone_2 = op.result()

    op.union([top_rocket, cone_2])
    body_rocket = op.result()
    op.output(body_rocket)


def button_click_2():
    op.box(5, 2, 2)
    secondary_color_pick()
    op.translate(0, -5, 0)
    foot_1 = op.result()

    op.cyl(2, 6)
    primary_color_pick()
    op.translate(1, -4, 2)
    leg_1 = op.result()

    op.box(5, 2, 2)
    secondary_color_pick()
    op.translate(0, 3, 0)
    foot_2 = op.result()

    op.cyl(2, 6)
    primary_color_pick()
    op.translate(1, 4, 2)
    leg_2 = op.result()

    op.box(4, 12, 16)
    primary_color_pick()
    op.translate(-1, -6, 8)
    body = op.result()

    op.box(4, 8, 10)
    tertiary_color_pick()
    op.translate(-.5, -4, 12)
    body_center = op.result()

    op.cyl(2, 4)
    primary_color_pick()
    op.translate(1, 0, 24)
    neck = op.result()

    op.box(4, 8, 6)
    primary_color_pick()
    op.translate(-1, -4, 27)
    head = op.result()

    op.sphere(2)
    tertiary_color_pick()
    op.translate(3, -2, 31)
    eye_1 = op.result()

    op.sphere(2)
    tertiary_color_pick()
    op.translate(3, 2, 31)
    eye_2 = op.result()

    op.box(2, 4, 1)
    secondary_color_pick()
    op.translate(1.5, -2, 28)
    mouth = op.result()

    op.cyl(2, 8)
    primary_color_pick()
    op.rotate(135, 0, 0)
    op.translate(1, -5, 23)
    arm_1 = op.result()

    op.cyl(2, 8)
    primary_color_pick()
    op.rotate(225, 0, 0)
    op.translate(1, 5, 23)
    arm_2 = op.result()

    op.box(3, 3, 3)
    secondary_color_pick()
    op.rotate(135, 0, 0)
    op.translate(-0.5, -8, 18)
    hand_1 = op.result()

    op.box(3, 3, 3)
    secondary_color_pick()
    op.rotate(225, 0, 0)
    op.translate(-0.5, 10.5, 19.5)
    hand_2 = op.result()

    op.union([foot_1, leg_1, foot_2, leg_2, body, neck, head, eye_1, eye_2, mouth, arm_1, arm_2, hand_1, hand_2,
              body_center])
    robot = op.result()
    op.output(robot)


def button_click_3():
    op.cyl(12, 16)
    secondary_color_pick()
    op.rotate(90, 0, 0)
    op.translate(0, 0, 0)
    front_body = op.result()

    op.sphere(12)
    secondary_color_pick()
    op.translate(0, -16, 0)
    front = op.result()

    op.cyl(3, 6)
    tertiary_color_pick()
    op.translate(0, -12, 6)
    stack = op.result()

    op.box(16, 20, 16)
    op.translate(-8, 0, -6)
    back_1 = op.result()

    op.box(17, 8, 8)
    op.translate(-8.5, 6, 0)
    back_2 = op.result()

    op.difference([back_1, back_2])
    primary_color_pick()
    back_body = op.result()

    op.box(16, 40, 6)
    primary_color_pick()
    op.translate(-8, -20, -12)
    bottom = op.result()

    op.cyl(12, 2)
    tertiary_color_pick()
    op.rotate(0, 90, 0)
    op.translate(8, -12, -12)
    wheel_1 = op.result()

    op.cyl(12, 2)
    tertiary_color_pick()
    op.rotate(0, 90, 0)
    op.translate(-10, -12, -12)
    wheel_2 = op.result()

    op.cyl(12, 2)
    tertiary_color_pick()
    op.rotate(0, 90, 0)
    op.translate(8, 2, -12)
    wheel_3 = op.result()

    op.cyl(12, 2)
    tertiary_color_pick()
    op.rotate(0, 90, 0)
    op.translate(-10, 2, -12)
    wheel_4 = op.result()

    op.cyl(12, 2)
    tertiary_color_pick()
    op.rotate(0, 90, 0)
    op.translate(8, 14, -12)
    wheel_5 = op.result()

    op.cyl(12, 2)
    tertiary_color_pick()
    op.rotate(0, 90, 0)
    op.translate(-10, 14, -12)
    wheel_6 = op.result()

    op.union([front, front_body, stack, back_body, bottom, wheel_1, wheel_2, wheel_3, wheel_4, wheel_5, wheel_6])
    train = op.result()
    op.output(train)


# Labels/Headings

Heading = Label(root, text="Welcome to the Third Dimension", padx=150, pady=20, bg="gray16", fg="white", borderwidth=5)
Direction = Label(root, text="Please make a choice from the menu below!", bg="royalblue1", padx=125, pady=5)
Primary_Color_Heading = Label(root, text="Primary Color         Enter Here ---->", padx=16, pady=0)
Secondary_Color_Heading = Label(root, text="Secondary Color         Enter Here ---->", padx=8, pady=0)
Tertiary_Color_Heading = Label(root, text="Tertiary Color         Enter Here ---->", padx=16, pady=0)
Spacer = Label(root, text="                       ",pady=10, bg="gray23")
Spacer2 = Label(root, text="                       ", pady=10, bg="gray23")
Spacer3 = Label(root, text="                       ", pady=10, bg="gray23")


Primary_Blue = Label(root, text="1", padx=10, pady=5, bg="blue", borderwidth=4)
Primary_Red = Label(root, text="2", padx=10, pady=5, bg="red", borderwidth=4)
Primary_Green = Label(root, text="3", padx=10, pady=5, bg="green", borderwidth=4)
Primary_Yellow = Label(root, text="4", padx=10, pady=5, bg="yellow", borderwidth=4)
Primary_Black = Label(root, text="5", padx=10, pady=5, bg="black", fg="white", borderwidth=4)
Primary_White = Label(root, text="6", padx=10, pady=5, bg="white", borderwidth=4)
Primary_Grey = Label(root, text="7", padx=10, pady=5, bg="grey", borderwidth=4)


Secondary_Blue = Label(root, text="1", padx=10, pady=5, bg="blue", borderwidth=4)
Secondary_Red = Label(root, text="2", padx=10, pady=5, bg="red", borderwidth=4)
Secondary_Green = Label(root, text="3", padx=10, pady=5, bg="green", borderwidth=4)
Secondary_Yellow = Label(root, text="4", padx=10, pady=5, bg="yellow", borderwidth=4)
Secondary_Black = Label(root, text="5", padx=10, pady=5, bg="black", fg="white", borderwidth=4)
Secondary_White = Label(root, text="6", padx=10, pady=5, bg="white", borderwidth=4)
Secondary_Grey = Label(root, text="7", padx=10, pady=5, bg="grey", borderwidth=4)

Tertiary_Blue = Label(root, text="1", padx=10, pady=5, bg="blue", borderwidth=4)
Tertiary_Red = Label(root, text="2", padx=10, pady=5, bg="red", borderwidth=4)
Tertiary_Green = Label(root, text="3", padx=10, pady=5, bg="green", borderwidth=4)
Tertiary_Yellow = Label(root, text="4", padx=10, pady=5, bg="yellow", borderwidth=4)
Tertiary_Black = Label(root, text="5", padx=10, pady=5, bg="black", fg="white", borderwidth=4)
Tertiary_White = Label(root, text="6", padx=10, pady=5, bg="white", borderwidth=4)
Tertiary_Grey = Label(root, text="7", padx=10, pady=5, bg="grey", borderwidth=4)

# Define Buttons

Rocket_Button = Button(root, text="Rocket", padx=20, pady=0, command=button_click_1)
Robot_Button = Button(root, text="Robot", padx=22, pady=0, command=button_click_2)
Train_Button = Button(root, text="Train", padx=25, pady=0, command=button_click_3)

# Define Entry Boxes

Primary_Color_Entry = Entry(root, width=5, borderwidth=2)
Secondary_Color_Entry = Entry(root, width=5, borderwidth=2)
Tertiary_Color_Entry = Entry(root, width=5, borderwidth=2)


# Screen Designations

Heading.grid(row=0, column=0, columnspa=9)
Direction.grid(row=1, column=0, columnspa=9)

Rocket_Button.grid(row=3, column=0)
Robot_Button.grid(row=6, column=0)
Train_Button.grid(row=9, column=0)

Spacer.grid(row=2, column=0, columnspan=8)
Spacer2.grid(row=11, column=0, columnspan=8)
# Spacer2.grid(row=8, column=2, columnspan=6)

Primary_Color_Entry.grid(row=3, column=8)
Secondary_Color_Entry.grid(row=6, column=8)
Tertiary_Color_Entry.grid(row=9, column=8)

Primary_Color_Heading.grid(row=3, column=2, columnspan=7)
Primary_Blue.grid(row=4, column=2)
Primary_Red.grid(row=4, column=3)
Primary_Green.grid(row=4, column=4)
Primary_Yellow.grid(row=4, column=5)
Primary_Black.grid(row=4, column=6)
Primary_White.grid(row=4, column=7)
Primary_Grey.grid(row=4, column=8)

Secondary_Color_Heading.grid(row=6, column=2, columnspan=7)
Secondary_Blue.grid(row=7, column=2)
Secondary_Red.grid(row=7, column=3)
Secondary_Green.grid(row=7, column=4)
Secondary_Yellow.grid(row=7, column=5)
Secondary_Black.grid(row=7, column=6)
Secondary_White.grid(row=7, column=7)
Secondary_Grey.grid(row=7, column=8)

Tertiary_Color_Heading.grid(row=9, column=2, columnspan=7)
Tertiary_Blue.grid(row=10, column=2)
Tertiary_Red.grid(row=10, column=3)
Tertiary_Green.grid(row=10, column=4)
Tertiary_Yellow.grid(row=10, column=5)
Tertiary_Black.grid(row=10, column=6)
Tertiary_White.grid(row=10, column=7)
Tertiary_Grey.grid(row=10, column=8)


root.mainloop()