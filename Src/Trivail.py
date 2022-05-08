from pyserini.search.lucene import LuceneSearcher
from pyserini.index import IndexReader

#需要預先跑完Sh-file
searcher = LuceneSearcher('Index/Wiki_Chinese')
index_reader = IndexReader('Index/Wiki_Chinese')

def Retreiver(quesion):
  searcher.set_language('zh')
  hits = searcher.search(quesion)
  return json.loads(searcher.doc(hits[0].docid).raw())["contents"]

# QA  use the PLM 