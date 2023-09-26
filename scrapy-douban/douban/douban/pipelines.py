# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

import scrapy
# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline

from douban.repo.mysql_localhost import DoubanTop250


class DoubanPipeline:
    def process_item(self, item, spider):
        return item


# try to download pic
class PictureDownloadPipeline(ImagesPipeline):
    def process_item(self, item, spider: scrapy.Spider):
        # 已经下载过了
        if item.get('img_downloaded'):
            return item
        # 下载文件
        spider.logger.info(f'{item["imdb_id"]} try to download picture')
        return super().process_item(item, spider)

    def item_completed(self, results, item: dict[str, object], info):
        super().item_completed(results, item, info)
        # 业务逻辑处理
        images: list[dict[str, str]] = item.get("images")
        if not images:
            return item
        # 填充 *_img_path
        for k, v in item.items():
            if not k.endswith("img"):
                continue
            for img in images:
                if img['url'] == v:
                    item[f'{k}_path'] = img['path']
        return item


class LogItemJSONString:
    def process_item(self, item, spider: scrapy.Spider):
        spider.logger.info(f'item downloaded -> {json.dumps(item, ensure_ascii=False)}')
        return item


class MySQLPersistence:
    def process_item(self, item, spider: scrapy.Spider):
        DoubanTop250(**item).save()
        pass
