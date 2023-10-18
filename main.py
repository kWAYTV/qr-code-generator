import os, qrcode
from qrcode.constants import ERROR_CORRECT_L

class QRCodeGenerator:
    def __init__(self, box_size=10, border=1, version=1, error_correction=ERROR_CORRECT_L, fill_color="#000000"):
        self.box_size = box_size
        self.border = border
        self.version = version
        self.error_correction = error_correction
        self.fill_color = fill_color

    def generate_qr_code(self, text):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.fill_color, back_color="white")
        return img

    def save_qr_code(self, text, file_name):
        img = self.generate_qr_code(text)
        img.save(file_name)
        print(f"QR code saved as {file_name}")
        
        # Use it however you want, then delete the file with the following command for space saving:
        #self._delete_file(file_name)

    def _delete_file(self, file_name):
        try:
            os.remove(file_name)
            print(f"Deleted {file_name} successfully!")
        except OSError as e:
            print(f"Error deleting {file_name}: {e}")

if __name__ == '__main__':
    text = "https://kwayservices.top" # Change this to whatever you want to encode
    file_name = "qr-code.png" # Change this to whatever you want to name your file
    
    qr_generator = QRCodeGenerator()
    qr_generator.save_qr_code(text, file_name)