from tkinter import *
from tkinter import ttk

class Erfassungsformular:

    def __init__(self, master):
        
        master.title("Sitzverteilung nach Hare-Niemeyer")
        master.resizable(True, True)
        master.configure(background = "#b7cceb")

        self.style = ttk.Style()
        self.style.configure("TFrame", background = "#b7cceb")
        self.style.configure("TButton", background = "#b7cceb")
        self.style.configure("TLabel", background = "#b7cceb", font = ("Arial", 11))
        self.style.configure("Header.TLabel", font = ("Arial", 18, "bold"))
        self.style.configure("Entry.TFrame", background = "#b7cceb")
                
        #Im Master-Frame kommt an oberster Stelle der Title-Frame
        self.frame_header = ttk.Frame(master, width = 650, height = 400)
        self.frame_header.pack()
        self.frame_header.title = "Hare-Niemeyer-Rechner"
        self.logo = PhotoImage(file = 'logo.png')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = "Sitzverteilung im Hessischen Landtag", style = "Header.TLabel").grid(row = 0, column = 1)
        ttk.Label(self.frame_header, text = "Berechnung der Sitzverteilung anhand der Wahlergebnisse").grid(row = 1, column = 1)

        #Unter dem Master-Frame sollen Notebooks dargestellt werden.
        notebook = ttk.Notebook(master)
        notebook.pack()

        #Im Notebook zwei "Seiten" (auch Frames)
        nbframe1 = ttk.Frame(notebook)
        nbframe2 = ttk.Frame(notebook)
        nbframe1.configure(style = "Entry.TFrame")
        notebook.add(nbframe1, text = "Eingabe")
        notebook.add(nbframe2, text = "Ausgabe")
        # notebook.tab(0, padding = 20)
        # notebook.tab(1, padding = 20)
        
        # Im nbframe1 der Frame mit den Eckdaten der Landtagswahl: abgegebene Landesstimmen und 5%-Hürde (wird ausgerechnet):
        self.frame_eckdaten_wahl = ttk.Frame(nbframe1)
        self.frame_eckdaten_wahl.pack()
        ttk.Label(self.frame_eckdaten_wahl, text = 'Abgegebene Landesstimmen:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_eckdaten_wahl, text = '(5%-Hürde:    )').grid(row = 1, column = 1, padx = 5, sticky = 'sw')
        self.entry_landesstimmen = ttk.Spinbox(self.frame_eckdaten_wahl, width = 24).grid(row = 1, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_eckdaten_wahl, text = '').grid(row = 1, column = 2)

        # darunter dann die Felder zur Eintragung der Parteien mit ihrem jeweiligen Ergebnis:        
        self.frame_parteien = ttk.Frame(nbframe1)
        self.frame_parteien.pack()
        ttk.Label(self.frame_parteien, text = "Partei:").grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_parteien, text = "Stimmen:").grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_parteien, text = "Prozent:").grid(row = 0, column = 2, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_parteien, text = "Direktmandate:").grid(row = 0, column = 3, padx = 5, sticky = 'sw')
        self.name_partei1 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 1, column = 0, padx = 5, pady = 5)
        self.stimmen_partei1 = ttk.Spinbox(self.frame_parteien, width = 24).grid(row = 1, column = 1, padx = 5, pady = 5)
        self.prozent_partei1 = ttk.Spinbox(self.frame_parteien, width = 24).grid(row = 1, column = 2, padx = 5, pady = 5)
        self.direktmandate_partei1 = ttk.Spinbox(self.frame_parteien, width = 24).grid(row = 1, column = 3, padx = 5, pady = 5)
        
        # self.partei2 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 2, column = 0, padx = 5, pady = 5)
        # self.stimmen_partei2 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 2, column = 1, padx = 5, pady = 5)
        # self.direktmandate_partei1 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 2, column = 2, padx = 5, pady = 5)
        # self.partei3 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 3, column = 0, padx = 5, pady = 5)
        # self.stimmen_partei3 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 3, column = 1, padx = 5, pady = 5)
        # self.direktmandate_partei1 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 3, column = 2, padx = 5, pady = 5)
        # self.partei4 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 4, column = 0, padx = 5, pady = 5)
        # self.stimmen_partei4 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 4, column = 1, padx = 5, pady = 5)
        # self.direktmandate_partei1 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 4, column = 2, padx = 5, pady = 5)
        # self.partei5 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 5, column = 0, padx = 5, pady = 5)
        # self.stimmen_partei5 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 5, column = 1, padx = 5, pady = 5)
        # self.direktmandate_partei1 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 5, column = 2, padx = 5, pady = 5)
        # self.partei6 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 6, column = 0, padx = 5, pady = 5)
        # self.stimmen_partei6 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 6, column = 1, padx = 5, pady = 5)
        # self.direktmandate_partei1 = ttk.Entry(self.frame_parteien, width = 24).grid(row = 6, column = 2, padx = 5, pady = 5)

        self.button_submit = ttk.Button(self.frame_parteien, text = "Eingabe").grid(row = 7, column = 1, padx = 5, pady = 5)




def main():

    root = Tk()
    erfassungsformular = Erfassungsformular(root)
    root.mainloop()

if __name__ == "__main__": main()