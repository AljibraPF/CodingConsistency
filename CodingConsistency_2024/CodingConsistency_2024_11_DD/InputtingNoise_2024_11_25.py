#An improvement from the last code "CatchingIndonesianSound"
#Instead of inputting files, you can just record your audio directly
#Just need to download pyaudio

import tkinter as tk
import threading
import pyaudio
import wave
from tkinter import messagebox

# Logika UI

# Function placeholder untuk mendeteksi suara
# Bisa langsung input suara, suaranya akan di letakkan di file yang bernama "output.wav"
# Masih nama file yang bisa ditangkap, modifikasimi functionnya supaya cocok dengan alur Logika mendeteksi suarata

def deteksi_pui_pui(audio_path): #parameter audio_path adalah file yang bernama "output.wav"
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

is_listening = False
filename = "output.wav"  

def start_recording():
    global is_listening
    is_listening = True
    label_status.config(text="Lagi Mendengar...", fg="green")
    threading.Thread(target=record_audio).start()

def stop_recording():
    global is_listening
    is_listening = False
    label_status.config(text="Berhenti", fg="red")

def record_audio():
    global is_listening
    chunk = 1024  
    format = pyaudio.paInt16  
    channels = 1  
    rate = 44100  

    p = pyaudio.PyAudio()
    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    frames = []

    while is_listening:
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b"".join(frames))

    suara_terdeteksi = deteksi_suara(filename)
    output_label.config(text=suara_terdeteksi)

def play_audio():
    try:
        chunk = 1024  
        wf = wave.open(filename, "rb")
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(chunk)
        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        stream.stop_stream()
        stream.close()
        p.terminate()

    except FileNotFoundError:
        label_status.config(text="Tdk ada file untuk di putar", fg="orange")

# Tampilan UI
root = tk.Tk()
root.title("Deteksi Suara")
root.geometry("600x400")

judul_label = tk.Label(root, text="Deteksi Suara", font=("Arial", 16))
judul_label.pack(pady=10)

label_status = tk.Label(root, text="Stopped", fg="red", font=("Helvetica", 16))
label_status.pack(pady=20)

btn_start = tk.Button(root, text="Mulai", command=start_recording)
btn_start.pack(pady=10)

btn_stop = tk.Button(root, text="Berhenti", command=stop_recording)
btn_stop.pack(pady=10)

btn_play = tk.Button(root, text="Playback Suara", command=play_audio)
btn_play.pack(pady=10)

output_label = tk.Label(root, text="Suara yang terdeteksi muncul di sini", font=("Arial", 24), fg="blue", wraplength=500, justify="center")
output_label.pack(pady=40)

root.mainloop()
