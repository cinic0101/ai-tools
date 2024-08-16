from image.ocr.passport import PassportRecognition

if __name__ == '__main__':
    result = PassportRecognition(
        image_file_path="",
        lang_list=["en"]
    ).process()

    print(result)
