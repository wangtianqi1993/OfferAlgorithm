# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import os
import logging
import gensim

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MySentences(object):
    """
    使用生成器作为word2vec的输入
    """
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

sentences = MySentences("/home/wtq/develop/workspace/word_2_vec")

model = gensim.models.Word2Vec(sentences)
print model.similarity("papers", "waste")
print model.similarity("from", "This")

