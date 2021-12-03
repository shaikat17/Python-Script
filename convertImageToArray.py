from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
img = load_img("image.png")
# converting it to array
data = img_to_array(img)
print(data)
