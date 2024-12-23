import board
import busio
import displayio
from adafruit_st7735r import ST7735R
from time import sleep
from frames import *
import random

# Display setup
mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16

displayio.release_displays()

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

display = ST7735R(display_bus, width=128, height=160, bgr=True)

# Create a display group
splash = displayio.Group()
display.root_group = splash

# Chicken palette (map the unique colors)
chicken_palette = displayio.Palette(23)
colors = [
    (245, 245, 245), (255, 195, 7), (119, 120, 120), (253, 191, 7),
    (131, 2, 18), (229, 57, 52), (19, 19, 19), (68, 68, 68),
    (236, 239, 241), (238, 241, 242), (255, 255, 255), (194, 194, 194),
    (243, 244, 244), (214, 216, 216), (0, 0, 0), (0, 0, 0),
    (228, 54, 49), (236, 238, 238), (205, 205, 205), (189, 189, 189),
    (248, 248, 248), (116, 117, 117), (162, 163, 163)
]
for i, color in enumerate(colors):
    chicken_palette[i] = (color[0] << 16) + (color[1] << 8) + color[2]

# Chicken frames for idle and walking
chicken_idle_frames = [
    chicken_idel_frame0,
    chicken_idel_frame1,
    chicken_idel_frame0,
    chicken_idel_frame3,
]
chicken_walk_frames = [
    cwr_f_00, cwr_f_01, cwr_f_02, cwr_f_03,
    cwr_f_04, cwr_f_05, cwr_f_06, cwr_f_07,
]

# Create a Bitmap for the chicken
chicken_bitmap = displayio.Bitmap(16, 16, len(chicken_palette))
chicken_sprite = displayio.TileGrid(chicken_bitmap, pixel_shader=chicken_palette, x=0, y=70)
splash.append(chicken_sprite)

# Function to update the chicken frame
def update_chicken_frame(frame):
    for y, row in enumerate(frame):
        for x, pixel in enumerate(row):
            chicken_bitmap[x, y] = pixel

# Animation loop
frame_index = 0
state = "idle"  # Initial state
x_position = 0
screen_width = 128  # Width of the display

while True:
    # Update the frame based on the current state
    if state == "idle":
        update_chicken_frame(chicken_idle_frames[frame_index])
        frame_index = (frame_index + 1) % len(chicken_idle_frames)
    elif state == "walking":
        update_chicken_frame(chicken_walk_frames[frame_index])
        frame_index = (frame_index + 1) % len(chicken_walk_frames)
        x_position += 2  # Move to the right
        if x_position > screen_width:
            x_position = -16  # Wrap around to the left
        chicken_sprite.x = x_position

    # Randomly change the state
    if random.random() < 0.05:  # Adjust probability as needed
        state = "walking" if state == "idle" else "idle"
        frame_index = 0  # Reset the frame index when the state changes

    sleep(0.1)  # Adjust the delay for animation speed

