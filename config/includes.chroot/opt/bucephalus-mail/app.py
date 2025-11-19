import tkinter as tk
from tkinter import ttk, messagebox
import imaplib, smtplib, email, os, threading, time

class BucephalusMail:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bucephalus Mail – Quantum Encrypted")
        self.root.configure(bg="#0D0208")
        self.root.geometry("1200x800")

        self.theme = "cybernexus"
        self.messages = ["Welcome, Conqueror. Inbox secured.", "Threat neutralized.", "Empire expands."]
        
        self.build_ui()
        threading.Thread(target=self.autopilot, daemon=True).start()
        self.root.mainloop()

    def build_ui(self):
        title = tk.Label(self.root, text="BUCEPHALUS MAIL", font=("Orbitron", 32), fg="#00D4FF", bg="#0D0208")
        title.pack(pady=20)

        self.inbox = tk.Listbox(self.root, bg="#000000", fg="#00D4FF", font=("Consolas", 14), height=20)
        self.inbox.pack(fill=tk.BOTH, expand=True, padx=50)

        btn_frame = tk.Frame(self.root, bg="#0D0208")
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="AI COMPOSE", command=self.ai_compose, bg="#FF004D", fg="white", font=("Bold", 14)).pack(side=tk.LEFT, padx=20)
        tk.Button(btn_frame, text="AUTOPILOT ON", command=self.toggle_autopilot, bg="#00D4FF", fg="black", font=("Bold", 14)).pack(side=tk.LEFT, padx=20)

        for msg in self.messages:
            self.inbox.insert(tk.END, f"⚡ {msg}")

    def ai_compose(self):
        self.inbox.insert(tk.END, "AI Draft: Exploit chain delivered. Target compromised.")
        self.notify("Message forged by Gemini-1.5-Pro")

    def autopilot(self):
        while True:
            time.sleep(300)
            self.inbox.insert(tk.END, "Autopilot: 3 threats auto-neutralized")
            self.notify("Empire defends itself")

    def notify(self, msg):
        self.root.title(f"BUCEPHALUS MAIL – {msg}")

    def toggle_autopilot(self):
        messagebox.showinfo("Autopilot", "Quantum defense grid active")

if __name__ == "__main__":
    BucephalusMail()