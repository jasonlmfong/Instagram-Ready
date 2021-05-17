from PIL import Image, ImageEnhance, ImageFilter
from size_crop import resize_jpg, crop_instagram
from tint_warmth import convert_temp

def filter_insta(image):
    contrast = image.ImageEnhance.Contrast().enhance(1.15)
    color = ImageEnhance.Color(contrast).enhance(1.2)
    bright = ImageEnhance.Brightness(color).enhance(0.95)
    unsharp = bright.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    warm = convert_temp(unsharp, 5000)
    return warm

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

