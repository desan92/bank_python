import bbdd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def main():
    main_window = Tk()
    app = PaginaInicial(main_window)
    main_window.mainloop()


class PaginaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("BANK")
        self.root.geometry("1200x600")

        # layout all of the main containers
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # create all of the main containers
        self.top_frame = Frame(self.root, bg='navy', width=1200, height=100, pady=3)
        self.main_frame = Frame(self.root, bg='#11DBF2', width=1200, height=500, padx=3, pady=3)

        self.top_frame.grid(row=0, sticky="ew")
        self.main_frame.grid(row=1, sticky="nsew")

        # create the center widgets
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.ctr_mid = Frame(self.main_frame, bg='#11DBF2', width=250, height=190, padx=3, pady=3)
        self.ctr_mid.grid(row=0, column=1, sticky="nsew")

        self.Title()
        self.logWidgets()

        self.btn_log = Button(self.ctr_mid, fg="white", bg="navy", text="Login",
                           relief="flat", cursor="hand1", command=lambda: self.log(self.username.get(), self.password.get()))
        self.btn_log.place(relx=0.41, rely=0.5, anchor=CENTER, width=90)
        self.btn_register = Button(self.ctr_mid, fg="white", bg="navy", text="Registre",
                           relief="flat", cursor="hand1", command=self.register)
        self.btn_register.place(relx=0.51, rely=0.5, anchor=CENTER, width=90)

    def logWidgets(self):
        self.username = StringVar()
        self.password = StringVar()

        self.label_username = Label(self.ctr_mid, text='USERNAME:', fg="navy", bg="#11DBF2", font="HELVETICA 10 bold")
        self.label_username.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.input_username = Entry(self.ctr_mid, textvariable=self.username)
        self.input_username.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.label_pass = Label(self.ctr_mid, text='PASSWORD:', fg="navy", bg="#11DBF2", font="HELVETICA 10 bold")
        self.label_pass.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.input_pass = Entry(self.ctr_mid, textvariable=self.password)
        self.input_pass.place(relx=0.5, rely=0.4, anchor=CENTER)

    def Title(self):
        # create the widgets for the top frame
        self.model_label = Label(self.top_frame, text='London Bank', fg="white", bg="navy", font="HELVETICA 30 bold")

        # layout the widgets in the top frame
        self.model_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def register(self):
        self.nom_usuari = StringVar()
        self.cognom_usuari = StringVar()
        self.user = StringVar()
        self.contrasenya = StringVar()
        self.tlf = StringVar()
        self.mail = StringVar()


        pop = Toplevel(self.main_frame, background="#11DBF2")
        pop.geometry("400x300")

        label_registre = Label(pop, foreground="navy", background="#11DBF2", text="Registre",
                          font="HELVETICA 12 bold").place(relx=0.5, rely=0.1, anchor=CENTER)

        label_nom = Label(pop, foreground="navy", background="#11DBF2", text="Nom usuari:",
                         font="HELVETICA 8 bold").place(relx=0.15, rely=0.2, anchor=CENTER)
        txt_nom = Entry(pop, textvariable=self.nom_usuari).place(relx=0.45, rely=0.2, anchor=CENTER)
        label_cognom = Label(pop, foreground="navy", background="#11DBF2", text="Cognom usuari:",
                         font="HELVETICA 8 bold").place(relx=0.15, rely=0.3, anchor=CENTER)
        txt_cognom = Entry(pop, textvariable=self.cognom_usuari).place(relx=0.45, rely=0.3, anchor=CENTER)
        label_username = Label(pop, foreground="navy", background="#11DBF2", text="Username:",
                             font="HELVETICA 8 bold").place(relx=0.15, rely=0.4, anchor=CENTER)
        txt_username = Entry(pop, textvariable=self.user).place(relx=0.45, rely=0.4, anchor=CENTER)
        label_pass = Label(pop, foreground="navy", background="#11DBF2", text="Password:",
                             font="HELVETICA 8 bold").place(relx=0.15, rely=0.5, anchor=CENTER)
        txt_pass = Entry(pop, textvariable=self.contrasenya).place(relx=0.45, rely=0.5, anchor=CENTER)
        label_telefon = Label(pop, foreground="navy", background="#11DBF2", text="Telefon:",
                             font="HELVETICA 8 bold").place(relx=0.15, rely=0.6, anchor=CENTER)
        txt_telefon = Entry(pop, textvariable=self.tlf).place(relx=0.45, rely=0.6, anchor=CENTER)
        label_mail = Label(pop, foreground="navy", background="#11DBF2", text="Email:",
                             font="HELVETICA 8 bold").place(relx=0.15, rely=0.7, anchor=CENTER)
        txt_mail = Entry(pop, textvariable=self.mail).place(relx=0.45, rely=0.7, anchor=CENTER)

        btn_canviar = Button(pop, text="Canviar", relief="flat", background="navy", cursor="hand1",
                             foreground="white",
                             command=lambda: self.GuardarUsuari(self.nom_usuari.get(), self.cognom_usuari.get(),
                                                         self.user.get(), self.contrasenya.get(), self.tlf.get(), self.mail.get())).place(relx=0.7, rely=0.9, anchor=CENTER, width=90)

    def GuardarUsuari(self, nom, cognom, user, password, tlf, mail):
        arr = [nom, cognom, user, password, tlf, mail]

        d = bbdd.Db()
        count_user = d.SelectUser(user)[0][0]

        if count_user != 0:
            messagebox.showinfo(title="Info", message="Nom d'usuari ja creat!")
        else:
            d.InsertUser(arr)
            messagebox.showinfo(title="Info", message="Usuari creat!")

            self.nom_usuari.set("")
            self.cognom_usuari.set("")
            self.user.set("")
            self.contrasenya.set("")
            self.tlf.set("")
            self.mail.set("")

    def log(self, user, password):

        d = bbdd.Db()
        count_log = d.SelectUserPass(user, password)[0][0]

        if count_log != 1:
            messagebox.showinfo(title="Info", message="Usuari no existent!")
        else:
            self.root.destroy()
            main_window = Tk()
            app = PaginaMoviments(main_window, self.username.get())
            main_window.mainloop()


class PaginaMoviments:
    def __init__(self, root, user):
        self.user = user
        self.root = root
        self.root.title("BANK")
        self.root.geometry("1200x600")

        # layout all of the main containers
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # create all of the main containers
        self.top_frame = Frame(self.root, bg='navy', width=1200, height=100, pady=3)
        self.main_frame = Frame(self.root, bg='#11DBF2', width=1200, height=500, padx=3, pady=3)

        self.top_frame.grid(row=0, sticky="ew")
        self.main_frame.grid(row=1, sticky="nsew")

        self.Title()

        # create the center widgets
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.ctr_mid = Frame(self.main_frame, bg='#11DBF2', width=250, height=190, padx=3, pady=3)
        self.ctr_mid.grid(row=0, column=1, sticky="nsew")

        self.btn_ingres = Button(self.ctr_mid, fg="white", bg="navy", font="HELVETICA 10 bold", text="Ingres",
                                relief="flat", cursor="hand1", width=30, height=5, command=self.InsertIngresar
                                )
        self.btn_ingres.place(relx=0.35, rely=0.3, anchor=CENTER)
        self.btn_retirar = Button(self.ctr_mid, fg="white", bg="navy", font="HELVETICA 10 bold", text="Retirar",
                                relief="flat", cursor="hand1", width=30, height=5, command=self.InsertRetirar
                                )
        self.btn_retirar.place(relx=0.65, rely=0.3, anchor=CENTER)
        self.btn_pagament = Button(self.ctr_mid, fg="white", bg="navy", font="HELVETICA 10 bold", text="Pagaments",
                                relief="flat", cursor="hand1", width=30, height=5, command=self.InsertPagament
                                )
        self.btn_pagament.place(relx=0.35, rely=0.7, anchor=CENTER)
        self.btn_comptes = Button(self.ctr_mid, fg="white", bg="navy", font="HELVETICA 10 bold", text="Comptes",
                                relief="flat", cursor="hand1", width=30, height=5, command=self.comptes_window
                                )
        self.btn_comptes.place(relx=0.65, rely=0.7, anchor=CENTER)

        self.btn_newCompte = Button(self.ctr_mid, text="Crear Compte", relief="flat", background="navy",
                                 cursor="hand1",
                                 foreground="white", command=self.CrearCompte).place(relx=0.9, rely=0.9, anchor=CENTER,
                                                                                     width=90)
        self.btn_perfil = Button(self.ctr_mid, text="Pefil", relief="flat", background="navy",
                                    cursor="hand1",
                                    foreground="white", command=self.UpdateUser).place(relx=0.9, rely=0.1, anchor=CENTER,
                                                                width=90)

    def Title(self):
        # create the widgets for the top frame
        self.model_label = Label(self.top_frame, text='London Bank', fg="white", bg="navy",
                                 font="HELVETICA 30 bold")

        # layout the widgets in the top frame
        self.model_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def comptes_window(self):
        self.root.destroy()
        main_window = Tk()
        app = PaginaComptes(main_window, self.user)
        main_window.mainloop()

    def InsertIngresar(self):
        self.tramitI = StringVar()
        self.tipus = "Ingres"

        pop = Toplevel(self.main_frame, background="#11DBF2")
        pop.geometry("400x300")

        label_ingres = Label(pop, foreground="navy", background="#11DBF2", text="Ingres",
                        font="HELVETICA 12 bold").place(relx=0.5, rely=0.2, anchor=CENTER)

        option = []
        self.clicked = StringVar()

        d = bbdd.Db()
        id_usuari = d.SelectId(self.user)[0][0]
        print(id_usuari)

        comptes = d.SelectCompte(id_usuari)
        print(comptes)

        for index, tuple in enumerate(comptes):
            option.append(tuple[1])

        if option:
            self.clicked.set(option[0])

            self.drop = OptionMenu(pop, self.clicked, *option)
            self.drop.place(relx=0.5, rely=0.35, anchor=CENTER)

        if comptes:
            label_tramit = Label(pop, foreground="navy", background="#11DBF2", text="Tramit:",
                        font="HELVETICA 8 bold").place(relx=0.15, rely=0.5, anchor=CENTER)

            txt_tramit = Entry(pop, textvariable=self.tramitI).place(relx=0.45, rely=0.5, anchor=CENTER)

            btn_tramit = Button(pop, text="Tramit", relief="flat", background="navy", cursor="hand1",
                                 foreground="white", command= lambda: self.InsertTable(self.tipus)).place(relx=0.7, rely=0.7, anchor=CENTER, width=90)

    def InsertRetirar(self):
        self.tramitI = StringVar()
        self.tipus = "Retirar"

        pop = Toplevel(self.main_frame, background="#11DBF2")
        pop.geometry("400x300")

        label_ingres = Label(pop, foreground="navy", background="#11DBF2", text="Retirar",
                        font="HELVETICA 12 bold").place(relx=0.5, rely=0.2, anchor=CENTER)

        option = []
        self.clicked = StringVar()

        d = bbdd.Db()
        id_usuari = d.SelectId(self.user)[0][0]
        print(id_usuari)

        comptes = d.SelectCompte(id_usuari)
        print(comptes)

        for index, tuple in enumerate(comptes):
            option.append(tuple[1])

        if option:
            self.clicked.set(option[0])

            self.drop = OptionMenu(pop, self.clicked, *option)
            self.drop.place(relx=0.5, rely=0.35, anchor=CENTER)

        if comptes:
            label_tramit = Label(pop, foreground="navy", background="#11DBF2", text="Tramit:",
                            font="HELVETICA 8 bold").place(relx=0.15, rely=0.5, anchor=CENTER)
            txt_tramit = Entry(pop, textvariable=self.tramitI).place(relx=0.45, rely=0.5, anchor=CENTER)

            btn_tramit = Button(pop, text="Tramit", relief="flat", background="navy", cursor="hand1",
                                 foreground="white", command= lambda: self.InsertTable(self.tipus)).place(relx=0.7, rely=0.7, anchor=CENTER, width=90)

    def InsertPagament(self):
        self.tramitI = StringVar()
        self.tipus = "Pagament"

        pop = Toplevel(self.main_frame, background="#11DBF2")
        pop.geometry("400x300")

        label_ingres = Label(pop, foreground="navy", background="#11DBF2", text="Pagament",
                        font="HELVETICA 12 bold").place(relx=0.5, rely=0.2, anchor=CENTER)

        option = []
        self.clicked = StringVar()

        d = bbdd.Db()
        id_usuari = d.SelectId(self.user)[0][0]
        print(id_usuari)

        comptes = d.SelectCompte(id_usuari)
        print(comptes)

        for index, tuple in enumerate(comptes):
            option.append(tuple[1])

        if option:
            self.clicked.set(option[0])

            self.drop = OptionMenu(pop, self.clicked, *option)
            self.drop.place(relx=0.5, rely=0.35, anchor=CENTER)

        if comptes:
            label_tramit = Label(pop, foreground="navy", background="#11DBF2", text="Tramit:",
                            font="HELVETICA 8 bold").place(relx=0.15, rely=0.5, anchor=CENTER)
            txt_tramit = Entry(pop, textvariable=self.tramitI).place(relx=0.45, rely=0.5, anchor=CENTER)

            btn_tramit = Button(pop, text="Tramit", relief="flat", background="navy", cursor="hand1",
                                 foreground="white", command= lambda: self.InsertTable(self.tipus)).place(relx=0.7, rely=0.7, anchor=CENTER, width=90)


    def InsertTable(self, tipus):
        d = bbdd.Db()
        tramit =  self.tramitI.get()
        id_compte = d.SelectCompte3(self.clicked.get())[0][0]
        if tipus == "Retirar":
            tramit = str("-" + tramit)

        elif tipus == "Pagament":
            tramit = str("-" + tramit)

        d.InsertMoviment(tipus, tramit, id_compte)
        messagebox.showinfo(title="Info", message="Operacio realitzada!")

    def CrearCompte(self):
        d = bbdd.Db()
        num_compte = int(d.SelectNumCompte()[0][0]) + 1
        id_usuari = d.SelectId(self.user)[0][0]
        d.InsertCompte(str(num_compte), id_usuari)

    def UpdateUser(self):
        self.nom = StringVar()
        self.cognom = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.telefon = StringVar()
        self.mail = StringVar()

        d = bbdd.Db()
        element = d.SelectInfoUser(self.user)

        id = element[0][0]
        nom = element[0][1]
        cognom = element[0][2]
        username = element[0][3]
        password = element[0][4]
        telefon = element[0][5]
        mail = element[0][6]
        creat = element[0][7]

        self.nom.set(nom)
        self.cognom.set(cognom)
        self.username.set(username)
        self.password.set(password)
        self.telefon.set(telefon)
        self.mail.set(mail)

        pop = Toplevel(self.main_frame, background="#11DBF2")
        pop.geometry("400x300")

        label_na = Label(pop, foreground="navy", background="#11DBF2", text="Nom:",
                                 font="HELVETICA 8 bold").place(relx=0.15, rely=0.2, anchor=CENTER)
        txt_na = Entry(pop, textvariable=self.nom).place(relx=0.45, rely=0.2, anchor=CENTER)
        label_su = Label(pop, foreground="navy", background="#11DBF2", text="Cognom:",
                        font="HELVETICA 8 bold").place(relx=0.15, rely=0.3, anchor=CENTER)
        txt_su = Entry(pop, textvariable=self.cognom).place(relx=0.45, rely=0.3, anchor=CENTER)
        label_us = Label(pop, foreground="navy", background="#11DBF2", text="Username:",
                         font="HELVETICA 8 bold").place(relx=0.15, rely=0.4, anchor=CENTER)
        txt_us = Entry(pop, textvariable=self.username).place(relx=0.45, rely=0.4, anchor=CENTER)
        label_pa = Label(pop, foreground="navy", background="#11DBF2", text="Contrasenya:",
                         font="HELVETICA 8 bold").place(relx=0.15, rely=0.5, anchor=CENTER)
        txt_pa = Entry(pop, textvariable=self.password).place(relx=0.45, rely=0.5, anchor=CENTER)
        label_tlf = Label(pop, foreground="navy", background="#11DBF2", text="Telefon:",
                         font="HELVETICA 8 bold").place(relx=0.15, rely=0.6, anchor=CENTER)
        txt_tlf = Entry(pop, textvariable=self.telefon).place(relx=0.45, rely=0.6, anchor=CENTER)
        label_su = Label(pop, foreground="navy", background="#11DBF2", text="Email:",
                         font="HELVETICA 8 bold").place(relx=0.15, rely=0.7, anchor=CENTER)
        txt_su = Entry(pop, textvariable=self.mail).place(relx=0.45, rely=0.7, anchor=CENTER)

        btn_arrendar = Button(pop, text="Editar", relief="flat", background="navy", cursor="hand1",
                                   foreground="white", command=lambda: self.ActualitzarUser(id)).place(relx=0.7, rely=0.85, anchor=CENTER, width=90)

    def ActualitzarUser(self, id):

        arr = [self.nom.get(), self.cognom.get(), self.username.get(), self.password.get(), self.telefon.get(), self.mail.get()]
        d = bbdd.Db()

        if self.user == self.username.get():
            d.UpdateUser(arr, id)
            messagebox.showinfo(title="Info", message="Operacio realitzada!")
        else:
            count = d.SelectUser(self.username.get())[0][0]
            if count == 0:
                d.UpdateUser(arr, id)
                messagebox.showinfo(title="Info", message="Operacio realitzada!")
                self.user = self.username.get()
            else:
                messagebox.showinfo(title="Info", message="Usuari existent!")






class PaginaComptes:
    def __init__(self, root, user):
        self.user = user
        self.root = root
        self.root.title("BANK")
        self.root.geometry("1200x600")

        # layout all of the main containers
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # create all of the main containers
        self.top_frame = Frame(self.root, bg='navy', width=1200, height=100, pady=3)
        self.main_frame = Frame(self.root, bg='#11DBF2', width=1200, height=500, padx=3, pady=3)

        # create the center widgets
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.top_frame.grid(row=0, sticky="ew")
        self.main_frame.grid(row=1, sticky="nsew")

        self.ctr_left = Frame(self.main_frame, bg='#11DBF2', width=350, height=190)
        self.ctr_right = Frame(self.main_frame, bg='#11DBF2', width=550, height=190, padx=3, pady=3)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.ctr_right.grid(row=0, column=1, sticky="nsew")

        self.Title()
        self.BuscadorCompte()
        self.DibuixarLlista()

        self.btn_tornar = Button(self.ctr_right, text="Pagina Inicial", relief="flat", background="navy", cursor="hand1",
                                 foreground="white", command=self.move_window).place(relx=0.9, rely=0.9, anchor=CENTER,
                                                                                     width=90)


    def Title(self):
        # create the widgets for the top frame
        self.model_label = Label(self.top_frame, text='London Bank', fg="white", bg="navy",
                                 font="HELVETICA 30 bold")

        # layout the widgets in the top frame
        self.model_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def move_window(self):
        self.root.destroy()
        main_window = Tk()
        app = PaginaMoviments(main_window, self.user)
        main_window.mainloop()

    def BuscadorCompte(self):
        option = []
        self.clicked = StringVar()

        # BUSCADOR PER ID.
        self.model_label = Label(self.ctr_left, text='Buscador de moviments', fg="navy", bg="#11DBF2",
                                 font="HELVETICA 14 bold")
        self.model_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        d = bbdd.Db()
        id_usuari = d.SelectId(self.user)[0][0]

        comptes = d.SelectCompte(id_usuari)

        for index, tuple in enumerate(comptes):
            option.append(tuple[1])

        if option:
            self.clicked.set(option[0])

            self.drop = OptionMenu(self.ctr_left, self.clicked, *option)
            self.drop.place(relx=0.5, rely=0.2, anchor=CENTER)

            self.btn_search = Button(self.ctr_left, text="Buscar", relief="flat", background="navy", cursor="hand1",
                                     foreground="white", command=self.DibuixarLlista).place(
                relx=0.5, rely=0.3, anchor=CENTER, width=90)

    def DibuixarLlista(self):
        elements = []
        self.saldo = ""


        self.llista = ttk.Treeview(self.ctr_right, columns=(1, 2, 3, 4), show="headings", height="15")
        self.estil = ttk.Style()
        self.estil.theme_use("clam")

        # aixo es el que es vol canviar.
        self.estil.configure("Treeview.Heading", background="navy", relief="flat", foreground="white")
        self.llista.heading(1, text="Id_compte")
        self.llista.heading(2, text="Tipus moviment")
        self.llista.heading(3, text="Import")
        self.llista.heading(4, text="Realitzacio")
        self.llista.column(1, anchor=CENTER)  # modifica alguna caracteristica de la columna
        self.llista.column(2, anchor=CENTER)
        self.llista.column(3, anchor=CENTER)
        self.llista.column(4, anchor=CENTER)
        self.llista.place(relx=0.5, rely=0.4, anchor=CENTER)


        self.model_saldo2 = Label(self.ctr_right, fg="navy", bg="#11DBF2", font="HELVETICA 14 bold")

        d = bbdd.Db()
        if self.clicked.get() != "":
            id = d.SelectCompte2(self.clicked.get())[0][0]
            elements = d.SelectMoviment(id)
            if elements:

                self.saldo = elements[0][5]

                self.model_saldo = Label(self.ctr_right, fg="navy", bg="#11DBF2", font="HELVETICA 14 bold", text='Saldo compte: ' + str(self.saldo))
                self.model_saldo.place(relx=0.8, rely=0.8, anchor=CENTER)

            else:
                self.model_saldo.config(text='Saldo compte: ' + str(0.00))


        for i in elements:
            self.llista.insert('', 'end', value=i)

    def NetejarLlista(self):
        self.llista.delete(*self.llista.get_children())



if __name__ == '__main__':
    main()