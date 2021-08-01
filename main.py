# -*- coding: utf-8 -*-
from shutil import copyfile
import eyed3
import os

from loguru import logger

path = '/Users/bmlee/Desktop/music/'
rename_dir_path = path + "rename/"

if __name__ == '__main__':
    if not os.path.exists(rename_dir_path):
        os.mkdir(rename_dir_path)
    file_list = os.listdir(path)
    for file_name in file_list:
        file_path = path + file_name
        try:
            if os.path.isfile(file_path):
                filename, fileExtension = os.path.splitext(file_path)
                file_meta = eyed3.load(file_path)
                if file_meta == None:
                    logger.error("!! >> file_path " + file_path)
                    continue
                rename_file_name = "{}-{}{}".format(file_meta.tag.title.strip(),
                                                    file_meta.tag.artist.strip(),
                                                    fileExtension)
                rename_file_path = rename_dir_path + rename_file_name.lower()
                if not os.path.exists(rename_file_path):
                    copyfile(file_path, rename_file_path)
                    logger.info("origin : {}, new : {}".format(file_name, rename_file_path))
        except Exception as e:
            logger.error(file_path)
