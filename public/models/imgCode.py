# _*_ coding: utf-8 _*_
# 导入页面封装好的操作类
import time
import pytesseract
import cv2
# 导入time   sleep单位为秒  便于设置等待时间
from PIL import Image, ImageEnhance
import public.models.myunit

# 该Login类继承页面类Page_Object


def getCode():
    # 获取截图
    ran = Image.open("share/screeshots/screenshot/1.png")
    # 截取二维码
    box = (1043, 456, 1105, 480)
    ran.crop(box).save("share/screeshots/screenshot/2.png")
    img = cv2.imread("share\screeshots\screenshot/2.png", -1)
    # 放大图像
    fx = 15
    fy = 15
    enlarge = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
    # 保存
    cv2.imwrite("share\screeshots\screenshot/2.png", enlarge, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    imageCode = Image.open("share\screeshots\screenshot/2.png")
    imgry = imageCode.convert('L')  # 图像增强，二值化
    pixels = imgry.load()
    for x in range(imgry.width):
        for y in range(imgry.height):
            if pixels[x, y] > 150:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0

    sharp_img = ImageEnhance.Contrast(imgry).enhance(2.0)  # 对比度增强
    sharp_img.save("share\screeshots\screenshot/3.png")
    time.sleep(2)
    # 图片转字符串
    code = pytesseract.image_to_string(Image.open("share\screeshots\screenshot/3.png")).strip()

    if code == '':
        return "no code"
    else:
        print(code)
        return code


if __name__ == '__main__':
    getCode()
