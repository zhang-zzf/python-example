from language._000011_log import Test
from language.config import LogConfig

if __name__ == '__main__':
    LogConfig().load_log_cfg()
    Test().test_normal_case()
