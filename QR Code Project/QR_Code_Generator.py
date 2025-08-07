import qrcode

# Ask user for input
data = input("Enter the URL or text to encode: ")
filename = input("Enter the filename to save the QR code (without extension): ")

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

# Create and save image
img = qr.make_image(fill='black', back_color='white')
img.save(f"{filename}.png")

print(f"QR code saved as {filename}.png")