filename= input("Input the Filename: ")

file_extension= filename.split(".")[-1]

extension_mapping= {
    "py": "python",
    "java": "Java",
    "c": "C",
    "cpp": "C++",
    "js": "JavaScript",
    "html": "HTML",
    "css": "CSS",
    "txt": "Text",
    "json": "JSON",
    "xml": "Xml",
    "csv": "CSV",
    "jpg": "JPEG image",
    "png": "PNG image",
    "gif": "GIF image",
    "bmp": "Bitmap Image",
    "mp3": "MP3 Audio",
    "wav": "WAV Audio",
    "mp4": "MP4 Video",
    "avi": "AVI Video",
    "mkv": "MKV Video",
    "doc": "Word Document",
    "docx": "Word Document",
    "xls": "Excel Spreadsheet",
    "xlsx": "Excel Spreadsheet",
    "ppt": "PowerPoint Presentation",
    "pptx": "PowerPoint Presentation",
    "pdf": "PDF Document",
    "zip": "ZIP Archive",
    "rar": "RAR Archive"
}

file_type= extension_mapping.get(file_extension, "Unknown")

print(f"The extension of this file is: '{file_type}'")