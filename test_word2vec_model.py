import gensim
from gensim.models import Word2Vec

model = gensim.models.Word2Vec.load('/home/wlane/PycharmProjects/word2vec/Resources/Training_Output/mimic_fh12k.word2vec.model')
print model.most_similar('ppd', topn=5)
print model.most_similar('pack-years', topn=5)
print model.most_similar('tob', topn=5)
print model.most_similar('etoh', topn=5)
print model.most_similar('biopsy', topn=5)
print model.most_similar('dx', topn=5)
print model.most_similar('status', topn=5)
print model.most_similar('pt', topn=5)
print model.most_similar('rn', topn=5)
print model.most_similar('nsclc', topn=5)
print model.most_similar('lung', topn=5)
print model.most_similar('breakfast', topn=5)
#One of these things is not like the other:
print model.doesnt_match("breakfast cereal dinner lunch".split())
# Similarity score between two terms:
print model.similarity('tylenol', 'ibuprofen')


