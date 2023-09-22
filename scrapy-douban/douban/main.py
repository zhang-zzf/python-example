# This is a sample Python script.
from scrapy import cmdline

from config import LogConfig
from douban.spiders.Top250 import Top250Spider

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # LogConfig().load_log_cfg()
    # 导入 cookies
    cookie_str = 'bid=8x55P5MHdm0; ll="108296"; ap_v=0,6.0; frodotk_db="650479fb328131112f0d6df197839333"; push_noty_num=0; push_doumail_num=0; dbcl2="274167245:xifZNZ8f6+Y"; ck=oc3q'
    Top250Spider.import_cookies(cookie_str)
    spider = 'Top250'
    cmd_setting = ''
    # cmd = f'scrapy crawl {spider} {cmd_setting}'
    cmd = f'scrapy crawl {spider} -s LOG_HTTP=True {cmd_setting}'
    cmdline.execute(cmd.split())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
