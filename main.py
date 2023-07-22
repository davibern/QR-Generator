from src.qr_generator import QRCodeGenerator
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('\x1b[1;31m' + 'Debes especificar una URL como argumento.' + '\x1b[0m')
    else:
        url = sys.argv[1]
        if len(sys.argv) < 3:
            file_name = 'qrcode.png'
            qrcode_gen = QRCodeGenerator(url, file_name)
        else:
            file_name = sys.argv[2]
            qrcode_gen = QRCodeGenerator(url, file_name)
            
        qrcode_gen.create()