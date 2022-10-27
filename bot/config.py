#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", default=18990697, cast=int)
    API_HASH = config("API_HASH", default="=f4815b9a16cb03c2f5eabe8db1cb0903")
    BOT_TOKEN = 5603895273:AAH_OWCXHDvEk4pIVZFqqDTIMnqJ37HP5O0
    DEV = 1479816157
    OWNER = 5261482689("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset veryfast -vcodec libx265 -crf 27 "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://te.legra.ph/file/f9f4413675c8ea31e7b1b.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
