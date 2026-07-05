import pyautogui
import time
import sys

# --- CONFIGURACIÓN DE COORDENADAS ---
# Modifica estos valores con las coordenadas de tu pantalla.
# Puedes usar el script auxiliar de abajo para encontrarlas.
X_CLICK_1 = 297
Y_CLICK_1 = 316

X_CLICK_2 = 550
Y_CLICK_2 = 380

# Número de veces que se repetirá el ciclo.
REPETICIONES = 10 
# ------------------------------------

print("====================================================")
print("   BOT DE AUTOMATIZACIÓN (Teclado y Mouse)")
print("====================================================")
print("El script comenzará en 5 segundos.")
print("¡Asegúrate de cambiar a la ventana correcta ahora!")
print("====================================================")

for i in range(5, 0, -1):
    print(f"Empezando en {i}...")
    time.sleep(1)

# Capturar la posición inicial del mouse
x_inicial, y_inicial = pyautogui.position()
print(f"\n[INFO] Posición inicial capturada: ({x_inicial}, {y_inicial})")

try:
    for i in range(REPETICIONES):
        print(f"\n[Ciclo {i+1}/{REPETICIONES}] Ejecutando secuencia...")
        
        # 1. Click en la primera posición
        print(f"  -> Haciendo click en ({X_CLICK_1}, {Y_CLICK_1})")
        pyautogui.click(X_CLICK_1, Y_CLICK_1)
        
        # 2. Esperar 2 segundos
        print("  -> Esperando 2 segundos...")
        time.sleep(2)
        
        # 3. Mover el mouse y hacer click en la segunda posición
        print(f"  -> Moviendo y haciendo click en ({X_CLICK_2}, {Y_CLICK_2})")
        pyautogui.click(X_CLICK_2, Y_CLICK_2)
        
        # 4. Presionar Enter
        print("  -> Presionando ENTER")
        pyautogui.press('enter')
        time.sleep(0.3) # Pausa breve para procesamiento del sistema
        
        # 5. Presionar Flecha Derecha
        print("  -> Presionando FLECHA DERECHA")
        pyautogui.press('right')
        time.sleep(0.3)
        
        # 6. Volver a la posición inicial
        print(f"  -> Volviendo a la posición inicial ({X_CLICK_1}, {Y_CLICK_1})")
        pyautogui.moveTo(X_CLICK_1, Y_CLICK_1, duration=0.5)
        
        # Pausa antes del siguiente ciclo
        time.sleep(0.5)

except pyautogui.FailSafeException:
    print("\n[¡PÁNICO!] Se activó el sistema de seguridad de PyAutoGUI.")
    print("Moviste el mouse a una esquina de la pantalla. Programa detenido.")
    sys.exit()

print("\n====================================================")
print("¡Automatización completada con éxito!")
print("====================================================")
