from scrapy import cmdline

name="zhihu"
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())