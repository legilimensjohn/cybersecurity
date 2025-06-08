import socket
import datetime
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

HOST = '0.0.0.0'
PORT = 2222

class HoneyPotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Honeypot Monitor")
        self.text = ScrolledText(master, width=80, height=20)
        self.text.pack()
        self.running = False

        self.start_button = tk.Button(master, text="Start Honeypot", command=self.start_honeypot)
        self.start_button.pack()
        self.stop_button = tk.Button(master, text="Stop Honeypot", command=self.stop_honeypot, state=tk.DISABLED)
        self.stop_button.pack()

    def log(self, message):
        self.text.insert(tk.END, message + "\n")
        self.text.see(tk.END)

    def start_honeypot(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.thread = threading.Thread(target=self.run_honeypot, daemon=True)
        self.thread.start()

    def stop_honeypot(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def run_honeypot(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(5)
            self.log(f"Honeypot listening on {HOST}:{PORT}...")
            while self.running:
                s.settimeout(1.0)
                try:
                    conn, addr = s.accept()
                except socket.timeout:
                    continue
                with conn:
                    self.log(f"Connection from {addr}")
                    try:
                        data = conn.recv(1024).decode(errors='ignore')
                    except Exception:
                        data = "<error receiving data>"
                    self.log(f"Data: {data}")
                    with open("honeypot_log.txt", "a") as log:
                        log.write(f"{datetime.datetime.now()} - Connection from {addr[0]}:{addr[1]} - Data: {data}\n")
                    conn.sendall(b"SSH-2.0-OpenSSH_7.4\r\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = HoneyPotGUI(root)
    root.mainloop()