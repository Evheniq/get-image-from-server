from global_errors_enums import GlobalErrorMessages
from get_image import GetImageFromServer
import config
import os


def test_get_image_from_server(delete_saved_image):
    GetImageFromServer(config.HOST, config.PORT, config.IMAGE_PATH)
    if not os.path.isfile(config.IMAGE_PATH):
        raise Exception(GlobalErrorMessages.IMAGE_NOT_SAVED.value)
