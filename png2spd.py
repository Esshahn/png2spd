
# 
#   sprite sheet to c64 sprite converter
#   (c)2020 by awsm of Mayday!
#   http://www.awsm.de
#
#   converts a bitmap with a spritesheet
#   into a sprite data binary
#
#
#   usage:
#   spritesheet_to_spd(input_file,output_file, sprite_width, sprite_height)
#   input_file: name of the PNG image. Image must be (24*X)*(21*X) pixels
#   output_file: name of the sprite file (usually ends with .spd)
#   sprite_width: usually 24, which is the width of a hires C64 sprite
#   sprite_height: usually 21, which is the height of a hires C64 sprite
#
#   example:
#   spritesheet_to_spd("spritesheet.png","sprites.spd", 24, 21)
#   loads a PNG file called "spritesheet.png" and exports it
#   as "sprites.spd" in C64 SpritePad format
#



from PIL import Image
import math

def get_sprites(image_path,x,y):
    i = Image.open(image_path, 'r')
    i.pixels = list(i.getdata())
    i.x, i.y = i.size
    i.col = i.x / x
    i.row = i.y / y
    i.total = int(i.row * i.col)
    i.sprite_width = x
    i.sprite_height = y
    return i



def convert_sprite(sprites,number):
    sprite_length = sprites.sprite_width * sprites.sprite_height
    row = int(math.ceil(number / sprites.col)) -1 
    row_offset = row * (sprite_length * sprites.col) 
    col = number - row*sprites.col -1
    col_offset = col * sprites.sprite_width
    start = int(row_offset + col_offset)
    end = int(start + sprite_length)

    line = 0
    pixel_count = 0
    bit_array = []
    
    for i in range(start,end):
        pixel_count = pixel_count + 1
        
        pixel_pos = i + line 
        pixel = sprites.pixels[pixel_pos]

        if pixel == 0:
            print(" ", end='')
            bit_array.append(0)
        else:
            print("#", end='')
            bit_array.append(1)

        if pixel_count == sprites.sprite_width:
            print()
            pixel_count = 0
            line = line + sprites.x -sprites.sprite_width
    return bit_array


def bits_to_bytes(data):
    byte_counter = 0
    byte = ""
    bytes_array = []

    for pixel in data:
        byte = byte + str(pixel)

        if byte_counter == 7:
            byte_counter = 0
            hex_number = int(byte,2)
            bytes_array.append(hex_number)
            byte = ""
        else:
            byte_counter = byte_counter + 1
    bytes_array.append(1)
    return bytes_array



def write_file(filename, data):
    if not filename:
        filename = "test"

    newFile = open(filename, "wb")
    file_array = [11,8,6]
    file_array = file_array + data 
    newFileByteArray = bytearray(file_array)
    newFile.write(newFileByteArray)



def png_to_spd(input_filename, output_filename, sprite_width, sprite_height ):
    image = get_sprites(input_filename, sprite_width,sprite_height)

    all_sprites = []

    for i in range(1,image.total+1):
        sprite_data = convert_sprite(image,i)
        sprite_bytes = bits_to_bytes(sprite_data)
        all_sprites = all_sprites + sprite_bytes
    
    write_file(output_filename,all_sprites)




#-----------------------------------------------------------------



png_to_spd("test.png","test2.spd", 24, 21)

