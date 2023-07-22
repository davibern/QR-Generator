import qrcode
import os


class QRCodeGenerator:
    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name
        self.qr_directory = os.path.join('pics', 'qr')
        
    def create(self):
        os.makedirs(self.qr_directory, exist_ok=True)
        qrcode_object = qrcode.make(self.url)
        image_path = os.path.join(self.qr_directory, self.file_name)
        qrcode_object.save(image_path)