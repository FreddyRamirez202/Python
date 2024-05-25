import tkinter as tk
from tkinter import simpledialog, messagebox

class FinancialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión Financiera")
        self.salary = 1600000
        self.debts = []

        self.init_ui()

    def init_ui(self):
        tk.Label(self.root, text="Gestión Financiera").pack()

        tk.Button(self.root, text="Establecer Sueldo", command=self.set_salary).pack(pady=5)
        tk.Button(self.root, text="Gestionar Deudas", command=self.manage_debts).pack(pady=5)
        tk.Button(self.root, text="Resumen Financiero", command=self.show_summary).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)

    def set_salary(self):
        salary = simpledialog.askinteger("Sueldo", "Este fue tu sueldo este mes, verdad?", initialvalue=self.salary)
        if salary is not None:
            self.salary = salary
            messagebox.showinfo("Sueldo", f"Sueldo establecido en: {self.salary} pesos")

    def manage_debts(self):
        debt_win = tk.Toplevel(self.root)
        debt_win.title("Gestionar Deudas")
        
        tk.Label(debt_win, text="Deuda:").pack()
        self.debt_entry = tk.Entry(debt_win)
        self.debt_entry.pack()

        tk.Button(debt_win, text="Añadir Deuda", command=self.add_debt).pack(pady=5)
        tk.Button(debt_win, text="Modificar Deuda", command=self.modify_debt).pack(pady=5)
        tk.Button(debt_win, text="Eliminar Deuda", command=self.remove_debt).pack(pady=5)
        tk.Button(debt_win, text="Cerrar", command=debt_win.destroy).pack(pady=5)

    def add_debt(self):
        try:
            debt = int(self.debt_entry.get())
            self.debts.append(debt)
            messagebox.showinfo("Deudas", "Deuda añadida correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico.")

    def modify_debt(self):
        try:
            index = simpledialog.askinteger("Modificar Deuda", "Índice de la deuda a modificar:")
            if index is not None and 0 <= index < len(self.debts):
                new_value = simpledialog.askinteger("Nueva Deuda", "Nuevo valor de la deuda:")
                if new_value is not None:
                    self.debts[index] = new_value
                    messagebox.showinfo("Deudas", "Deuda modificada correctamente.")
                else:
                    messagebox.showwarning("Cancelar", "No se ha modificado la deuda.")
            else:
                messagebox.showwarning("Índice inválido", "Por favor ingrese un índice válido.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico.")

    def remove_debt(self):
        try:
            index = simpledialog.askinteger("Eliminar Deuda", "Índice de la deuda a eliminar:")
            if index is not None and 0 <= index < len(self.debts):
                self.debts.pop(index)
                messagebox.showinfo("Deudas", "Deuda eliminada correctamente.")
            else:
                messagebox.showwarning("Índice inválido", "Por favor ingrese un índice válido.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico.")

    def show_summary(self):
        total_debt = sum(self.debts)
        remaining_salary = self.salary - total_debt
        summary = f"Sueldo: {self.salary} pesos\nTotal de Deudas: {total_debt} pesos\nSueldo Restante: {remaining_salary} pesos"
        messagebox.showinfo("Resumen Financiero", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialApp(root)
    root.mainloop()
