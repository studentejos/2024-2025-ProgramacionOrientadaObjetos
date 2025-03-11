import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        # Entrada de tarea
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=10, fill=tk.X)
        self.task_entry.focus()

        # Botones
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=5)

        self.add_button = tk.Button(self.button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(self.button_frame, text="Marcar Completada", command=self.mark_completed)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12))
        self.task_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.mark_completed())
        self.root.bind("<C>", lambda event: self.mark_completed())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<D>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor escribe una tarea.")

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            current_text = self.task_listbox.get(index)
            if not current_text.startswith("[✔]"):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"[✔] {current_text}")
        else:
            messagebox.showinfo("Selecciona una Tarea", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected[0])
        else:
            messagebox.showinfo("Selecciona una Tarea", "Selecciona una tarea para eliminar.")