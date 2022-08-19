import pytest
import os
import config


def delete_image():
    if os.path.isfile(config.IMAGE_PATH):
        os.remove(config.IMAGE_PATH)
        print("Saved image has been deleted")
        return True
    else:
        print("Saved image does not exist")
        return False


@pytest.fixture
def delete_saved_image():
    delete_image()
    yield
    delete_image()


@pytest.fixture(autouse=True)
def run_server():
    import server
