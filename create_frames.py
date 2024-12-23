from PIL import Image
import numpy as np

# Define your palette (as RGB values matching the indices in your frame data)
palette = [
    (245, 245, 245), (255, 195, 7), (119, 120, 120), (253, 191, 7),
    (131, 2, 18), (229, 57, 52), (19, 19, 19), (68, 68, 68),
    (236, 239, 241), (238, 241, 242), (255, 255, 255), (194, 194, 194),
    (243, 244, 244), (214, 216, 216), (135, 0, 19), (0, 0, 0),
    (228, 54, 49), (236, 238, 238), (205, 205, 205), (189, 189, 189),
    (248, 248, 248), (116, 117, 117), (162, 163, 163)
]

def find_nearest_color(rgb):
    """Find the index of the closest color in the palette."""
    return min(range(len(palette)), key=lambda i: np.linalg.norm(np.array(rgb) - np.array(palette[i])))

def gif_to_frames_bit(file_path):
    """Extract frames from a GIF and convert them to 16x16 bitmap lists."""
    with Image.open(file_path) as img:
        frames_bit = []
        for frame in range(img.n_frames):
            img.seek(frame)
            frame_image = img.convert("RGB")  # Convert to RGB
            frame_image = frame_image.resize((16, 16))  # Resize to 16x16 pixels
            frame_array = []
            for y in range(frame_image.height):
                row = []
                for x in range(frame_image.width):
                    pixel = frame_image.getpixel((x, y))
                    index = find_nearest_color(pixel)
                    row.append(index)
                frame_array.append(row)
            frames_bit.append(frame_array)

    return frames_bit

def save_frames_to_file(frames_bit, output_file):
    """Save each frame as a separate variable in a Python file."""
    with open(output_file, "w") as f:
        f.write("# Frame data extracted from GIF\n\n")
        for i, frame in enumerate(frames_bit):
            f.write(f"frame{i} = {repr(frame)}\n\n")

# Example usage
file_path = "original_pet_gif/grain_picking.gif"
output_file = "frames.py"

frames_bit = gif_to_frames_bit(file_path)
save_frames_to_file(frames_bit, output_file)

print(f"Frame data saved to {output_file}")
