# 내가 그린 이미지 읽기
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('nice.png')
img = np.array(im.resize((28,28), Image.ANTIALIAS).convert('L'))
print(img, img.shape)

data = img.reshape([1,784])
data = data / 255.0
print(data)

plt.imshow(data.reshape(28,28), cmap = 'Greys')
plt.show()
#plt.imshow(img)
#plt.show()