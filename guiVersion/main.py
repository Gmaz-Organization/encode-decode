#module importing
from encode_decode import *
import tkinter
import customtkinter
import os
import sys

# function for finding temporary directory of added files
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#f inding temporary directory of added files
path_apperaance = resource_path(r"guiVersion\apperanceConfig\gmaz_theme_v2.json")
path_icon = resource_path(r"guiVersion\apperanceConfig\converter_white_dark.ico")
# we need to make the icon

# customize
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(r"{}".format(path_apperaance))
root = customtkinter.CTk()
#root.iconbitmap(r"{}".format(path_icon))


class App(customtkinter.CTk):

    WIDTH = 692
    HEIGHT = 532

    def __init__(self):
        super().__init__()

        self.title("ENCODE or DECODE")
        # window set and it can't be moved
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(width=App.WIDTH, height=App.HEIGHT)
        self.maxsize(width=App.WIDTH, height=App.HEIGHT)

        # set the icon
        self.iconbitmap(r"{}".format(path_icon))


        # change encode to decode
        # switch on left = encode, on right = decode
        switch_var = customtkinter.StringVar(value="left")

        # switch mode events
        def switch_event():
          value = switch_var.get()

          # set to encode
          if value == "left":
            self.title_label.configure(text="ENCODE", font = "65")
            self.convert_bottun.configure(text="Encode")
            self.convert_bottun.configure(command=self.encodeMode)
            self.reset()
            self.key_frame1.configure(state = "disabled")
            self.key_frame2.configure(state = "disabled")
            self.key_frame3.configure(state = "disabled")

          # set to decode
          elif value == "right":
            self.title_label.configure(text="DECODE", font = "65")
            self.convert_bottun.configure(text="Decode")
            self.convert_bottun.configure(command=self.decodeMode)
            self.reset()
            self.key_frame1.configure(state = "normal")
            self.key_frame2.configure(state = "normal")
            self.key_frame3.configure(state = "normal")
          else:
            pass


        self.input_frame = tkinter.Text(master=self, width=36, height=20, font = "Gilroy", insertbackground='white',
                                         bg="gray10", fg ="#ffffff", highlightthickness=2, 
                                         highlightbackground = "gray10", highlightcolor= "#109a47")
        self.input_frame.grid(row=3, column=1, columnspan=3)

        self.output_frame = tkinter.Text(master=self, width=36, height=20, font = "Gilroy", insertbackground='white',
                                         bg="gray10", fg ="#ffffff", highlightthickness=2, 
                                         highlightbackground = "gray10", highlightcolor= "#109a47")
        self.output_frame.grid(row=3, column=4, columnspan=5)

        self.title_label = customtkinter.CTkLabel(master=self)
        self.title_label.grid(row=0, column=0, columnspan=9, pady=6)

        self.switch = customtkinter.CTkSwitch(master=self, text="switch mode", command=switch_event, 
                                              variable=switch_var ,onvalue="right",offvalue="left",)
        self.switch.grid(row=1, column=0, columnspan=9)

        
        button_row = 6 # row where the buttons are

        self.convert_bottun = customtkinter.CTkButton(master=self)
        self.convert_bottun.grid(row=button_row, column=1, columnspan=1)

        self.reset_bottun = customtkinter.CTkButton(master=self, command=self.reset, text="Reset")
        self.reset_bottun.grid(row=button_row, column=3, columnspan=1)

        self.key_label = customtkinter.CTkLabel(master=self, text = "key: ", anchor="e")
        self.key_label.grid(row=button_row, column=4, columnspan=2)

        self.key_frame1 = tkinter.Text(master=self, width=2, height=1, font = "Gilroy", insertbackground='white',
                                         bg="gray10", fg ="#ffffff", highlightthickness=2, 
                                         highlightbackground = "gray10", highlightcolor= "#109a47")
        self.key_frame1.grid(row=button_row, column=6, columnspan=1, padx = 0)

        self.key_frame2 = tkinter.Text(master=self, width=2, height=1, font = "Gilroy", insertbackground='white',
                                         bg="gray10", fg ="#ffffff", highlightthickness=2, 
                                         highlightbackground = "gray10", highlightcolor= "#109a47")
        self.key_frame2.grid(row=button_row, column=7, columnspan=1, padx = 0)

        self.key_frame3 = tkinter.Text(master=self, width=2, height=1, font = "Gilroy", insertbackground='white',
                                         bg="gray10", fg ="#ffffff", highlightthickness=2, 
                                         highlightbackground = "gray10", highlightcolor= "#109a47")
        self.key_frame3.grid(row=button_row, column=8, columnspan=1, padx = 0)

        
        # empty rows and col for viusals
        self.empty_col1 = customtkinter.CTkLabel(master=self, text="", width=20)
        self.empty_col1.grid(row=button_row, column=0)
        self.empty_col2 = customtkinter.CTkLabel(master=self, text="", width=20)
        self.empty_col2.grid(row=button_row, column=2)

        self.empty_row1 = customtkinter.CTkLabel(master=self, text="")
        self.empty_row1.grid(row=2, column=0, columnspan=9)
        self.empty_row2 = customtkinter.CTkLabel(master=self, text="")
        self.empty_row2.grid(row=4, column=0, columnspan=9)


        # set default values
        self.title_label.configure(text="ENCODE", font = "65")
        self.convert_bottun.configure(text="Encode")
        self.convert_bottun.configure(command=self.encodeMode)
        self.input_frame.insert("0.0", "type here")
        self.output_frame.insert("0.0", "output will be here")
        self.output_frame.configure(state = "disabled") #every time when we change this we need to configutr  state = enabled first
        self.key_frame1.configure(state = "disabled")
        self.key_frame2.configure(state = "disabled")
        self.key_frame3.configure(state = "disabled")


    def encodeMode(self):
        text = self.input_frame.get("0.0", "end")
        output_text, key = encode(text)
        key_list = key.split(".") # spliting the key into 3 parts 00.00.00

        self.key_frame1.configure(state = "normal")
        self.key_frame1.delete("0.0", "end")
        self.key_frame1.insert("0.0", key_list[0])
        self.key_frame1.configure(state = "disabled")

        self.key_frame2.configure(state = "normal")
        self.key_frame2.delete("0.0", "end")
        self.key_frame2.insert("0.0", key_list[1])
        self.key_frame2.configure(state = "disabled")

        self.key_frame3.configure(state = "normal")
        self.key_frame3.delete("0.0", "end")
        self.key_frame3.insert("0.0", key_list[2])
        self.key_frame3.configure(state = "disabled")

        self.output_frame.configure(state = "normal")
        self.output_frame.delete("0.0", "end")
        self.output_frame.insert("0.0", output_text)
        self.output_frame.configure(state = "disabled")


    def decodeMode(self):
        text = self.input_frame.get("0.0", "end")
        key1 = self.key_frame1.get("0.0", "end")
        key2 = self.key_frame2.get("0.0", "end")
        key3 = self.key_frame3.get("0.0", "end")
        
        try:
          # checking if the key input is valid
          if ( (int(key1)>=0 and int(key1)<=99) and
              (int(key2)>=0 and int(key2)<=99) and
              (int(key3)>=0 and int(key3)<=99)):

                key = (f"{key1}.{key2}.{key3}")
                output_text = decode(text, key)

                self.output_frame.configure(state = "normal")
                self.output_frame.delete("0.0", "end")
                self.output_frame.insert("0.0", output_text)
                self.output_frame.configure(state = "disabled")

          else:
            self.reset()

        except:
          print("invalid key error")
          self.reset()




        
    def reset(self):
        self.input_frame.delete("0.0", "end")
        self.input_frame.insert("0.0", "type here")

        self.output_frame.configure(state = "normal")
        self.output_frame.delete("0.0", "end")
        self.output_frame.insert("0.0", "output will be here")
        self.output_frame.configure(state = "disabled")

        self.key_frame1.configure(state = "normal")
        self.key_frame1.delete("0.0", "end")

        self.key_frame2.configure(state = "normal")
        self.key_frame2.delete("0.0", "end")

        self.key_frame3.configure(state = "normal")
        self.key_frame3.delete("0.0", "end")



if __name__ == "__main__":
    app = App()
    app.mainloop()