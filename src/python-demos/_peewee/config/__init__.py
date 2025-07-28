import logging
import logging.config
import os
from os import makedirs
from os.path import dirname, exists

from yaml import load_all, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class LogConfig:

    def load_log_cfg(self, env_key="PROJ_ENV"):
        env = os.getenv(env_key, 'local')
        path = f"{dirname(os.path.abspath(__file__))}/log_cfg.yaml"
        config = None
        if exists(path):
            with open(path, "r") as f:
                config = self.__extract_env_config(load_all(f, Loader), env)
        if config:
            self.__mkdir_for_log_files(config)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(filename='app.log',
                                format='[%(asctime)s][%(levelname)-7s][%(name)s]-> %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S',
                                encoding='utf-8',
                                level=logging.DEBUG)

    def __mkdir_for_log_files(self, config: dict):
        # 如果路径不存在，创建日志文件文件夹
        handlers: dict = config.get('handlers')
        if not handlers:
            return
        h_c: dict
        for h_c in handlers.values():
            filename = h_c.get('filename')
            if filename:
                log_dir = dirname(filename)
                if not exists(log_dir):
                    makedirs(log_dir)

    def __extract_env_config(self, configs, env):
        for c in configs:
            if c['proj_env'] == env:
                return c
        return None
