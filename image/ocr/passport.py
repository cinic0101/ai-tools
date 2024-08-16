from image.iamge_tool import ImageTool


class PassportRecognition(ImageTool):
    _lang_list = []

    def __init__(self, image_file_path: str, lang_list: [str]):
        super().__init__(image_file_path)
        self._lang_list = lang_list

    def _pre_process(self) -> dict:
        pass

    def _process(self, preprocessed_data: dict) -> dict:
        pass

    def _post_process(self, processed_data: dict) -> dict:
        pass
