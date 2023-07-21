import qrcode
import sys
import os

def main():
    try:
        # Obtain the url across the argument line program
        url = sys.argv[1]
        
        # Create QRCode object
        qrcode_object = qrcode.make(url)
        
        # Directory to save the qrcode image
        qr_directory = os.path.join(os.getcwd(), 'pics', 'qr')
        
        # Create directory if exists
        os.makedirs(qr_directory, exist_ok = True)
        
        # Check if user give a file name
        file_name = sys.argv[2] if sys.argv[2] is not None else 'qrcode.png'   
        
        # Save QRCode
        image_path = os.path.join(qr_directory, file_name)
        qrcode_object.save(image_path)
        
    except IndexError:
        sys.stderr.write('\x1b[1;31m' + 'No has especificado página web.' + '\x1b[0m')

if __name__ == '__main__':
    main()