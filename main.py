import customtkinter as ctk
from ui.welcome_page import WelcomePage as welcome_page
from ui.perftool_page import PerfToolPage as perftool_page

# 设置 CustomTkinter 的外观模式和主题
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# 主窗口类
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("PerfTool Application")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        # 定义两个页面
        self.welcome_page = welcome_page(self)
        self.perftool_page = perftool_page(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 显示 Welcome 页面
        self.show_page(self.welcome_page)

    def show_page(self, page):
        """切换页面"""
        page.tkraise()

# 启动应用
if __name__ == "__main__":
    app = App()
    app.mainloop()