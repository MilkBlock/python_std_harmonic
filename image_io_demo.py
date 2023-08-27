from PIL import Image
import io
import base64
dataurl = "xxxxx"
_format, _dataurl = dataurl.split(';base64,')
image_io = io.BytesIO()
image_io.write(base64.urlsafe_b64decode(_dataurl))
image =  Image.open(image_io)
image.save("this is a file.png")
# from PIL import Image
import io
import base64
# _format, _dataurl = dataurl.split(';base64,')
# image_io = io.BytesIO()
# image_io.write(base64.urlsafe_b64decode(_dataurl))
# image =  Image.open(image_io)
# image.save("this is a file.png")
import base64 

