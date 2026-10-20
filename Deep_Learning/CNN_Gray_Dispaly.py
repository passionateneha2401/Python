from PIL import Image
import numpy as np

img = Image.open("digit.png")
img = img.convert("L")
img = img.resize((28,28))

pixels = np.array(img)

print("Image size : ",pixels.shape)

print("Pixel Values : ")
print(pixels)

# 0     Pure Black
# 255   Pure White
# 50    Dark Gray
# 120   Medium Gray
# 200   Light Gray