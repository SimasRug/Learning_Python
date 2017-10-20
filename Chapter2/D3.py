gb = 10**9

gif_space = (800*600*1) / 5
jpeg_space = (800*600*3) / 25
png_space =  (800*600*3) / 8
tiff_space = (800*600*6) / 1

usb_drive_size = int(input('Enter USB size (GB) : \n'))

usb_size_bytes = usb_drive_size * gb

print(round(usb_size_bytes/gif_space), ' images in GIF format can be stored')
print(round(usb_size_bytes/jpeg_space), ' images in JPEG format can be stored')
print(round(usb_size_bytes/png_space), ' images in PNG format can be stored')
print(round(usb_size_bytes/tiff_space), ' images in TIFF format can be stored')
