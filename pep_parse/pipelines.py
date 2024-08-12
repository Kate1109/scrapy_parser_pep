# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import datetime as dt
from pathlib import Path
from collections import Counter


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = Counter()
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        filename = self.results_dir / 'status_summary_{time}.csv'.format(
            time=dt.datetime.now().strftime('%Y-%m-%dT%H-%M-%S'))
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(('Статус', 'Количество'))
            for key, val in self.results.items():
                writer.writerow([key, val])
            writer.writerow(['Total', sum(self.results.values())])
