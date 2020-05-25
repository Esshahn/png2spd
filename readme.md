# png2spd

## A PNG image to C64 sprite converter

The python script converts a PNG image file into a SpritePad compatible binary file. It can be used to convert sprites for the Commodore 64.

### Usage
`png_to_spd(input_file, output_file, sprite_width, sprite_height)`

`input_file`: name of the PNG image. Image must be (24*X)*(21*X) pixels
`output_file`: name of the sprite file (usually ends with .spd)
`sprite_width`: usually 24, which is the width of a hires C64 sprite
`sprite_height`: usually 21, which is the height of a hires C64 sprite

### Example
`spritesheet_to_spd("spritesheet.png","sprites.spd", 24, 21)`
loads a PNG file called `spritesheet.png` and exports it as `sprites.spd` in C64 SpritePad format.

Note: This script can easily be included into your make file, making it quite convenient to update sprites in an image editor (I use Asesprite) and save the bitmap file into the project folder of your C64 production. At compile time, the script takes the newest image file and converts it into a binary sprite file.


### Dependencies
Uses `Pillow` image manipulation library


### Version history
2020-05-25: initial release
