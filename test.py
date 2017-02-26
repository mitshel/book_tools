import os
from book_tools.format import create_bookfile

#file = "test_files/skazka.mobi"
#file = "test_files/Tolstoy_Aelita.132493.fb2"
file = "test_files/arduino.epub"
#file = "test_files/Volshebnye_skazki_Kitaja.fb2"
#file = "test_files/Vector.mobi"

path, name = os.path.split(file)
if isinstance(file, str):
    f = open(file, 'rb')
else:
    f = file

book = create_bookfile(f, name)

title = book.title
authors = book.authors
tags = book.tags
description = book.description
path=book.file.name
mimetype=book.mimetype
series_info=book.series_info
lang=book.language_code
issues=book.issues
original_filename=book.original_filename
docdate = book.docdate
cover = book.extract_cover("test_files/")


print("Title: %s"%title)
print("Authors: %s"%authors)
print("Tags: %s"%tags)
print("Description: %s"%description)
print("Path: %s"%path)
print("Mimetype: %s"%mimetype)
print("Series: %s"%series_info)
print("Lang: %s"%lang)
print("Issues: %s"%issues)
print("Docdate: %s"%docdate)
print("Original_filename: %s"%original_filename)

