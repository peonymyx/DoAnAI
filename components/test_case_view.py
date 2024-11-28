# components/test_case_view.py
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class TestCaseView:
    def __init__(self, parent, add_items_callback):
        self.parent = parent
        self.add_items_callback = add_items_callback
        self.selected_case = tk.StringVar()

    def create(self):
        # Frame tạo khung, padding 10px
        frame = ttk.LabelFrame(
            self.parent,
            text="SỐ SẢN PHẨM KIỂM THỬ",
            padding=10,
            bootstyle="primary"
        )
        frame.pack(fill=tk.X, pady=10)

        case_frame = ttk.Frame(frame)
        case_frame.pack(fill=tk.X)

        cases = (('50', '50'),
                 ('100', '100'),
                 ('200', '200'),
                 ('500', '500'),
                 ('1000', '1000'),
                 ('2000', '2000'))
        
        for case in cases:
            ttk.Radiobutton(
                case_frame,
                text=case[0],
                value=case[1],
                variable=self.selected_case
            ).pack(side=tk.LEFT, expand=tk.YES, padx=5)

        ttk.Button(
            frame,
            text="CHỌN CASE",
            command=self.on_add_items,
            bootstyle="success"
        ).pack(side=tk.LEFT, padx=5, pady=(10, 0), expand=tk.YES)

        ttk.Button(
            frame,
            text="HỦY CHỌN CASE",
            command=self.on_reset_case,
            bootstyle="danger"
        ).pack(side=tk.RIGHT, padx=5, pady=(10, 0), expand=tk.YES)

        return frame
    
    def on_add_items(self):
        self.add_items_callback(self.selected_case.get())

    def on_reset_case(self):
        self.selected_case.set('0')
        self.on_add_items()