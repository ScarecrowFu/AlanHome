import configparser
import os


def get_configure(config_file, section, option, default=''):
    # 获取配置文件中的配置
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
        return config.get(section, option)
    except:
        return default


def get_website_configure():
    from django.conf import settings
    serial_number = get_configure(settings.CONFIGURE_FILE, 'VERSION_INFO', 'serial_number', 'AlanHome')
    version = get_configure(settings.CONFIGURE_FILE, 'VERSION_INFO', 'version', 'V1')
    title = get_configure(settings.CONFIGURE_FILE, 'VERSION_INFO', 'title', '程序员赛道')
    keywords = get_configure(settings.CONFIGURE_FILE, 'VERSION_INFO', 'keywords', '扶妖-程序员赛道')
    description = get_configure(settings.CONFIGURE_FILE, 'VERSION_INFO', 'description', '扶妖，程序员赛道, 技术文章，博客，文章，程序，Python, JavaScript, 副业，自媒体，短视频，电商')
    remark = get_configure(settings.CONFIGURE_FILE, 'VERSION_INFO', 'remark', '程序员赛道，分享各类技术文章，项目，工具，创业方向，以及利用程序解决遇到的问题。')
    return {'serial_number': serial_number, 'version': version, 'title': title, 'keywords': keywords, 'description': description, 'remark': remark}

