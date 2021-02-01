from PIL import Image

file_path = 'D:/AI/xxxx.png'#指定文件路径

img = Image.open(file_path)

imgSize = img.size

w = img.width  #图片的宽
h = img.height #图片的高
f = img.format #图像格式

print('图片的宽是：'   + str(w))
print('图片的高是：'   + str(h))
print('图片的格式是：' + str(f))
