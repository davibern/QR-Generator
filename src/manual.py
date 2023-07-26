from src.color_print import ColorPrint


text_manual = """Welcome to the QR Generator Manual.

That's the option the software has:

--help or --h: show the help menu

Params QR:

url: QR Generator needs the url to generate QR
[name]: If you want to generate the file with a name write in second position the name

Example:
python main.py https://google.es google.png"""


class Manual:  
    
    @staticmethod
    def print_manual():
        ColorPrint.print_standard(text_manual)