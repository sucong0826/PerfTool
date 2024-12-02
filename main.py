# import tkinter as tk
# from tkinter import messagebox

# def on_button_click():
#     messagebox.showinfo("hello!", "button clicked!")

# app = tk.Tk()
# app.title("cross-platform tkinter app")
# app.geometry("400x300")

# label = tk.Label(app, text="welcome to tkinter gui", font=("Arial", 16))
# label.pack(pady=20)

# button = tk.Button(app, text="click me", command=on_button_click)
# button.pack(pady=10)

# app.mainloop()

import customtkinter as ctk

# 设置 CustomTkinter 的外观模式和主题
ctk.set_appearance_mode("dark")  # 模式：light, dark, system
ctk.set_default_color_theme("blue")  # 主题：blue, green, dark-blue

# 创建主窗口
app = ctk.CTk()
app.title("CustomTkinter App")
app.geometry("400x300")

# 添加控件
label = ctk.CTkLabel(app, text="Welcome to CustomTkinter!", font=("Arial", 16))
label.pack(pady=20)

button = ctk.CTkButton(app, text="Click Me", command=lambda: print("Button clicked"))
button.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="Enter something...")
entry.pack(pady=10)

# 启动应用
app.mainloop()
