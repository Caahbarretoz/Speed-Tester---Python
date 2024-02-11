from tkinter import *
import speedtest
import customtkinter
from PIL import Image
import os


def on_enter(event):
    image_b = customtkinter.CTkImage(Image.open(current_path + "./pictures/botaow.png"), size=(127, 36))
    mybtn.configure(image=image_b, fg_color="#382B86", bg_color="#382B86")


def on_leave(event):
    image_a = customtkinter.CTkImage(Image.open(current_path + "./pictures/botao1.png"), size=(127, 36))
    mybtn.configure(image=image_a)


def testar():
    image_c = customtkinter.CTkImage(Image.open(current_path + "./pictures/refresh.png"), size=(127, 36))
    mybtn.configure(image=image_c, fg_color="#382B86", bg_color="#382B86")

    # Agendando a execução da função de teste de velocidade após um curto intervalo (10 ms)
    root.after(1, realizar_teste)


def realizar_teste():
    teste = speedtest.Speedtest()
    download = teste.download()
    upload = teste.upload()
    ping = teste.results.ping
    text_download = f"{download // 10 ** 6:.1f} Mbps"
    text_upload = f"{upload // 10 ** 6:.1f} Mbps"
    text_ping = f" {ping // 10 ** 6:.0f} ms"
    label_download.configure(text=text_download)
    label_upload.configure(text=text_upload)
    label_ping.configure(text=text_ping)


####################################################################################################################
width = 660
height = 383

root = customtkinter.CTk()
root.title("Speed Test")

x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 3) - (height // 3)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.resizable(False, False)

root.iconbitmap('./pictures/velocity.ico')

current_path = os.path.dirname((os.path.realpath(__file__)))

image_a = customtkinter.CTkImage(Image.open(current_path + "./pictures/botao1.png"), size=(127, 36))

background = customtkinter.CTkImage(Image.open(current_path + "./pictures/tela.png"), size=(width, height))

bg_label = customtkinter.CTkLabel(root, image=background, text="")
bg_label.place(x=0, y=0)


label_download = customtkinter.CTkLabel(root,
                                        text="",
                                        width=50,
                                        height=15,
                                        corner_radius=15,
                                        fg_color="#4635B2",
                                        text_color="black",
                                        justify="center",
                                        bg_color="#4635B2",
                                        font=("Roboto Mono", 13, "bold")
                                        )
label_download.place(x=219, y=220)


label_upload = customtkinter.CTkLabel(root,
                                      text="",
                                      width=40,
                                      height=15,
                                      corner_radius=15,
                                      fg_color="#4635B2",
                                      text_color="black",
                                      justify="center",
                                      bg_color="#4635B2",
                                      font=("Roboto Mono", 13, "bold")
                                      )
label_upload.place(x=360, y=220)

label_ping = customtkinter.CTkLabel(root,
                                    text="",
                                    width=10,
                                    height=10,
                                    corner_radius=15,
                                    fg_color="#7162CF",
                                    text_color="black",
                                    justify="center",
                                    bg_color="#7162CF",
                                    font=("Roboto Mono", 13, "bold"))
label_ping.place(x=306, y=107)

mybtn = customtkinter.CTkButton(root,
                                    image=image_a,
                                    cursor='hand2',
                                    command=testar,
                                    fg_color="#382B86",
                                    bg_color="#382B86",
                                    text="",
                                    hover=True)
mybtn.place(x=260, y=305)

mybtn.bind("<Enter>", on_enter, add='+')
mybtn.bind("<Leave>", on_leave, add='+')


root.mainloop()
