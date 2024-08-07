from PIL import Image, ImageDraw
def ellipse(x, y, offset):
    image = Image.new("RGB", (500, 500), "lightblue")
    draw = ImageDraw.Draw(image)
    draw.ellipse((x, y, x+offset, y+offset), fill="blue")
    return image
def make_gif():
    frames = []
    x = 0
    y = 0
    offset = 100
    for number in range(20):
        frames.append(ellipse(x, y, offset))
        x += 55
        y += 55

    frame_one = frames[0]
    frame_one.save("circle.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)

if __name__ == "__main__":
    make_gif()
