# Thin in a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image, ImageDraw,ImageFont
import requests
import io

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def runingNumber():
    a3_width = 420
    a3_hight = 594
    font_color = (255, 255, 255)
    url = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Black.ttf?raw=true'
    result = requests.get(url, allow_redirects=True)
    font = ImageFont.truetype(io.BytesIO(result.content), size=108)

    for i in custom_range_list(1, 138):
        color_code = (0, 0, 0)
        if i in custom_range_list(1, 17):
            color_code = (255, 144, 39)
        elif i in custom_range_list(17, 24) or i in custom_range_list(38, 45):
            color_code = (254, 177, 164)
        elif i in custom_range_list(25, 38):
            color_code = (109, 101, 86)
        elif i in custom_range_list(46, 52) or i in custom_range_list(66, 73):
            color_code = (141, 90, 57)
        elif i in custom_range_list(53, 66):
            color_code = (36, 92, 176)
        elif i in custom_range_list(74, 80) or i in custom_range_list(94, 101):
            color_code = (99, 71, 161)
        elif i in custom_range_list(81, 94):
            color_code = (58, 62, 64)
        elif i in custom_range_list(102, 128):
            color_code = (30, 120, 194)
        elif i in custom_range_list(129, 138):
            color_code = (68, 185, 74)

        img = Image.new(mode="RGB", size=(a3_width, a3_hight), color=color_code)
        img_drawing = ImageDraw.Draw(img)
        img_drawing.text((420 / 2, 594 / 2), text=f'{i}', fill=font_color, anchor="mb", font=font, align="center")
        file_name = 'runningNumber_'f'{i}'
        img.save(file_name + '.png')

# Press the green button in the gutter to run the script.
def custom_range_list(start,end):
    return range(start,end+1)

if __name__ == '__main__':
    print_hi('PyCharm')
    runingNumber()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
