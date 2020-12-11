from PIL import Image

# import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import os

os.system("")


def ccolor(r, g, b):
    return f"\x1B[38;2;{r};{g};{b}m"


ox = 5
noise1 = PerlinNoise(octaves=ox * 1)
noise2 = PerlinNoise(octaves=ox * 2)
noise3 = PerlinNoise(octaves=ox * 3)
noise4 = PerlinNoise(octaves=ox * 4)
noise5 = PerlinNoise(octaves=ox * 5)


xpix, ypix = 100, 100
pic = []

for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = ox ** (-0) * noise1([i / xpix, j / ypix])
        noise_val += ox ** (-1) * noise2([i / xpix, j / ypix])
        noise_val += ox ** (-2) * noise3([i / xpix, j / ypix])
        noise_val += ox ** (-3) * noise4([i / xpix, j / ypix])
        noise_val += ox ** (-4) * noise5([i / xpix, j / ypix])
        row.append(noise_val)
    pic.append(row)
    print(
        f"setting noise_val at {ccolor(255,12,34)}{i}{ccolor(0,255,255)}  {j}{ccolor(255,255,255)}"
    )
# asdfgbhgfadsfbhgweafsvdbhfgweafs
pic1 = sum(pic, [])
minnoise = min(pic1)
maxnoise = max(pic1)
newpic = []
for y in pic:
    row = []
    for x in y:
        NewValue = round((((x - minnoise) * (255 - 0)) / (maxnoise - minnoise)) + 0)
        row.append(NewValue)
    newpic.append(row)
# plt.subplot(2, 1, 1)
# plt.imshow(pic, cmap='gray')

# plt.subplot(2, 1, 2)
# plt.imshow(newpic, cmap='gray')


class surfc:
    def grc():
        import random

        return [
            random.randrange(0, 255),
            random.randrange(0, 255),
            random.randrange(0, 255),
        ]

    colormap = [
        {"mn": 0, "mx": 40, "clr": grc()},
        {"mn": 40, "mx": 90, "clr": grc()},
        {"mn": 90, "mx": 110, "clr": grc()},
        {"mn": 110, "mx": 150, "clr": grc()},
        {"mn": 150, "mx": 190, "clr": grc()},
        {"mn": 190, "mx": 210, "clr": grc()},
        {"mn": 210, "mx": 215, "clr": grc()},
        {"mn": 215, "mx": 255, "clr": grc()},
    ]

    def inRange(source, min_s, max_s):
        if source >= min_s and source <= max_s:
            return True
        return False

    def getSurface(grayclr):
        for check in surfc.colormap:
            if surfc.inRange(grayclr, check["mn"], check["mx"]):
                return check["clr"]
        return [0, 0, 0]


img = Image.new("RGB", (xpix, ypix))
for y in range(len(newpic)):
    for x in range(len(newpic[y])):
        print(
            f"{ccolor(255,12,34)}{x}{ccolor(0,255,255)}{y}{(ccolor(*surfc.getSurface(newpic[y][x])))};",
            end="",
        )
        img.putpixel((y - 1, x - 1), tuple(surfc.getSurface(newpic[y][x])))
    print()
img.show()
# plt.show()
