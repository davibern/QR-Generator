import qrcode
import sys
import os

def main():
    # Obtain the url across the argument line program
    url = sys.argv[1]
    
    # Create QRCode object
    qrcode_object = qrcode.make(url)
    
    # Directory to save the qrcode image
    qr_directory = os.path.join('pics', 'qr')
    
    # Create directory if exists
    os.makedirs(qr_directory, exist_ok = True)
    
    # Save QRCode
    image_path = os.path.join(qr_directory, 'qrcode.png')
    qrcode_object.save(image_path)
    

if __name__ == '__main__':
    main()