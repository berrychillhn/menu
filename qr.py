import qrcode
from PIL import Image

# Enlace de tu menú (puede ser de OneDrive, Google Drive, etc.)
url = "https://andrs26.github.io/berrychill/"

# Crear código QR básico
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H  # Alto nivel de corrección para que funcione con logo
)
qr.add_data(url)
qr.make(fit=True)

# Crear imagen base
img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Abrir logo
logo = Image.open('logo.png')  # Usa tu logo aquí

# Calcular tamaño proporcional
qr_width, qr_height = img_qr.size
factor = 4  # El logo ocupará 1/4 del QR
logo_size = qr_width // factor

# Redimensionar logo
logo = logo.resize((logo_size, logo_size))

# Posicionar logo al centro
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
img_qr.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# Guardar imagen final
img_qr.save('menu_qr_con_logo.png')

print("¡QR con logo generado como 'menu_qr_con_logo.png'!")
