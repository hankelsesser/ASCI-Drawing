from PIL import ImageGrab

width, height = 400, 400
x, y, = 140, 110


def get_picture(width, height):
    image = ImageGrab.grab()
    black = 0
    white = 0
    picture = []
    output=[]
    for i in range(height):
        row = []
        for n in range(width):
            if image.getpixel((n+x, y+i))[0] > 200:
                white += 1
                row.append(" ")
            else:
                black += 1
                row.append("0")
        output.append(row)
    return(output, black, white)
    
def pixelate(picture, grouping):
    p_output= []
    for row in range(0, len(picture), grouping):
        p_row = []
        for character in range(0,len(picture[row])-grouping, grouping):
            l_grouping = ""
            for n in range(grouping):
                for z in range(grouping):
                    l_grouping += picture[(row+n)][character+z]
            if "0" in l_grouping:
                p_row.append("0 ")
            else: 
                p_row.append("  ")
        p_output.append(p_row)
    return(p_output)






product = open("ASCI/output.txt","w")

output, black, white = get_picture(width, height)
output = pixelate(output, 8)
# output = transform(output)
row = ""
for row in output:
    _row = ""
    for character in row:
        _row += character
    #print(len(_row))
    product.write(_row+"\n")
print(black, white)


