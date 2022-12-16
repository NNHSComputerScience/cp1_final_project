from PIL import Image 

def gray_scale(image):
	"""Sets the RGB components of every pixel in the picture to the average of all RGB values. Resulting image appears to be gray-scale."""
	pass

def posterize(image, color1, color2, color3, color4):
	"""Applies a Shepard Fairey effect to an image."""
	pass

# MAIN CODE

# RGB color tuples
#	Shepard Fairey color scheme: off white, light blue, red, dark blue
OFF_WHITE = ( 248, 229, 175 )
LIGHT_BLUE = ( 121, 149, 159 )
RED = ( 198, 50, 45 )
DARK_BLUE = ( 16, 48, 77 )

# EXTENSION - create your own custom color scheme to use
# 	color scheme 2: light orange, orange, dark orange, dark teal
LIGHT_ORANGE = ( 255, 212, 188 )
ORANGE = ( 255, 160, 87 )
DARK_ORANGE = ( 255, 86, 0)
DARK_TEAL = ( 0, 97, 65 )

# open the original image and convert to RGB format
orig_image = Image.open("huskie.jpg").convert("RGB")

# call the gray_scale function and pass to it the original image
gray_scale(orig_image)

# open the grayscale image and covnert to RGB format
gray_image = Image.open("gray_scale.png").convert("RGB")
    
# call the posterize function and pass to it the grayscale image and the 4 colors in the color palette.
posterize(gray_image, OFF_WHITE , LIGHT_BLUE, RED, DARK_BLUE )
