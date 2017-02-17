#!/usr/bin/env python
import os
import sys
import Image



if __name__ == "__main__":
    if len(sys.argv) > 1:
        print('Stripping ' + sys.argv[1] + ' of exif data!')
        raw_name = sys.argv[1].split('.')[0]

        image_file = open(sys.argv[1])
        image = Image.open(image_file)

        data = list(image.getdata())
        image_wo_exif = Image.new(image.mode, image.size)
        image_wo_exif.putdata(data)

        image_wo_exif.save(raw_name.lower() + '-s.jpg')
        print('Done!')
        print('New file saved as ' + raw_name.lower() + '-s.jpg')
    exit(0)
