from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time
import random


class InstagramBot:


    def __init__(self, usuario, senha, link):
        self.username = usuario
        self.password = senha
        self.link = link
        self.qtdComentario = 0
        self.driver = webdriver.Firefox(executable_path=r"D:\projetos\BOT\geckodriver\geckodriver.exe")
        self.login()
        self.carregaComenta_sorteio()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_usuario = driver.find_element_by_xpath("//input[@name='password']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.password)
        campo_usuario.send_keys(Keys.RETURN)
        time.sleep(5)

    @staticmethod
    def digite_como_pessoa(comentario, onde_digitar):
        for letra in comentario:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,10)/30)

    

    def carregaComenta_sorteio(self):
        
        try:
            comentarios = [
            "esse é meu", 
            "já quero", 
            "já ganhei",
            "melhor sorteio",
            "to comentando muitoo",
            "premiação surreal",
            "premio top",
            "comentar muito pra ganhar",
            "quero esse premio",
            "qualidade altissima",
            "já to seguindo todas as regras",
            "vou ganhar, to sentindo",
            "melhor instagram"
            ]
            usuarios = [
                "@jorgeramosgus",
                "@cleitinho.leite",
                "@rick.hr",
                "@laura.lima",
                "@gipng",
                "@prisciow65",
                "@jbarros0",
                "@gabrieldasilvaarte",
                "@valter_vieira",
                "@joao.militao_",
                "@robertoamaral_",
                "@carlosaugusto.18",
                "@jrenattosilva",
                "@_evd",
                "@adonis_belo",
                "@fran_pimentel",
                "@deborasouza.ofc",
                "@pallomabasttos",
                "@thamires7159",
                "@joaovictorn.2016",
            ]
            emojies = [
                "😍",
                "😎",
                "👾",
                "🚗",
                "🚕", 
                "🚙",
                "😀", 
                "😃", 
                "😄",
                "😁",
                "😆",
                "😅",
                "😂", 
                "🤣"
            ]
            driver = self.driver
            driver.get(self.link)

            i = 0
            while (i < 100):
                driver.find_element_by_class_name("Ypffh").click()
                campo_comentario = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2,6))

                c = 0
                u = 0
                e = 0
                while (c < 4):
                    self.digite_como_pessoa(random.choice(comentarios), campo_comentario)
                    time.sleep(random.randint(10,30))
                    driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                    time.sleep(5)
                    c = c + 1
                    self.qtdComentario = self.qtdComentario + 1
                
                time.sleep(40)

                while (u < 7):
                    self.digite_como_pessoa(random.choice(usuarios), campo_comentario)
                    time.sleep(random.randint(10,25))
                    driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                    time.sleep(5)
                    u = u + 1
                    self.qtdComentario = self.qtdComentario + 1

                time.sleep(30)

                while (e < 5):
                    self.digite_como_pessoa(random.choice(emojies), campo_comentario)
                    time.sleep(random.randint(5,15))
                    driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                    time.sleep(5)
                    e = e + 1
                    self.qtdComentario = self.qtdComentario + 1
                

                
                print("Rodada " + str(i) + " de comentarios")
                i = i+1
                time.sleep(120)

                # https://www.instagram.com/p/CP3QldZsRhL/
        except Exception as e:
            print(e)
            print("Comentarios feitos: " + str(self.qtdComentario))
            time.sleep(5)
            






class App:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 15
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 5
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text = "InstaBOT")
        self.titulo["font"] = ("Verdana", "15", "bold")
        self.titulo.pack()

        self.userInput = Label(self.segundoContainer, text="Usuario", font=self.fontePadrao)
        self.userInput.pack(side=LEFT)

        self.user = Entry(self.segundoContainer)
        self.user["width"] = 30
        self.user["font"] = self.fontePadrao
        self.user.pack(side=LEFT)

        self.senhaInput = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaInput.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.linkLabel = Label(self.quartoContainer, text="link", font=self.fontePadrao)
        self.linkLabel.pack(side=LEFT)

        self.link = Entry(self.quartoContainer)
        self.link["width"] = 30
        self.link["font"] = self.fontePadrao
        self.link.pack(side=LEFT)

        self.autenticar = Button(self.quintoContainer)
        self.autenticar["text"] = "AUTENTICAR"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.logaUsuario
        self.autenticar.pack()
    
    def logaUsuario(self):
        usuario = self.user.get()
        senha = self.senha.get()
        link = self.link.get()
        usuario = InstagramBot(usuario, senha, link)

        self.user.delete(0, END)
        self.senha.delete(0, END)
        self.link.delete(0, END)


root = Tk()
App(root)
root.mainloop()

