from PIL import ImageGrab
#import Image

def isRunNian(year,month,day):
    if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
        return True
    else:
        return False

print isRunNian(2000,2,2)

bbox = (0, 0, 0+100, 0+100)
img = ImageGrab.grab(bbox)
img.save("pixel.png")
img.show()
