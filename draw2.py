from tkinter import W, image_names
from PIL import ImageGrab, Image

image = Image.open('test.png', 'r')

size = image.size
width, height = size[0], size[1]
print(width, height)

pixels = list(image.getdata())
print(len(pixels))

def get_picture(width, height):
    output = []
    black, white = 0, 0
    for i in range(height):
         row = []
         for n in range(width):
             if pixels[i*width + n][0] > 85:
                 white += 1
                 row.append(" ")
             else:
                 black += 1
                 row.append("0")
         output.append(row)
    return(output, white, black)

    
def pixelate(picture, grouping):
    p_output= []
    for row in range(0, len(picture)-(len(picture)%grouping), grouping):
        p_row = []
        for character in range(0,len(picture)-(len(picture)%grouping)-grouping, grouping):
            l_grouping = ""
            for n in range(grouping):
                for z in range(grouping):
                    l_grouping += picture[(row+n)][character+z]
            if "0" in l_grouping:
                p_row.append("0")
            else: 
                p_row.append(" ")
        p_output.append(p_row)
    return(p_output)

def get_symbol(string):
    if string == "0 0 ":return("| ")
    if string == " 0 0":return(" |")
    if string == "0  0":return("\\\\")
    if string == " 00 ": return("//")
    if string == "00  ":return("--")
    if string == "  00":return("__")
    if string == "0 00":return("\\\\")
    if string == " 000":return("//")
    if string == "00 0":return("\\")
    if string == "000 ":return("//")
    if string.count("0") == 1:return("  ")
    if string.count("0") == 0:return("  ")
    if string.count("0") == 4:return("||")
    return("?")

def transform(picture):
    grouping = 2
    p_output= []
    for row in range(0, len(picture)-(len(picture)%grouping), grouping):
        p_row = []
        for character in range(0,len(picture)-(len(picture)%grouping)-grouping, grouping):
            l_grouping = ""
            for z in range(grouping):
                for n in range(grouping):
                    l_grouping += picture[(row+z)][character+n]
            p_row.append(get_symbol(l_grouping))
        p_output.append(p_row)
    return(p_output)

def main():
    product = open("output.txt","w")
    output, white, black = get_picture(width, height)
    output = pixelate(output, 2)
    output = transform(output)
    row = ""
    for row in output:
        _row = ""
        for character in row:
            _row += character
        #print(len(_row))
        product.write(_row+"\n")
    print(white, black)

main()