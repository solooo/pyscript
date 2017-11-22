from PIL import Image


ascii_char = list(r"█_")
# 把RGB转为灰度值，并且返回该灰度值对应的字符标记
def select_ascii_char(r, g, b):
    gray = int((19595 * r + 38469 * g + 7472 * b) >> 16)  # ‘RGB－灰度值’转换公式
    unit = 256.0/len(ascii_char)  # ascii_char中的一个字符所能表示的灰度值区间
    return ascii_char[int(gray/unit)]

img = Image.open("E:\\qrcode.jpg")
img = img.convert('L')
old_width, old_height = img.size
img = img.resize((int(old_width), int(old_height)), Image.NEAREST)
width, height = img.size
for i in range(height):
    txt = ""
    for j in range(width):
        value = img.getpixel((j, i))
        txt += "▇" if value < 125 else " "
        # txt += select_ascii_char(*img.getpixel((j, i))[0:3])
        # txt += str(img.getpixel((j, i))) + " "
    print(txt)




