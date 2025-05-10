# Puedes usar el siguiente código en Python para listar las combinaciones de teclas disponibles en tu teclado.
# Este script utiliza la biblioteca `keyboard` para detectar las teclas presionadas.

import keyboard

print("Presiona diferentes combinaciones de teclas para ver cómo se registran.")
print("Presiona 'Esc' para salir.")

def on_key_event(event):
    print(f"Tecla presionada: {event.name}")

keyboard.hook(on_key_event)

keyboard.wait('esc')