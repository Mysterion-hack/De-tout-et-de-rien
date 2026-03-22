################################ Let's create a simple QR code using an image on the net ######################################################
# I have to add personnilisation features to the code 
import qrcode

image = qrcode.make("URL to image")
type(image)
image.save("imageName.png")

print("success")
