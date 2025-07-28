from scrapy import cmdline

# 注意，cmdline.execute()是为了减少输入命令的操作，该方法的参数必须为列表。
# 执行爬虫文件来启动项目
if __name__ == '__main__':
    cmdline.execute('scrapy crawl quotes'.split())
