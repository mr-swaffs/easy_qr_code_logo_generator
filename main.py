import pyqrcode
from PIL import Image, ImageOps
import numpy as np

def create_qrcode(url : str, logo_path : str, output_path : str, debug : bool = True):
    """
    This function creates the qr code of the url and then replaces the center code with a binary version
    of the image.
    Fun fact it actually replaces valid code. When I was playing around with box-sizes at a certain point
    the code becomes unreadable. So watch out and try the code with the phone!
    :param url: the url of the website to encode
    :param logo_path: the image you want to encode
    :param output_path:  the output path of the generated qr-code
    """
    url = pyqrcode.QRCode(url,error = 'H')
    url.png(output_path,scale=10)
    im = Image.open(output_path)
    im = im.convert("RGBA")
    logo = Image.open(logo_path)
    box = (150,150,300,300)
    im.crop(box)
    region = logo
    region = region.crop([500,500,2000,2000]).quantize(2)
    region = np.array(region)
    region[region < 1] = 255
    region[region <2] = 0
    region = Image.fromarray(region)
    region = ImageOps.grayscale(region)
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    region.show()
    im.paste(region,box)
    im.save(output_path)
    if debug:
        im.show()

if __name__ == '__main__':
    url = "www.the-url-you-want-to-encode"
    logo_path = "path-to-the-image"
    output_path = "output-path-of-the-qr-code"
    create_qrcode(url,logo_path, output_path)
