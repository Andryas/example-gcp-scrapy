import json
from itemadapter import ItemAdapter
from src.utils.gcp import *
from src.utils.destymd import destymd
from src.settings import *

class JsonWriterPipeline:

    def __init__(self):
        pass

    def open_spider(self, spider):
        self.file = open(spider.name + ".jsonl", "w")

    def close_spider(self, spider):
        self.file.close()
        upload_blob(
            BUCKET, 
            spider.name + ".jsonl",
            destymd(spider.name, "jsonl")
        )

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item