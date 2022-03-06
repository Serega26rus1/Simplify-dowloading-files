import os
import requests
from PIL import Image
from io import BytesIO

def getphoto(token, bot, message, filename, *dir):
    file_info = bot.get_file(message.photo[-1].file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
    if len(dir) != 0:
        if dir[0] != '':
            if os.path.exists(dir[0]) != True:
                os.mkdir(dir[0])
            Image.open(BytesIO(file.content)).save(dir[0] + '/' + filename + '.jpg')
        else:
            Image.open(BytesIO(file.content)).save(filename + '.jpg')
    else:
        Image.open(BytesIO(file.content)).save(filename + '.jpg')


def getdocument(token, bot, message, filename, *dir):
    file_info = bot.get_file(message.document.file_id)
    file = bot.download_file(file_info.file_path)
    if len(dir) != 0:
        if dir[0] != '':
            if os.path.exists(dir[0]) != True:
                os.mkdir(dir[0])
            f = open(dir[0] + '/' + filename, 'wb')
            f.write(file)
            f.close()
        else:
            f = open(filename, 'wb')
            f.write(file)
            f.close()
    else:
        f = open(filename, 'wb')
        f.write(file)
        f.close()