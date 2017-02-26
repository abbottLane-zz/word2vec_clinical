import gensim


def main():
    model_path = "/home/wlane/PycharmProjects/word2vec/Resources/Training_Output/mimic_fh12k.word2vec.model"
    new_docs_dir = ""
    new_sentences = get_sentences(new_docs_dir)

    model = gensim.models.Word2Vec.load('/tmp/mymodel')
    model.train(new_sentences)


def get_sentences(dir):
    """
    Given a directory where clinical docs live, return a list of tokenized sentences
    :param dir: Where a set of new documents live
    :return: a list of tokenized sentences
    """
    sents = list()
    return sents

if __name__ == "__main__":
    main()