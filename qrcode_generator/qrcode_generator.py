import qrcode
#name=input("Enter name of the QR CODE")
data="https://penchalavamsic.github.io/penchalavamsi/"
qr = qrcode.QRCode(version = 2,
                   box_size = 20,
                   border = 10)
qr.add_data(data)
qr.make(fit = True)
image = qr.make_image(fill_color = 'red',
                      back_color = 'white')
image.save('myportfolio.jpg')