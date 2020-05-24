#############################################
# 
#   sprite sheet to c64 sprite converter
#   (c)2020 by awsm of Mayday!
#
#   converts a bitmap with a spritesheet of (24*X)*(21*x) pixels
#   into a sprite data binary
#
#   notes:
#   I found the conversion to be quite tricky since I retrieve the pixel information
#   from the image itself 
#
#############################################



from PIL import Image
import math

def get_sprites(image_path,x,y):
    i = Image.open(image_path, 'r')
    i.pixels = list(i.getdata())
    i.x, i.y = i.size
    i.col = i.x / x
    i.row = i.y / y
    i.total = i.row * i.col
    i.sprite_width = x
    i.sprite_height = y

    print("spritesheet is: ",i.row, " rows by ", i.col, " cols.")
    return i


def show_sprite(sprites,number):
    sprite_block = sprites.sprite_width * sprites.sprite_height
    row = int(math.ceil(number / sprites.col)) -1 
    row_offset = row * (sprite_block * sprites.col) 
    col = number - row*sprites.col -1
    col_offset = col * sprites.sprite_width

    start = int(row_offset + col_offset)
    end = int(start + sprite_block)
    print("sprite: #",number)
    print("row is: ",row)
    print("row_offset is: ", row_offset)
    print("col is: ", col)
    print("col_offset is: ", col_offset)
    print("start is: ", start)
    print("end is: ", end)

    line = 0
    pixel_count = 0
    
    for i in range(start,end):
        pixel_count = pixel_count + 1
        
        pixel_pos = i + line 
        pixel = sprites.pixels[pixel_pos]

        if pixel == 0:
            print(".", end='')
        else:
            print("O", end='')

        if pixel_count == sprites.sprite_width:
            print()
            pixel_count = 0
            line = line + sprites.x -sprites.sprite_width
    print()
        

sprites = get_sprites("sprites-001.png", 24, 21)
#show_sprites(sprites)
show_sprite(sprites,15)




