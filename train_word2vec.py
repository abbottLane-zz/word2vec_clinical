#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os.path
import re
import sys
import multiprocessing
from os import sysconf

import gensim
from gensim.models import Word2Vec

def main():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments

    input = "/home/wlane/PycharmProjects/word2vec/Resources/Training_Input"
    output = "/home/wlane/PycharmProjects/word2vec/Resources/Training_Output/mimic_fh12k.word2vec.400.sg.u.model.bin"

    sentences = MySentences(input)  # a memory-friendly iterator
    model = Word2Vec(sentences, size=400, window=5, min_count=5, sg=1, workers=multiprocessing.cpu_count())

    # trim unneeded model memory = use (much) less RAM (WARNING: Resultant model can not be updated!)
    #model.init_sims(replace=True)

    # save binary model format
    model.save(output)

    #save txt readable model format
    #model.save_word2vec_format(output, binary=False)


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                sent = line.split()
                sent = [x.lower() for x in sent]
                sent = [re.sub(r'[(){}<>,.?/:;]', '', x) for x in sent]
                yield sent


if __name__ == '__main__':
    main()