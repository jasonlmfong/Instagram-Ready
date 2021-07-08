from PIL import Image

#resize the image to 1080
def resize_jpg(image):
    if image.width < image.height and image.width != 1080:
        ratio = image.height/image.width
        newimg = image.resize((1080,int(1080*(ratio))))
        return newimg
    if image.width > image.height and image.height != 1080:
        ratio = image.width/image.height
        newimg = image.resize((int(1080*(ratio)),1080))
        return newimg

#crop the image to 1080*1080
def crop_instagram(image):
    midx = image.width//2
    midy = image.height//2
    croparea = (midx-540,midy-540,midx+540,midy+540)
    cropped = image.crop(croparea)
    return cropped