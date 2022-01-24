# coding: UTF-8
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import serial
import threading
import os
 

# port1 = serial.Serial(
#                         port='COM8',
#                         baudrate=115200,
#                         bytesize=serial.EIGHTBITS,
#                         parity=serial.PARITY_NONE,
#                         stopbits=serial.STOPBITS_ONE,
#                         timeout=None
#                     )

class SimpleTerminal:
    def __init__(self) -> None:
        # 通信で用いるLoRaボードとのシリアルポート
        # port1.write(b'comm $\r\n')    
        self.windowConfig()

    def windowConfig(self):
        self.root = tk.Tk()
        self.root.geometry("400x300+0+0")
        self.root.title('SimpleTerminal')
        # 入力
        self.frame_1 = tk.Frame(self.root, padx=5, pady=2)
        self.frame_1.pack(fill= tk.X)

        self.text = tk.Entry(self.frame_1)
        self.text.pack(side = tk.LEFT, fill=tk.X, expand=True)
        self.text.bind("<Return>", lambda event: (self.event_send()))

        self.btn = tk.Button(self.frame_1, text='Send', command=self.event_send)
        self.btn.pack(side = tk.RIGHT, padx=2)

        # 結果表示
        self.frame_2 = tk.Frame(self.root)
        self.frame_2.pack(fill=tk.BOTH, expand=True)

        self.mainText = ScrolledText(self.frame_2, state="disabled")
        self.mainText.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)

        self.t1 = threading.Thread(target=self.receiveSerial)
        self.t1.start()

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()
                os._exit(0)
        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        self.root.mainloop()

    def event_send(self, event=None):
        text = self.text.get()
        if text != '':
            self.mainText.configure(state='normal')
            self.mainText.insert(1.0, 'send content: ' + text + '\n')
            # 実際に送るところ
            # このタイミングで符号化をはさむ必要あり
            # 現状そのまま
            # port1.write((text + '\r\n').encode())

            self.mainText.configure(state='disabled')

    def event_receive(self, input):
        self.mainText.insert(1.0, input)

    def receiveSerial(self):
        while True:
            # input = port1.readline()
            self.event_receive(input.decode())

SimpleTerminal()