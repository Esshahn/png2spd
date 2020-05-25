#############################################
# 
#   sprite sheet to c64 sprite converter
#   (c)2020 by awsm of Mayday!
#
#   converts a bitmap with a spritesheet of (24*X)*(21*x) pixels
#   into a sprite data binary
#
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



def spritesheet_to_spd(filename, image):
    all_sprites = []

    for i in range(1,image.total+1):
        sprite_data = convert_sprite(image,i)
        sprite_bytes = bits_to_bytes(sprite_data)
        all_sprites = all_sprites + sprite_bytes
    
    write_file(filename,all_sprites)


def write_file(filename, data):
    if not filename:
        filename = "test"

    newFile = open(filename+".spd", "wb")
    file_array = [11,8,6]
    file_array = file_array + data 
    newFileByteArray = bytearray(file_array)
    newFile.write(newFileByteArray)

#-----------------------------------------------------------------


image = get_sprites("sprites-001.png", 24, 21)
spritesheet_to_spd("hallo",image)

