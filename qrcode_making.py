import qrcode
image = qrcode.make("https://drive.google.com/drive/u/3/my-drive")
type(image)
image.save("code.png")

print("success")