from src.qr_generator import QRCodeGenerator
from src.color_print import ColorPrint
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        ColorPrint.print_error('Debes especificar una URL para generar el código QR.')
    else:
        url = sys.argv[1]
        if len(sys.argv) < 3:
            file_name = 'qrcode.png'
            qrcode_gen = QRCodeGenerator(url, file_name)
            ColorPrint.print_info('Código QR generado con el nombre qrcode.png')
        else:
            file_name = sys.argv[2]
            qrcode_gen = QRCodeGenerator(url, file_name)
            ColorPrint.print_info(f'Código QR generado con el nombre {file_name}')            
        qrcode_gen.create()