import tkinter as tk
from tkinter import messagebox

def güncelle_giriş_alanları(*args):
    secim = operation.get()
    if secim == "kare":
        entry2.config(state='disabled')
        entry2.delete(0, tk.END)  # Kare seçilirse ikinci giriş temizlenir
    else:
        entry2.config(state='normal')

def ekle_sayi(sayi):
    # İşlem operatörlerinin numpad ile girilmesini engelle
    if sayi in ['+', '-', '*', '/']:
        messagebox.showinfo("Geçersiz Giriş", "İşlem operatörleri numpad ile girilemez. Lütfen yukarıdaki seçeneklerden birini seçin.")
        return

    if entry_focus.get() == "entry1":
        current = entry1.get()
        entry1.delete(0, tk.END)
        entry1.insert(tk.END, current + sayi)
    elif entry_focus.get() == "entry2":
        current = entry2.get()
        entry2.delete(0, tk.END)
        entry2.insert(tk.END, current + sayi)

def temizle():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

def hesapla():
    try:
        sayi1_text = entry1.get()
        if not sayi1_text:
            messagebox.showerror("Hata", "Lütfen ilk sayıyı girin!")
            return
        sayi1 = float(sayi1_text)

        secim = operation.get()

        if secim == "kare":
            sonuc = sayi1 ** 2
            result_label.config(text=f"Sonuç: {sonuc}")
            return

        sayi2_text = entry2.get()
        if not sayi2_text:
            messagebox.showerror("Hata", "Lütfen ikinci sayıyı girin!")
            return
        sayi2 = float(sayi2_text)

        if secim == "toplama":
            sonuc = sayi1 + sayi2
        elif secim == "cikarma":
            sonuc = sayi1 - sayi2
        elif secim == "carpma":
            sonuc = sayi1 * sayi2
        elif secim == "bölme":
            if sayi2 == 0:
                messagebox.showerror("Hata", "Bölen sıfır olamaz!")
                return
            sonuc = sayi1 / sayi2
        else:
            messagebox.showwarning("Seçim Hatası", "Lütfen geçerli bir işlem seçin!")
            return

        result_label.config(text=f"Sonuç: {sonuc}")

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin!")

# Ana pencere
window = tk.Tk()
window.title("Numpad ile Hesap Makinesi")
window.geometry("400x550")

# Giriş alanları için odak
entry_focus = tk.StringVar(value="entry1")  # hangi giriş aktif?

# Giriş alanları
entry1 = tk.Entry(window, font=("Arial", 14), justify='right')
entry2 = tk.Entry(window, font=("Arial", 14), justify='right')

# Giriş alanlarına tıklanınca odak ayarı
def set_focus1(event):
    entry_focus.set("entry1")

def set_focus2(event):
    entry_focus.set("entry2")

entry1.bind("<FocusIn>", set_focus1)
entry2.bind("<FocusIn>", set_focus2)

label1 = tk.Label(window, text="Sayı 1:")
label2 = tk.Label(window, text="Sayı 2:")

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()

# İşlem Seçimi
operation = tk.StringVar(window)
operation.set("toplama")  # varsayılan değer
operation.trace_add("write", güncelle_giriş_alanları)

operations_frame = tk.Frame(window)
operations_frame.pack(pady=5)

tk.Radiobutton(operations_frame, text="Toplama", variable=operation, value="toplama").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(operations_frame, text="Çıkarma", variable=operation, value="cikarma").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(operations_frame, text="Çarpma", variable=operation, value="carpma").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(operations_frame, text="Bölme", variable=operation, value="bölme").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(operations_frame, text="Kare Alma", variable=operation, value="kare").pack(side=tk.LEFT, padx=5)

# Numpad Frame
numpad_frame = tk.Frame(window)
numpad_frame.pack(pady=10)

buttons = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['0', '.', 'C'],
    ['+', '-', '*', '/'],
    ['=']
]

for row in buttons:
    grid_row = tk.Frame(numpad_frame)
    grid_row.pack(side=tk.TOP)
    for btn in row:
        if btn == '=':
            tk.Button(grid_row, text=btn, width=23, height=2,
                      command=hesapla).pack(padx=2, pady=2, fill=tk.X)
        elif btn == 'C':
            tk.Button(grid_row, text=btn, width=5, height=2,
                      command=temizle).pack(side=tk.LEFT, padx=2, pady=2)
        else:
            tk.Button(grid_row, text=btn, width=5, height=2,
                      command=lambda b=btn: ekle_sayi(b)).pack(side=tk.LEFT, padx=2, pady=2)

# Sonuç Etiketi
result_label = tk.Label(window, text="Sonuç: ", font=("Arial", 14))
result_label.pack(pady=10)

# İlk durumda kontrol et
window.after(100, güncelle_giriş_alanları)

# Pencereyi çalıştır
window.mainloop()