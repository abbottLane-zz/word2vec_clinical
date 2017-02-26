import os
import re

import gensim


def main():
    model_path = "/home/wlane/PycharmProjects/word2vec/Resources/Training_Output/mimic_fh12k.word2vec.model"
    new_docs_dir = ""
    new_sentences = Sentence_Generator(new_docs_dir)

    model = gensim.models.Word2Vec.load('/tmp/mymodel')
    model.train(new_sentences)


class Sentence_Generator(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                # TODO: remove punctuation from words: 'ppd.' and 'ppd' should be the same thing
                sent = line.split()
                sent = [x.lower() for x in sent]
                sent = [re.sub(r'[(){}<>,.?/:;]', '', x) for x in sent]
                yield sent

if __name__ == "__main__":
    main()