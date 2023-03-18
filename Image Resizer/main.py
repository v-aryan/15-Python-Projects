# install pillow if you havent  - done
# import pillow - done
# open up the image that we want to resize
# print the current size of image
# specify the size we wanna change it to
# save the new resized image

from PIL import Image


def resize_image(size1,size2):
    image = Image.open('mine.jpg')
    print(f"current size: {image.size}")

    resized_image = image.resize((size1, size2))
    resized_image.save('newimage1.jpg')


size1 = int(input("Enter the new width of image: "))
size2 = int(input("Enter the new length of image: "))
resize_image(size1,size2)
