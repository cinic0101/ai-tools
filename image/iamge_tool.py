from abc import ABC, abstractmethod


class ImageTool(ABC):
    _image_file_path = ""

    def __init__(self, image_file_path: str):
        self._image_file_path = image_file_path

    @abstractmethod
    def _pre_process(self) -> dict:
        pass

    @abstractmethod
    def _process(self, preprocessed_data: dict) -> dict:
        pass

    @abstractmethod
    def _post_process(self, processed_data: dict) -> dict:
        pass

    def process(self) -> dict:
        preprocessed_data = self._pre_process()
        processed_data = self._process(preprocessed_data)
        return self._post_process(processed_data)