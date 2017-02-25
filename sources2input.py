"""
MIMIC-II NoteEvents table -2- txt file containing all note events

Read in source documents from mimic.csv.gz NOTEEVENTS table, writes all clinical notes into a single file.
Assumes that column 10 in the csv.gz file is the "Notes" column. This is currently the case for the MIMIC-III
NOTEEVENTS.csv.gz table
"""
import csv
import logging
import os
import sys
import gzip
from os.path import isfile, join


program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))

def main():
    out_dir = "/home/wlane/PycharmProjects/word2vec/Resources/Training_Input/mimic_data.word2vec.in"
    in_dirs = ["/home/wlane/PycharmProjects/word2vec/Resources/Sources/mimic-III-data"]

    logger.info("Reading source data...")
    texts = get_texts_from_directories(in_dirs, out_dir)

    logger.info("Finished converting source data to word2vec input format. Your file lives in: "
                + "/home/wlane/PycharmProjects/word2vec/Resources/Training_Input")


def get_texts_from_directories(in_dirs, out_dir):
    all_texts = list()
    for dir in in_dirs:
        logger.info("\tfrom " + dir)
        onlyfiles = [f for f in os.listdir(dir) if isfile(join(dir, f))]
        all_texts.extend(get_texts_from_files(dir, onlyfiles, out_dir))
    return all_texts


def write_texts_to_out_dir(text, f):
    f.write(text)
    pass

def get_texts_from_files(dir, filenames, out_dir):
    texts=list()
    with open(out_dir, "wb") as outwriter:
        for file in filenames:
                texts.extend(read_mimic_data(dir, file, outwriter))
    return texts

def read_mimic_data(dir, filename, outwriter):
    docs = list()
    f = gzip.open(os.path.join(dir, filename), 'rb')
    reader = csv.reader(f, delimiter=",")
    doc_count = 0
    for row in reader:
        write_texts_to_out_dir(row[10], outwriter)
        doc_count +=1
    logger.info("Found %d documents", doc_count)
    return docs

if __name__ == '__main__':
    main()