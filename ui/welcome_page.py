import customtkinter as ctk

class WelcomePage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")  # 使用 grid 布局覆盖整个窗口

        label = ctk.CTkLabel(self, text="Welcome to the Application!", font=("Arial", 16))
        label.pack(pady=20)

        button = ctk.CTkButton(self, text="Go to Main Page", command=lambda: parent.show_page(parent.perftool_page))
        button.pack(pady=10)