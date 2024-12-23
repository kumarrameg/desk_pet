from PIL import Image, ImageDraw
import time

# Define the palette (RGB values)
palette = [
    (245, 245, 245), (255, 195, 7), (119, 120, 120), (253, 191, 7),
    (131, 2, 18), (229, 57, 52), (19, 19, 19), (68, 68, 68),
    (236, 239, 241), (238, 241, 242), (255, 255, 255), (194, 194, 194),
    (243, 244, 244), (214, 216, 216), (135, 0, 19), (0, 0, 0),
    (228, 54, 49), (236, 238, 238), (205, 205, 205), (189, 189, 189),
    (248, 248, 248), (116, 117, 117), (162, 163, 163)
]

# Example frame data (replace with your actual frame data)
frames = [
      [
        [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 6, 15, 15, 15, 15],
        [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 6, 15, 15, 15],
        [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 7, 16, 14, 7, 15, 15],
        [15, 15, 15, 15, 15, 15, 15, 15, 15, 6, 22, 20, 10, 22, 6, 15],
        [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 7, 13, 13, 7, 15, 15],
        [15, 7, 7, 15, 15, 15, 15, 15, 15, 6, 17, 3, 3, 17, 6, 15],
        [6, 11, 20, 2, 21, 21, 15, 15, 15, 21, 9, 13, 13, 17, 6, 15],
        [15, 21, 17, 10, 10, 10, 2, 2, 2, 10, 10, 10, 10, 17, 21, 15],
        [6, 7, 7, 19, 17, 2, 2, 10, 10, 12, 22, 12, 10, 17, 18, 6],
        [6, 13, 22, 11, 13, 6, 2, 10, 10, 17, 6, 17, 10, 9, 13, 6],
        [15, 21, 10, 10, 12, 21, 21, 7, 7, 21, 22, 20, 0, 9, 13, 6],
        [15, 15, 7, 17, 13, 22, 7, 7, 21, 2, 9, 0, 9, 13, 7, 15],
        [15, 15, 15, 7, 7, 19, 19, 19, 19, 18, 18, 11, 7, 7, 15, 15],
        [15, 15, 15, 15, 15, 6, 6, 7, 6, 6, 6, 6, 15, 15, 15, 15],
        [15, 15, 15, 15, 15, 15, 6, 3, 15, 6, 3, 6, 15, 15, 15, 15],
        [15, 15, 15, 15, 15, 15, 6, 3, 3, 6, 3, 3, 6, 15, 15, 15],
    ],
    # Add more frames here...
]

def display_frames(frames, scale=10, delay=0.5):
    """Display the frames sequentially."""
    for frame in frames:
        height = len(frame)
        width = len(frame[0])

        # Create an image for the frame
        img = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(img)

        # Draw each pixel with the corresponding palette color
        for y, row in enumerate(frame):
            for x, pixel in enumerate(row):
                draw.point((x, y), fill=palette[pixel])

        # Resize for better visibility (optional)
        img = img.resize((width * scale, height * scale), Image.NEAREST)

        # Display the image
        img.show()
        time.sleep(delay)

# Call the function to display the frames
display_frames(frames)
