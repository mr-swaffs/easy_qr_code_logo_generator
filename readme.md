# QR Code Generator with Logo

This is a small script to create qr codes with logos. <br/>
Currently, it is coded to only create grayscale images. <br/>
If you want to create rgb codes you will have to remove the 
gray scaling and binarization lines.

To run, 
adapt the url, logo and output paths. 
Also adapt the crop regions etc. since i hardcoded them.
Then just run the main.

### Example

![in.jpg : Photo by Richard Brutyo on Unsplash](example/in.jpg)
*Photo by Richard Brutyo on Unsplash https://unsplash.com/photos/Sg3XwuEpybU?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink*

```
url = "www.github.com"
logo_path = "example/in.png"
output_path = "example/out.png"
create_qrcode(url,logo_path, output_path)
```

#### Output

![](example/out.png)