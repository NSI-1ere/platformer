import tkinter as tk
import subprocess
from pathlib import Path
from PIL import Image, ImageTk
from itertools import count, cycle
import os

class ImageLabel(tk.Label):
    """Un Label qui affiche des images et les joue si ce sont des GIFs."""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

root = tk.Tk()
root.title("Launcher")
root.geometry("1000x373")
root.resizable(False, False)

# Conteneur principal
container = tk.Frame(root, width=600, height=300)
container.pack(fill='both', expand=True)

# Chemin d'accès
chemin_repertoire = os.path.dirname(os.path.abspath(__file__))


lbl = ImageLabel(container)
lbl.place(relx=0.5, rely=0.5, anchor='center')  # Centré dans le conteneur
lbl.load(chemin_repertoire + r'.\Launcher.gif')

label_title = tk.Label(container, text="Platformer", font=('Papyrus', 30, 'bold'), bg="grey", fg="black")
label_title.place(relx=0.5, rely=0.2, anchor='center')

# Chemin du programme Python à exécuter
chemin_platformer = Path(chemin_repertoire + r".\main.py").resolve()

# Exécuter le programme
def run_program():
    # Ferme la fenêtre principale
    root.destroy()
    # Exécuter le programme
    subprocess.run(["python", chemin_platformer])

# Créer le bouton
button_run = tk.Button(container, text="Lancer le jeu", command=run_program, font=('Arial', 12, 'bold'), bg="blue", fg="white", cursor="hand2")  
button_run.place(relx=0.5, rely=0.7, anchor='center')  # Position centré un peu plus bas que le centre
root.bind("<Return>", lambda event: run_program())
root.bind("<Escape>", lambda event: root.destroy())

root.mainloop()
