import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import psutil
import threading
import time

class CPUMonitorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CPU Monitor")
        self.geometry("800x600")

        # 创建图形显示区
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # 创建按钮和标签
        self.start_button = ttk.Button(self, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.average_label = ttk.Label(self, text="Average CPU Usage: N/A")
        self.average_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.cpu_data = []

    def start_monitoring(self):
        self.cpu_data = []
        self.monitoring = True
        threading.Thread(target=self.collect_cpu_data).start()
    
    def collect_cpu_data(self):
        start_time = time.time()
        while time.time() - start_time < 60:
            cpu_usage = psutil.cpu_percent(interval=1)
            self.cpu_data.append(cpu_usage)
            self.update_plot()
        
        self.monitoring = False
        self.calculate_average()

    def update_plot(self):
        self.ax.clear()
        self.ax.plot(self.cpu_data, label="CPU Usage")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("CPU Usage (%)")
        self.ax.legend()
        self.canvas.draw()

    def calculate_average(self):
        if self.cpu_data:
            avg_cpu_usage = sum(self.cpu_data) / len(self.cpu_data)
            self.average_label.config(text=f"Average CPU Usage: {avg_cpu_usage:.2f}%")

if __name__ == "__main__":
    app = CPUMonitorApp()
    app.mainloop()
