import nltk
import re
import pickle
import sys
import pprint
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from math import floor, log10

keyword = ['wait', 'good', 'bad', 'horrible', 'excellent', 'rude', 'great', 'waited', 'cold', 'poor', 'manager', 'loud',
           'friendly',
           'negative', 'positive', 'apologize', 'best', 'worst', 'expensive', 'inexpensive', 'delicious', 'fun',
           'recommend', 'time',
           'waste', 'slow', 'fast', 'complain', 'waiter', 'cafeteria', 'respect', 'pissed', 'hour', 'minutes', 'sucks',
           'nice', 'try', 'highly',
           'wonderful', 'never', 'asked', 'Asked']
bi_keyword = ['service friendly', 'bad food', 'bad service', 'good service', 'excellent restaurant', 'bad restaurant',
              'was wonderful',
              'Beautiful place', 'was great', 'was good', 'after waiting', 'very poor', 'best food', 'worst food',
              'worst place',
              'very good', 'good quality', 'bad quality']

all_keyword = []


def evaluate(classifier, features_set, output , name):
    accuracy = nltk.classify.accuracy(classifier, features_set)
    print( "Accuracy for",name," = ",  accuracy )
    features_only = []
    reference_labels = []
    for feature_vectors, category in features_set:
        features_only.append(feature_vectors)
        reference_labels.append(category)

    predicted_labels = classifier.classify_many(features_only)
    confusion_matrix = nltk.ConfusionMatrix(reference_labels, predicted_labels)

    print("\nConfusion Matrix for",name,":\n")
    print(confusion_matrix)


def normalize(review):
    lowerText = review.lower()
    lowerText = nltk.word_tokenize(lowerText)

    stopWords = stopwords.words('english')
    stopWords.append("'s")
    stopWords.append("'t")
    stopWords.append("like")
    stopWords.append("things")
    stopWords.append("told")
    stopWords.append("tables")
    stopWords.append("seemed")
    stopWords.append("looked")
    stopWords.append("list")
    stopWords.append("given")
    stopWords.append("looked")
    stopWords.append("food")

    normalizedText = (" ").join(word for word in lowerText if word not in stopWords)

    pattern = r"(?<!\w)(\W+)(?!\w)"
    normalizedText = re.sub(pattern, " ", normalizedText)
    normalizedText = re.sub(r"( ){2,}", " ", normalizedText)[:-1]
    normalizedText = normalizedText.split(sep=' ')

    return normalizedText


def feature_extractor_com(all_reviews):
    result = []
    for review in all_reviews:
        flist = {}
        total_word = nltk.word_tokenize(review)
        pos = nltk.pos_tag(total_word)
        all_pos = [(tag[1]) for tag in pos]  # find all the tags in each review
        total_pos = len(pos)
        pos_count = nltk.FreqDist(all_pos).most_common()
        for value in pos_count:
            flist['UNIGRAM_POS_' + value[0]] = value[1] / total_pos
        total = len(total_word)
        word_count = nltk.FreqDist(total_word).most_common()
        for w in word_count:
            flist['UNIGRAM_' + w[0]] = w[1] / total
        pos_bigram = nltk.bigrams(pos)  # contains tuples
        all_pos_bigram = [(tuple[0][1] + '_' + tuple[1][1]) for tuple in
                          pos_bigram]  # extract firstPOS_secondPOS in bigrams
        total_pos = len(all_pos_bigram)
        all_bi_pos = nltk.FreqDist(all_pos_bigram).most_common()
        for value in all_bi_pos:
            flist['BIGRAM_POS_' + value[0]] = value[1] / total_pos
        bigram_num = len(total_word) - 1
        bigrams = nltk.bigrams(total_word)
        for word, count in nltk.FreqDist(bigrams).most_common():
            flist['BIGRAM_' + word[0] + '_' + word[1]] = count / bigram_num
        result.append(flist)
    return result


def generate_file_(feature_set, file_name):
    pos_line = ''
    neg_line = ''
    for data in feature_set:
        if data[1] == 'positive':
            pos_line += 'positive '
            for key in data[0]:
                pos_line += key + ':' + str(data[0][key]) + ' '
            pos_line += '\n'
        elif data[1] == 'negative':
            neg_line += 'negative '
            for key in data[0]:
                neg_line += key + ':' + str(data[0][key]) + ' '
            neg_line += '\n'

    re.sub(r'positive \w', '**', pos_line)
    # pos_line.replace(r'positive \n','')
    with open(file_name, 'w+', encoding='UTF-8') as file:
        file.write(pos_line)
        file.write(neg_line)

def rnd(x):
    return round(x, (floor(-log10(x)) + 1))

def feature_extractor(all_reviews):
    result = []
    for review in all_reviews:
        flist = {}
        total_word = normalize(review)
        total_word = [w for w in total_word if len(w) > 0]
        pos = nltk.pos_tag(total_word)
        all_pos = [(tag[1]) for tag in pos]  # find all the tags in each review
        total_pos = len(pos)
        total = len(total_word)
        word_count = nltk.FreqDist(total_word).most_common()  #
        pos_count = nltk.FreqDist(all_pos).most_common()  #
        bigram_num = len(total_word) - 1
        bigrams = nltk.bigrams(total_word)
        tigram = nltk.ngrams(total_word, 3)
        all_bi = nltk.FreqDist(bigrams).most_common()

        for value in pos_count:
            flist['UNIGRAM_POS_' + value[0]] = rnd(value[1] / total_pos)

        for w in total_word:
            if (total_word.count(w) > 0):
                flist['OCCURRENCE_' + w] = 1
            else:
                flist['OCCURRENCE_' + w] = 0

        for w in all_keyword:
            if (total_word.count(w) > 0):
                flist['OCCURRENCE_KEY' + w] = 1
            else:
                flist['OCCURRENCE_KEY' + w] = 0

        for w in word_count:
            flist['UNIGRAM_' + w[0]] = rnd(w[1] / total)

        for ti in tigram:
            flist['COUNT_TI_' + ti[0] + '_' + ti[1] + '_' + ti[2]] = 1

        for bi in all_bi:
            if re.match(r'([mM]inute[s]?)', bi[0][1]) and re.match(r'\b\d{1,2}\b', bi[0][0]):
                flist['TIME'] = 1

        for word, count in nltk.FreqDist(bigrams).most_common():
            flist['BIGRAM_' + word[0] + '_' + word[1]] = rnd(count / bigram_num)

        result.append(flist)

    return result


def get_score(review):
    return int(re.search(r'Overall = ([1-5])', review).group(1))

def get_text(review):
    return re.search(r'Text = "(.*)"', review).group(1)

def process_reviews(file_name):
    file = open(file_name, "rb")
    raw_data = file.read().decode("latin1")
    file.close()

    positive_texts = []
    negative_texts = []
    document = []
    first_sent = None
    for review in re.split(r'\.\n', raw_data):
        overall_score = get_score(review)
        review_text = get_text(review)
        if overall_score > 3:
            positive_texts.append(review_text)
        elif overall_score < 3:
            negative_texts.append(review_text)
        if first_sent == None:
            sent = nltk.sent_tokenize(review_text)
            if (len(sent) > 0):
                first_sent = sent[0]
    document.append(positive_texts)
    document.append(negative_texts)
    return document


if __name__ == '__main__':
    if  len(sys.argv) == 4:
        classifier = sys.argv[1]
        input_file = sys.argv[2]
        output = sys.argv[3]
    else:
        print("Please enter 3 arguments t start")
        exit()


    with open(classifier,'rb') as file:
        classifier = pickle.load(file)


    name = re.findall(r'\\(.*)',input_file)[0]
    reviews = process_reviews( input_file )



    pos_reviews = reviews[0]
    neg_reviews = reviews[1]

    feature_set = ([(feature, 'positive') for feature in feature_extractor(pos_reviews)] +
                   [(feature, 'negative') for feature in feature_extractor(neg_reviews)])


    evaluate( classifier , feature_set , output , name)
