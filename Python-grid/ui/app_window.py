import tkinter as tk
from tkinter import ttk
from service.task_service import TaskService
import uuid


class AppWindow(tk.Tk):

    def __init__(self, task_service: TaskService) -> None:
        super().__init__()
        self._task_service = task_service

        self.title("Tkinter desde POO")
        self.geometry("800x600")
        self.resizable(False, False)
        

        # Widgets
        self.create_widgets()

    def create_widgets(self) -> None:

        label = tk.Label(self, text="Bienvenido a mi App")
        label.grid(row=0, column=0, columnspan=2, pady=10)


        #tk.Label(self, text="Título").pack()
        #self.entry_title = tk.Entry(self)
        #self.entry_title.pack()

        # Titulo
        tk.Label(self, text="Título: ").grid(row=1, column=0)
        self.entry_title = tk.Entry(self)
        self.entry_title.grid(row=1, column=1, padx=10, pady=5)


        #tk.Label(self, text="Descripción").pack()
        #self.entry_desc = tk.Entry(self)
        #self.entry_desc.pack()

        tk.Label(self, text="Descripción").grid(row=2, column=0)
        self.entry_desc = tk.Entry(self)
        self.entry_desc.grid(row=2, column=1, padx=10, pady=5)

        button = tk.Button(self, text="Capturar",
                           command=self.add_task)
        
        button.grid(row=3, column=0, pady=10)


        self.grid = ttk.Treeview(self, columns=("Column1", "Column2"), height= 10)
        self.grid.column("#0", width=150, stretch=True)
        self.grid.column("Column1", width=300, stretch=True, anchor="center")
        self.grid.column("Column2", width=250, stretch=True, anchor="center")

        self.grid.heading("#0", text="Título")
        self.grid.heading("Column1", text="Descripción")
        self.grid.heading("Column2", text="id")

        self.grid.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="e")

        self.show_table()


    def show_table(self):
        for task in self._task_service.get_all_task():
            self.grid.insert("", "end", text= task.title, values= (task.description, task.uuid))

       
        
    def add_task(self):
        title = self.entry_title.get()
        description = self.entry_desc.get()


        if not title or not description:
            print("No puedes dejar campos vacíos")
        else:
             task = self._task_service.create_one_task(title, description)
             self.grid.insert("", "end", text= task.title, values= (task.description, task.uuid))
        
        return
      
        
    
        
        

    #     label_title = tk.Label(self, text="Nombre: ")
    #     label_title.pack()
    #     self.title = tk.Entry(self)
    #     self.title.pack()

    #     label_desc = tk.Label(self, text="Apellido: ")
    #     label_desc.pack()
    #     self.desc = tk.Entry(self)
    #     self.desc.pack()


    #     button = tk.Button(self, text="Capturar",
    #                        command=self.show_message)
        
    #    button.pack()
       
    # def show_message(self) -> None:

    #     for task in self._task_service.get_all_task():
    #         print(f"{task.uuid} - {task.title} - {task.description}")
        
   
 