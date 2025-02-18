import customtkinter as ctk

class PerfToolPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")  # 使用 grid 布局覆盖整个窗口

        # divide the frame into 3 panels
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=7)
        self.grid_columnconfigure(0, weight=1)

        # panel 1 for configuration 
        self.config_panel = ctk.CTkFrame(self, corner_radius=0)
        self.config_panel.grid(row=0, column=0, sticky="nsew")

        # for i in range(5): # 4 rows
        #     # self.config_panel.grid_rowconfigure(i, weight=1)
        # for j in range(5): # 5 columns
        #     self.config_panel.grid_columnconfigure(j, weight=1)

        headers = ["Process ID", "Metrics", "Test Duration", "Sample Interval", "Algorithm", "Actions"]
        for col, header in enumerate(headers):
            label = ctk.CTkLabel(self.config_panel, text=header, font=("Arial", 12, "bold"), height=30)
            label.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

        metrics = ["CPU", "GPU", "Memory", "Power"]
        self.process_id_inputs = []
        self.duration_inputs = []
        self.interval_inputs = []
        self.algorithm_droplists = []

        for row, metric in enumerate(metrics, start=1):
            process_id_input = ctk.CTkEntry(self.config_panel, placeholder_text="process id number", height=30)
            process_id_input.grid(row=row, column=0, padx=5, pady=5, sticky="nsew")
            self.process_id_inputs.append(process_id_input)

            metric_label = ctk.CTkLabel(self.config_panel, text=metric, font=("Arial", 12), height=30)
            metric_label.grid(row=row, column=1, padx=5, pady=5, sticky="nsew")

            test_duration_input = ctk.CTkEntry(self.config_panel, placeholder_text="seconds", height=30)
            test_duration_input.grid(row=row, column=2, padx=5, pady=5, sticky="nsew")
            self.duration_inputs.append(test_duration_input)

            sample_duration_input = ctk.CTkEntry(self.config_panel, placeholder_text="milliseconds", height=30)
            sample_duration_input.grid(row=row, column=3, padx=5, pady=5, sticky="nsew")
            self.interval_inputs.append(sample_duration_input)

            # algorithm droplist
            algorithms = ["Average", "Min-Max"]
            algorithms_var = ctk.StringVar(value=algorithms[0])
            droplist = ctk.CTkComboBox(self.config_panel, values=algorithms, variable=algorithms_var, height=30)
            droplist.grid(row=row, column=4, padx=5, pady=5, sticky="nsew")
            self.algorithm_droplists.append(algorithms_var)
        

        # panel 2 for perf running stats
        self.perf_running_panel = ctk.CTkFrame(self, corner_radius=0)
        self.perf_running_panel.grid(row=1, column=0, sticky="nsew")
        label3 = ctk.CTkLabel(self.perf_running_panel, text="Bottom Area", font=("Arial", 16))
        label3.pack(expand=True)

        print("Row 0 weight:", self.grid_rowconfigure(0))
        print("Row 1 weight:", self.grid_rowconfigure(1))