import qrcode

img = qrcode.make("try this way")
img.save('qr_image.jpg')