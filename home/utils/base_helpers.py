import configparser


def get_configure(config_file, section, option, default=''):
    # 获取配置文件中的配置
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
        return config.get(section, option)
    except:
        return default