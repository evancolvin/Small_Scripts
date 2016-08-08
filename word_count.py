# word_count.py
import docx


def word_count(doclist):
    '''Gives you the total word count for several files.

    It Takes a list of .docx files as inputs, and counts the words (by
    splitting along spaces) in each paragraph of each document and returns
     the total count.
    '''
    words = 0
    for document in doclist:
        for paragraph in range(len(doclist[document].paragraphs)):
            words += len(doclist[document].paragraphs[paragraph].text.split())
    return words
