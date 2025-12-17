import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime

def get_target_time():
    # Hide the main window while asking for input
    root.withdraw()
    
    while True:
        # Prompt user for input
        user_input = simpledialog.askstring(
            "Set Timer", 
            "Enter target date/time:\n(Format: YYYY-MM-DD HH:MM:SS)",
            initialvalue=datetime.now().strftime("%Y-%m-%d 00:00:00")
        )
        
        # If user hits Cancel, exit the app
        if user_input is None:
            root.destroy()
            return None
            
        try:
            # Try to convert input to a date object
            target_date = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
            
            # Check if date is in the past
            if target_date < datetime.now():
                messagebox.showwarning("Error", "That date is in the past!")
                continue
                
            # If successful, show main window and return the date
            root.deiconify()
            return target_date
            
        except ValueError:
            messagebox.showerror("Error", "Invalid Format.\nPlease use: YYYY-MM-DD HH:MM:SS")

def update_timer():
    now = datetime.now()
    remaining = target_date - now

    if remaining.total_seconds() <= 0:
        label_time.config(text="00:00:00:00", fg="#ff4d4d") # Red
        label_msg.config(text="TIME'S UP!", fg="#ff4d4d")
        return

    # Calculate time parts
    days = remaining.days
    seconds = remaining.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Update display
    time_str = f"{days:02}d {hours:02}h {minutes:02}m {seconds:02}s"
    label_time.config(text=time_str)
    
    # Run again in 1 second
    root.after(1000, update_timer)

# --- MAIN SETUP ---
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("500x250")
root.configure(bg="#1e1e1e")

# Layout Configuration
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Labels
label_msg = tk.Label(root, text="Countdown to Target", font=("Helvetica", 16), bg="#1e1e1e", fg="#aaaaaa")
label_msg.pack(pady=(40, 10))

label_time = tk.Label(root, text="00:00:00:00", font=("Helvetica", 40, "bold"), bg="#1e1e1e", fg="#00ffcc")
label_time.pack(pady=10)

# Ask for date before starting the loop
target_date = get_target_time()

if target_date:
    update_timer()
    root.mainloop()
