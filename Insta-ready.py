from PIL import Image, ImageEnhance

def resize_jpg(image):
    if image.width < image.height and image.width != 1080:
        ratio = image.height/image.width
        newimg = image.resize((1080,int(1080*(ratio))))
        return newimg
    if image.width > image.height and image.height != 1080:
        ratio = image.width/image.height
        newimg = image.resize((int(1080*(ratio)),1080))
        return newimg

def crop_instagram(image):
    midx = image.width//2
    midy = image.height//2
    croparea = (midx-540,midy-540,midx+540,midy+540)
    cropped = image.crop(croparea)
    return cropped

def filter_insta(image):
    contrast = ImageEnhance.Contrast(image).enhance(1.2)
    color = ImageEnhance.Color(contrast).enhance(1.3)
    bright = ImageEnhance.Brightness(color).enhance(1.1)
    sharp = ImageEnhance.Sharpness(bright).enhance(1.1)
    return sharp

if __name__ == "__main__":
    name = input("Which image would you like to deal with?")
    with Image.open(f"{name}{'.jpg'}") as inimg:
        newimg = resize_jpg(inimg)

        cropped = crop_instagram(newimg)

        filtered = filter_insta(cropped)

        outfile = f"{name}{'.png'}"
        im = filtered.save(outfile, "PNG")
        with Image.open(outfile) as im:
            im.show()

