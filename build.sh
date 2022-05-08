# The cmd way to get trivail of data
!pip install pyserini
!pip install faiss-cpu

!python -m pyserini.index.lucene \
  --collection JsonCollection \
  --input corpus \
  --language zh \
  --index Index/Wiki_Chinese \
  --generator DefaultLuceneDocumentGenerator \
  --threads 1 \
  --storePositions --storeDocvectors --storeRaw



