import tkinter as tk
from gui_manager import GerenciadorGUI

def main():
    root = tk.Tk()
    app = GerenciadorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()