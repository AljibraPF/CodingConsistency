#A Side project from somone who i consider very special to my heart
#They've asked me to make them a GUI that is able to detect sounds and give the name of the sounds in an output!

import tkinter as tk
from tkinter import filedialog, messagebox

# Logika UI

# Function placeholder untuk mendeteksi suara
# Logika cara mendeteksi ini akan mencari jika file cocok dengan namanya
# Cuma namanya yang bisa ditangkap, implementasikanmi logika ta di function untuk menangkap suara

def deteksi_pui_pui(audio_path): 
    if "Pui-pui" in audio_path:
        return "Pui-pui Terdeteksi"
    return "Suara tidak terdeteksi"

def deteksi_gendang(audio_path):
    if "Gendang" in audio_path:
        return "Gendang Terdeteksi"
    return "Suara tidak terdeteksi"

def deteksi_kacaping(audio_path):
    if "Kacaping" in audio_path:
        return "Kacaping Terdeteksi"
    return "Suara tidak terdeteksi"

def deteksi_suling(audio_path):
    if "Suling" in audio_path:
        return "Suling Terdeteksi"
    return "Suara tidak terdeteksi"

def deteksi_papparappasa(audio_path):
    if "Papparappasa" in audio_path:
        return "Papparappasa Terdeteksi"
    return "Suara tidak terdeteksi"

def deteksi_rebana(audio_path):
    if "Rebana" in audio_path:
        return "Rebana Terdeteksi"
    return "Suara tidak terdeteksi"

def deteksi_kesok_kesok(audio_path):
    if "Kesok-Kesok" in audio_path:
        return "Kesok-Kesok Terdeteksi"
    return "Suara tidak terdeteksi"

def deteksi_mandaliong(audio_path):
    if "Mandaliong" in audio_path:
        return "Mandaliong Terdeteksi"
    return "Suara tidak terdeteksi"

def deteksi_gambus(audio_path):
    if "Gambus" in audio_path:
        return "Gambus Terdeteksi"
    return "Suara tidak terdeteksi"

def deteksi_bassing_kajang(audio_path):
    if "Bassing Kajang" in audio_path:
        return "Bassing Kajang Terdeteksi"
    return "Suara tidak terdeteksi"

def deteksi_suara(audio_path):
    suara_fungsi = [
        deteksi_pui_pui,
        deteksi_gendang,
        deteksi_kacaping,
        deteksi_suling,
        deteksi_papparappasa,
        deteksi_rebana,
        deteksi_kesok_kesok,
        deteksi_mandaliong,
        deteksi_gambus,
        deteksi_bassing_kajang
    ]
    
    for fungsi in suara_fungsi:
        hasil = fungsi(audio_path)
        if hasil != "Suara tidak terdeteksi":
            return hasil  

    return "Suara tidak terdeteksi"

def upload_file():
    file_path = filedialog.askopenfilename(
        title="Pilih File Audio",
        filetypes=[("File Audio", "*.wav *.mp3 *.ogg *.flac")]
    )
    if file_path:
        try:
            suara_terdeteksi = deteksi_suara(file_path)
            output_label.config(text=suara_terdeteksi)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")


# Tampilan UI
root = tk.Tk()
root.title("Deteksi Suara")
root.geometry("600x400")

judul_label = tk.Label(root, text="Deteksi Suara", font=("Arial", 16))
judul_label.pack(pady=10)

upload_button = tk.Button(root, text="Upload File Audio", font=("Arial", 14), command=upload_file)
upload_button.pack(pady=20)

output_label = tk.Label(root, text="Suara yang terdeteksi muncul di sini", font=("Arial", 24), fg="blue", wraplength=500, justify="center")
output_label.pack(pady=40)

root.mainloop()
