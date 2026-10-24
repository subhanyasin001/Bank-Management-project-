import tkinter as tk
from tkinter import messagebox
from bank import BankSystem

# Bank system ko initialize kiya
bank = BankSystem()

# Main Window (GUI)
root = tk.Tk()
root.title("OOP Bank System")
root.geometry("350x500")

tk.Label(root, text="🏦 OOP Bank System", font=("Arial", 16, "bold")).pack(pady=20)

# 1. Create Account Window Function
def open_create_window():
    win = tk.Toplevel(root)
    win.title("Create Account")
    win.geometry("300x320")

    tk.Label(win, text="Name:").pack(pady=2)
    e_name = tk.Entry(win)
    e_name.pack()

    tk.Label(win, text="Email:").pack(pady=2)
    e_email = tk.Entry(win)
    e_email.pack()

    tk.Label(win, text="4-Digit PIN:").pack(pady=2)
    e_pin = tk.Entry(win, show="*")
    e_pin.pack()

    tk.Label(win, text="Account Number (e.g., ACC123):").pack(pady=2)
    e_acc = tk.Entry(win)
    e_acc.pack()

    def submit():
        name = e_name.get()
        email = e_email.get()
        pin = e_pin.get()
        acc_no = e_acc.get()

        if name and email and pin and acc_no:
            success, msg = bank.create_account(name, email, pin, acc_no)
            if success:
                messagebox.showinfo("Success", msg)
                win.destroy()
            else:
                messagebox.showerror("Error", msg)
        else:
            messagebox.showwarning("Warning", "Please fill all fields!")

    tk.Button(win, text="Create Account", command=submit, bg="green", fg="white").pack(pady=15)


# 2. Deposit Window Function
def open_deposit_window():
    win = tk.Toplevel(root)
    win.title("Deposit Money")
    win.geometry("300x250")

    tk.Label(win, text="Account Number:").pack(pady=2)
    e_acc = tk.Entry(win)
    e_acc.pack()

    tk.Label(win, text="PIN:").pack(pady=2)
    e_pin = tk.Entry(win, show="*")
    e_pin.pack()

    tk.Label(win, text="Amount:").pack(pady=2)
    e_amount = tk.Entry(win)
    e_amount.pack()

    def submit():
        acc_no = e_acc.get()
        pin = e_pin.get()
        try:
            amount = int(e_amount.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric amount!")
            return

        acc = bank.authenticate(acc_no, pin)
        if acc:
            success, msg = acc.deposit(amount)
            bank.save_data()
            messagebox.showinfo("Success", msg)
            win.destroy()
        else:
            messagebox.showerror("Error", "Invalid Account Number or PIN!")

    tk.Button(win, text="Deposit", command=submit, bg="blue", fg="white").pack(pady=15)


# 3. Withdraw Window Function
def open_withdraw_window():
    win = tk.Toplevel(root)
    win.title("Withdraw Money")
    win.geometry("300x250")

    tk.Label(win, text="Account Number:").pack(pady=2)
    e_acc = tk.Entry(win)
    e_acc.pack()

    tk.Label(win, text="PIN:").pack(pady=2)
    e_pin = tk.Entry(win, show="*")
    e_pin.pack()

    tk.Label(win, text="Amount:").pack(pady=2)
    e_amount = tk.Entry(win)
    e_amount.pack()

    def submit():
        acc_no = e_acc.get()
        pin = e_pin.get()
        try:
            amount = int(e_amount.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric amount!")
            return

        acc = bank.authenticate(acc_no, pin)
        if acc:
            success, msg = acc.withdraw(amount)
            if success:
                bank.save_data()
                messagebox.showinfo("Success", msg)
                win.destroy()
            else:
                messagebox.showerror("Error", msg)
        else:
            messagebox.showerror("Error", "Invalid Account Number or PIN!")

    tk.Button(win, text="Withdraw", command=submit, bg="orange", fg="white").pack(pady=15)


# 4. View Details Window Function
def open_details_window():
    win = tk.Toplevel(root)
    win.title("Account Details")
    win.geometry("300x220")

    tk.Label(win, text="Account Number:").pack(pady=2)
    e_acc = tk.Entry(win)
    e_acc.pack()

    tk.Label(win, text="PIN:").pack(pady=2)
    e_pin = tk.Entry(win, show="*")
    e_pin.pack()

    def submit():
        acc_no = e_acc.get()
        pin = e_pin.get()

        acc = bank.authenticate(acc_no, pin)
        if acc:
            details = f"Name: {acc.name}\nEmail: {acc.email}\nAcc No: {acc.acc_number}\nBalance: Rs. {acc.balance}"
            messagebox.showinfo("Account Details", details)
            win.destroy()
        else:
            messagebox.showerror("Error", "Invalid Account Number or PIN!")

    tk.Button(win, text="View Details", command=submit, bg="purple", fg="white").pack(pady=15)


# Main Menu Buttons
tk.Button(root, text="1. Create Account", width=25, height=2, command=open_create_window).pack(pady=8)
tk.Button(root, text="2. Deposit Money", width=25, height=2, command=open_deposit_window).pack(pady=8)
tk.Button(root, text="3. Withdraw Money", width=25, height=2, command=open_withdraw_window).pack(pady=8)
tk.Button(root, text="4. View Details", width=25, height=2, command=open_details_window).pack(pady=8)

# Run the App
root.mainloop()