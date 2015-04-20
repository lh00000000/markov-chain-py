from collections import defaultdict
from itertools import chain
import random

class MarkovCharacter(object):

    def __init__(self, filepath):
        self.knowledge = defaultdict(list)
        self.train(filepath)

    def train(self, filepath):
        def text_to_knowledge(text):
            def tokenize_text(text):
                def tokenize_line(line):
                    line_tokens = [w.strip() for w in line.split() if w.strip() != '']
                    return line_tokens
                tokens = [tokenize_line(line) for line in text]
                return list(chain.from_iterable(tokens))

            def yield_trigrams():
                if len(tokens) < 3:
                    return
                for i in range(len(tokens) - 3):
                    yield (tokens[i], tokens[i + 1], tokens[i + 2])

            tokens = tokenize_text(text)
            text_knowledge = defaultdict(list)
            for w1, w2, w3 in yield_trigrams():
                text_knowledge[(w1, w2)].append(w3)
            return text_knowledge

        def append_new_knowledge(new_knowledge):
            for gram in new_knowledge.items():
                self.knowledge[gram[0]].append(gram[1][0])
            
        with open(filepath) as f:
            text = [line for line in f]
        append_new_knowledge(text_to_knowledge(text))

    def generate_phrase(self, min_chars=100, max_chars=140):
        random_bigram_key = random.choice(self.knowledge.keys())

        w1, w2 = random_bigram_key[0], random_bigram_key[1]
        phrase = '  '

        while phrase[-2] not in '.!?' and len(phrase) < max_chars:
            phrase += (w1 + ' ')
            w1, w2 = w2, random.choice(self.knowledge[(w1, w2)])

        if (len(phrase) < min_chars):
            return self.generate_phrase(min_chars, max_chars)
        else:
            return phrase.strip()

def main():
    mk = MarkovCharacter("tswift-corpus.txt")
    mk.train("birds-rights-activist-corpus.txt")

    print mk.generate_phrase()


if __name__ == '__main__':
    main()
