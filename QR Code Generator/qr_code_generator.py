# Converting Text to QR Code

#Install Necessary Libraries
#Create Function that Collect the Text and Convert it to QR Code
#Save QR Code as Image
#Run the Function

#pip install qrcode Image //Windows 11
import qrcode
from matplotlib import pyplot as plt
import cv2

def generate_qrcode(text):

  qr =  qrcode.QRCode(
      version = 1,
      error_correction = qrcode.constants.ERROR_CORRECT_L,
      box_size = 10,
      border = 4,
  )

  qr.add_data(text)
  qr.make(fit = True)
  IMG = qr.make_image(fill_color = "black", back_color = "white")
  #QR_CODE = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
  
  plt.subplot(121)
  plt.imshow(IMG)
  plt.xticks([]),plt.yticks([])

  plt.subplot(122)
  plt.imshow(IMG,cmap = 'gray')
  plt.xticks([]),plt.yticks([])

  plt.show()
  IMG.save("QR.png")

text = input("Enter The Text To Be Converted To QR Code : ")
generate_qrcode(text)
