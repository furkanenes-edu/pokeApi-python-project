import customtkinter as ctk
from tkinter import messagebox
from api_handler import get_poke_info, get_poke_img

def pokemon_getir():
    pokemon_id = entry_id.get()
    if not pokemon_id:
        messagebox.showwarning("Hata", "Lütfen bir geçerli bir sayı giriniz.")
        return

    pokemon_info = get_poke_info(pokemon_id)

    if pokemon_info:
        name = pokemon_info['name'].capitalize()
        height = pokemon_info['height'] * 10/100
        weight = pokemon_info['weight'] * 10/100
        image_url = pokemon_info['sprites']['front_default']

        label_pokemon.configure(
            text=f"Pokemon: {name} \nBoy: {height} m \nKilo: {weight} kg"
        )

        if image_url:
            img = get_poke_img(image_url)
            if img:
                pokemon_image = ctk.CTkImage(light_image=img,dark_image=img, size=(200,200))
                label_img.configure(image=pokemon_image)
            else:
                label_img.configure(image=None)
        else:
            label_img.configure(image=None)
    else:
        label_pokemon.configure(text="Bu sayı ile bir Pokemon bulunamadı.")
        label_img.configure(image=None)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Pokemon Kitaplığı")
app.geometry("300x400")
app.resizable(False,False)
app.config(pady=25)

entry_id = ctk.CTkEntry(app, placeholder_text="Bir sayı giriniz")
entry_id.pack(pady=10)

button_ara = ctk.CTkButton(app, text="Pokemon Bul", command=pokemon_getir)
button_ara.pack()

label_img = ctk.CTkLabel(app,text="")
label_img.pack()

label_pokemon = ctk.CTkLabel(app, text="", justify="left")
label_pokemon.pack()

app.mainloop()