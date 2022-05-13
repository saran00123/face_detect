# #finding image properties
# from PIL import Image
# image = Image.open('images/Screenshot from 2022-01-29 22-06-49.png')
# print(image.format)
# print(image.size)
# print(image.mode)
# image.show()


# #ploting a image
# from matplotlib import image
# from matplotlib import pyplot
# image = image.imread('images/Screenshot from 2022-01-29 22-06-49.png')
# print(image.dtype)
# print(image.shape)
# pyplot.imshow(image)
# pyplot.show()


# #numpy packages
# from PIL import Image
# from numpy import asarray
# image = Image.open('images/2.jpg')
# data = asarray(image)
# print(type(data))
# print(data.shape)
# image2 = Image.fromarray(data)
# print(type(image2))
# print(image2.mode)
# print(image2.size)
# print(data)


# #saving gray image
# import numpy as np
# from PIL import Image
# im = np.array(Image.open('images/2.jpg').convert('L'))
# print(type(im))
# gr_img = Image.fromarray(im).save('images/gr_2.jpg')


# #resiezing a image
# import numpy as np
# from PIL import Image
# load_img_rz = np.array(Image.open('images/2.jpg').resize((200,200)))
# Image.fromarray(load_img_rz).save('images/R_2.jpg')
# print("after resizing:",load_img_rz.shape)


# #trimming a image
# import numpy as np
# from PIL import Image
# im = np.array(Image.open('images/2.jpg'))
# print("Before Trimming", im.shape)
# im_trim = im[128:384, 128:384]
# print("After trimming",im_trim.shape)
# Image.fromarray(im_trim).save('images/trim_2.jpg')


#loading an image using keras API
from keras.preprocessing.image import load_img
import warnings

img = load_img('images/2.jpg')

print(type(img))
print(img.format)
print(img.mode)
print(img.size)

img.show()