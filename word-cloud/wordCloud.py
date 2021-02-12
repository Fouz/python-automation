import re
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


def _upload():
    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 ** 10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)


_upload()

content = "So much for the term term term term term term‘peer’ as having reference to an ennobled person.[2] But it is applicable, in fact, to all persons who are not ennobled, for they are the ‘peers’ of each other. We all know the old maxim that ‘every man has a right to be tried by his peers;’ in other words, his equals. This is, in fact, one of the most important features in Magna Charta: ‘No freeman shall be taken or imprisoned ... otherwise than by the lawful judgment of his peers, or by the law of the land.’ This of course applies as much to noblemen as to commoners, although its application to the former is, as we shall directly see, somewhat modified. If John Smith and Thomas Jones were to enter into a conspiracy to dethrone the sovereign, they would be guilty of treason, and would be tried by their peers—namely, a common jury; but if the Duke of A. and Viscount B., peers of parliament, conspired with a like intent, they also would be entitled to be tried by their peers—who, however, would be members of the House of Lords. Also, if Brown, Jones, or Robinson, either singly or in combination, committed burglary, arson, forgery, robbery, embezzlement, they, or he, would be guilty of felony, and would be tried by their peers. So also would the Duke of A. or the Earl of C., &c., as before. But if a peer of parliament were to obtain money under false pretences, or commit perjury, he would not be entitled to be tried in these cases by his peers, but would be tried by those who are his peers only as members of the community. For although the last-named offences are undoubtedly serious, the law regards them as "


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    frequencies = {}
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "so", "for", "in",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    s = re.sub(r'[^\w\s]', '', " ".join(file_contents.strip().split()))
    s = re.sub(r'_', '', s)
    s = re.sub("(?m)^\s+", "", s)

    for i in s.split(" "):
        if i.lower() in uninteresting_words or i == "":
            continue
        elif i.lower() not in frequencies:
            frequencies[i.lower()] = 0
        frequencies[i.lower()] += 1

    # LEARNER CODE START HERE

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
