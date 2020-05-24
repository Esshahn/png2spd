from PIL import Image
import math

def get_sprites(image_path,x,y):
    i = Image.open(image_path, 'r')
    i.pixels = list(i.getdata())
    i.x, i.y = i.size
    i.row = i.x / x
    i.col = i.y / y
    i.total = i.row * i.col
    i.sprite_width = x
    i.sprite_height = y
    return i

def show_sprites(sprites):
    count = 0
    for i in range(0,sprites.x*sprites.y):
        
        pixel = sprites.pixels[i]

        if count == sprites.x:
            print()
            count = 0

        if i % (sprites.x*sprites.sprite_height) == 0:
            print()

        if count % sprites.sprite_width == 0:
            print(" ", end='')

        if pixel == 0:
            print(".", end='')
        else:
            print("O", end='')

        count = count + 1



def show_sprite(sprites,number):
    
    row = int(math.ceil(number / sprites.row))-1 # which row is the sprite in
    row_offset = int(row * (sprites.sprite_width * sprites.sprite_height * sprites.row))
    col = int(number % sprites.row)-1
    col_offset = col * sprites.sprite_width
    
    start = row_offset + col_offset 
    end = start + sprites.sprite_height*sprites.sprite_width

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
show_sprite(sprites,11)




