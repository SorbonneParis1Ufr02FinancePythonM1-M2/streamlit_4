import os

from helpers_config import get_serialized_data


def get_config():
    file_name = r"input\config.toml"
    config_path = os.path.join(os.getcwd(), file_name)
    return get_serialized_data(config_path)


def get_data():
    pass


if __name__ == "__main__":
    config = get_config()
    print(config)
    print("End config test")
