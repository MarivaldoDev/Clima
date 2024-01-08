import requests
from customtkinter import *
from tkinter import messagebox
from PIL import Image
from datetime import datetime


class App:
    def __init__(self) : 
        self.tela = CTk()
        self.tela.title('Weather')
        self.tela.resizable(width=False, height=False)
        self.tela.config(background='#4A708B')
        self.tela.iconbitmap('imgs\sol.ico')
        self.tela.geometry('500x550')
        self.main()
        self.tela.mainloop()

    def main(self):
        self.imagem = Image.open('imgs\main.png')
        self.imagem1 = CTkImage(dark_image=self.imagem, light_image=self.imagem, size=(950, 750))

        self.imagem_tela = CTkLabel(master=self.tela, text='' ,image=self.imagem1, fg_color='#4a708b', bg_color='#4a708b', width=100, height=150)
        self.label = CTkLabel(master=self.tela, text='City', font=('arial', 40), text_color='#00FFFF', fg_color='#4a708b')

        self.city = CTkEntry(master=self.tela, width=200 ,height=40, placeholder_text='Write your city...', 
        border_width=2,
        border_color='#7FFFD4',
        placeholder_text_color='#7FFFD4', 
        bg_color='#4a708b')

        self.seachr = CTkButton(master=self.tela, text='Seachr', text_color='#F0FFFF',
        font=('arial', 28), 
        width=150, 
        height=50, 
        bg_color='#4a708b', 
        fg_color='#191970', 
        corner_radius=100,
        command=self.new_window)

        self.imagem_tela.place(x=-150, y=-140)
        self.label.place(x=210, y=310)
        self.city.place(x=150, y=370)
        self.seachr.place(x=175, y=460)

    def temperaturas(self):
        cidade = self.city.get()
        
        key = "3d750123dbfeefcba851a398e9d81521"
        site = f"https://api.openweathermap.org/data/2.5/weather?q={cidade.capitalize()}&appid={key}&lang=pt_br"

        requisicao = requests.get(site)
        requisicao_dicionario = requisicao.json()

        situacao = requisicao_dicionario['weather'][0]['description']
        temperatura = requisicao_dicionario['main']['temp'] - 273.15
        sensacao = requisicao_dicionario['main']['feels_like'] - 273.15     

        mensagem = f"""Situação: {situacao.upper()}\nTemperatura: {temperatura:.1f}°C\nSensação térmica: {sensacao:.1f}°C"""
            
        return mensagem

    def new_window(self):
        self.new_tela = CTkToplevel()
        self.new_tela.title('Weather')
        self.new_tela.geometry('400x450')
        self.new_tela.config(background='#4A708B')
        try:
            self.texto = self.temperaturas()
        except requests.exceptions.ConnectionError:
            messagebox.showerror(title="Erro", message="Verifique sua coneão com a internet!")
            self.new_tela.destroy()
        except KeyError:
            messagebox.showerror(title="Erro", message="Apenas pesquise sobre o clima de cidades!")
            self.new_tela.destroy()
        else:
            if 'trovoada'.upper() in self.texto:
                self.trovoada = Image.open(r'imgs\trovoada.png')
                self.trovoada_tela = CTkImage(dark_image=self.trovoada, light_image=self.trovoada, size=(390, 280))
                self.imagem_trovoada = CTkLabel(master=self.new_tela, text='', image=self.trovoada_tela, bg_color='#4A708B')
                self.imagem_trovoada.place(x=10, y=40)
                self.new_tela.geometry('430x450')
                self.resul = CTkLabel(master=self.new_tela, text=self.texto, text_color='#FFFAFA', font=('arial', 21), bg_color='#4A708B')
                self.resul.place(x=10, y=340)
            elif 'chuva'.upper() in self.texto:
                self.img_chuva = Image.open('imgs\chuva.png')
                self.chuva_tela = CTkImage(dark_image=self.img_chuva, light_image=self.img_chuva, size=(500, 430))
                self.imagem_chuva = CTkLabel(master=self.new_tela, text='', image=self.chuva_tela, bg_color='#4A708B')
                self.resul = CTkLabel(master=self.new_tela, text=self.texto, text_color='#DCDCDC', font=('arial', 25), bg_color='#4A708B')
                self.resul.place(x=30, y=330)
                self.imagem_chuva.place(x=-60, y=-60)
            elif 'limpo'.upper() in self.texto:
                self.momento = datetime.now()
                if self.momento.hour >= 18:
                    self.img_lua = Image.open('imgs\lua.png')
                    self.lua_tela = CTkImage(dark_image=self.img_lua, light_image=self.img_lua, size=(500, 330))
                    self.imagem_lua = CTkLabel(master=self.new_tela, text='', image=self.lua_tela, bg_color='#4A708B')
                    self.imagem_lua.place(x=-60, y=-20)
                    self.resul = CTkLabel(master=self.new_tela, text=self.texto, text_color='#87CEFA', font=('arial', 25), bg_color='#4A708B')
                    self.resul.place(x=50, y=340)
                else:
                    self.img_sol = Image.open('imgs\sol.png')
                    self.sol_tela = CTkImage(dark_image=self.img_sol, light_image=self.img_sol, size=(500, 330))
                    self.imagem_sol = CTkLabel(master=self.new_tela, text='', image=self.sol_tela, bg_color='#4A708B')
                    self.imagem_sol.place(x=-60, y=-20)
                    self.resul = CTkLabel(master=self.new_tela, text=self.texto, text_color='#FFD700', font=('arial', 25), bg_color='#4A708B')
                    self.resul.place(x=50, y=340)
            elif 'nublado'.upper() in self.texto:
                self.nublado = Image.open(r'imgs\nublado.png')
                self.nublado_tela = CTkImage(dark_image=self.nublado, light_image=self.nublado, size=(500, 320))
                self.imagem_nublado = CTkLabel(master=self.new_tela, text='', image=self.nublado_tela, bg_color='#4A708B')
                self.imagem_nublado.place(x=-60, y=-20)
                self.resul = CTkLabel(master=self.new_tela, text=self.texto, text_color='#D3D3D3', font=('arial', 25), bg_color='#4A708B')
                self.resul.place(x=50, y=340)
            elif 'nuvens'.upper() in self.texto:
                self.nuvens = Image.open(r'imgs\nuvens.png')
                self.nuvens_tela = CTkImage(dark_image=self.nuvens, light_image=self.nuvens, size=(420, 200))
                self.imagem_nuvem = CTkLabel(master=self.new_tela, text='', image=self.nuvens_tela, bg_color='#4A708B')
                self.imagem_nuvem.place(x=-5, y=60)
                self.resul = CTkLabel(master=self.new_tela, text=self.texto, text_color='#D3D3D3', font=('arial', 25), bg_color='#4A708B')
                self.resul.place(x=20, y=340)
            elif 'neve'.upper() in self.texto:
                self.neve = Image.open(r'imgs\neve.png')
                self.neve_tela = CTkImage(dark_image=self.neve, light_image=self.neve, size=(380, 260))
                self.imagem_neve = CTkLabel(master=self.new_tela, text='', image=self.neve_tela, bg_color='#4A708B')
                self.imagem_neve.place(x=10, y=40)
                self.resul = CTkLabel(master=self.new_tela, text=self.texto, text_color='#FFFAFA', font=('arial', 25), bg_color='#4A708B')
                self.resul.place(x=50, y=340)
            else:
                self.resul = CTkLabel(master=self.new_tela, text=self.texto, text_color='cyan', font=('arial', 25), bg_color='#4A708B')
                self.resul.place(x=10, y=330)
            
            self.new_tela.mainloop()


App()