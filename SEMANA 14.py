import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Lista de eventos
        self.eventos = []

        # Frames para organizar los componentes
        self.frame_lista = ttk.Frame(root)
        self.frame_lista.pack(pady=10)

        self.frame_entradas = ttk.Frame(root)
        self.frame_entradas.pack(pady=10)

        self.frame_botones = ttk.Frame(root)
        self.frame_botones.pack(pady=10)

        # Lista de eventos (TreeView)
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Entradas para la fecha, hora y descripción
        ttk.Label(self.frame_entradas, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_fecha = ttk.Entry(self.frame_entradas)
        self.entrada_fecha.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entradas, text="Hora (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_hora = ttk.Entry(self.frame_entradas)
        self.entrada_hora.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entradas, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.entrada_descripcion = ttk.Entry(self.frame_entradas)
        self.entrada_descripcion.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5,
                                                                                                pady=5)
        ttk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1,
                                                                                                  padx=5, pady=5)
        ttk.Button(self.frame_botones, text="Salir", command=root.destroy).grid(row=0, column=2, padx=5, pady=5)

        self.actualizar_lista()

    def agregar_evento(self):
        fecha = self.entrada_fecha.get()
        hora = self.entrada_hora.get()
        descripcion = self.entrada_descripcion.get()

        if fecha and hora and descripcion:
            self.eventos.append({"fecha": fecha, "hora": hora, "descripcion": descripcion})
            self.actualizar_lista()
            self.entrada_fecha.delete(0, tk.END)
            self.entrada_hora.delete(0, tk.END)
            self.entrada_descripcion.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            respuesta = messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar el evento seleccionado?")
            if respuesta:
                indice = int(seleccion[0][1:], 16) - 1
                del self.eventos[indice]
                self.actualizar_lista()
        else:
            messagebox.showerror("Error", "Por favor, seleccione un evento para eliminar.")

    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for evento in self.eventos:
            self.tree.insert("", tk.END, values=(evento["fecha"], evento["hora"], evento["descripcion"]))


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


