import tkinter as tk


class Cuoco(object):

    def __init__(self):
        self.__comande = []  # lista (vuota) delle comande

        # finestra di gestione comande
        self.w_comande = tk.Tk()
        self.w_comande.geometry("300x60+900+200")
        self.w_comande.title("sistema comande")
        self.w_comande.grid()

        self.vAccoda = tk.StringVar()
        self.txt_accoda = tk.Entry(self.w_comande, textvariable=self.vAccoda, width=30)
        self.txt_accoda.grid(row=0, column=0)

        self.btn_accoda_comanda = tk.Button(self.w_comande, text="accoda", command=self.__accoda_comanda)
        self.btn_accoda_comanda.grid(row=0, column=1)

        self.vPrepara = tk.StringVar()
        self.txt_prepara = tk.Entry(self.w_comande, textvariable=self.vPrepara, width=30, state=tk.DISABLED)
        self.txt_prepara.grid(row=1, column=0)

        self.btn_prepara_comanda = tk.Button(self.w_comande, text="prepara", command=self.__prepara_comanda)
        self.btn_prepara_comanda.grid(row=1, column=1)

        self.w_comande.mainloop()

    def __accoda_comanda(self):
        self.__comande.append(self.vAccoda.get())
        self.vAccoda.set("")

    def __prepara_comanda(self):
        if len(self.__comande) > 0:
            self.vPrepara.set(self.__comande.pop(0))
        else:
            self.vPrepara.set("")


def main():
    Cuoco()


main()
