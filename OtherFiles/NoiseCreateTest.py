import noise
import numpy as np
from PIL import Image

sizex, sizey = 1024, 1024
shape = (sizex, sizey)
scale = 0.5
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = np.random.randint(0, 100)

world = np.zeros(shape)

# make coordinate grid on [0,1]^2
x_idx = np.linspace(0, 1, shape[0])
y_idx = np.linspace(0, 1, shape[1])
world_x, world_y = np.meshgrid(x_idx, y_idx)

# apply perlin noise, instead of np.vectorize, consider using itertools.starmap()
world = np.vectorize(noise.pnoise2)(
    world_x / scale,
    world_y / scale,
    octaves=octaves,
    persistence=persistence,
    lacunarity=lacunarity,
    repeatx=sizex,
    repeaty=sizey,
    base=seed,
)

# here was the error: one needs to normalize the image first. Could be done without copying the array, though
imgMap = np.floor((world + 0.5) * 255).astype(np.uint8)  # <- Normalize world first
img = Image.fromarray(imgMap, mode="L")
img.show()
img2Map = []
for x in range(sizex):
    xline = []
    for y in range(sizey):
        xline.append([img.getpixel((x, y))])
    img2Map.append(xline)
