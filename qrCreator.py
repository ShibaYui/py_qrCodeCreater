import qrcode

url="https://hackmd.io/@ult-yu1/ryxieqYyv"

qr_img=qrcode.make(url)
qr_img.save('qrcode.img')
