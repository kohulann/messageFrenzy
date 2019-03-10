from random import choices
import random
class MessageFrenzy:
    sentence1 = "This boy is cool is awesome is amazing"

    def main(self):
        words = self.sentence_splitter(self)
        table = self.generate_table(self, words)
        initial_word = self.initial_word(self,table)
        sentence = self.build_sentence(self, initial_word, table)
        print(sentence)

    def sentence_splitter(self):
        words = self.sentence1.split()
        return words

    def generate_table(self,words):
        table = dict()
        counter = 0
        for x in words:
            if counter + 1 < len(words):
                if words[counter] in table:
                    new_words = table[words[counter]]
                    new_words.append(words[counter+1])
                    table[words[counter]] = new_words
                    counter = counter + 1
                else:
                    table[words[counter]] = [words[counter+1]]
                    counter = counter + 1

        return table

    def initial_word(self,table):
        initial_word = random.choice(list(table.keys()))
        return initial_word

    def build_sentence(self, initial_word, table):
        sentence = initial_word
        current_word = initial_word
        x = 0
        while x <= 3:
            if current_word in table:
                next_word = random.choice(table[current_word])
                sentence = sentence + " " + next_word
                current_word = next_word
                x = x + 1
            else:
                x = 4
        return sentence


MessageFrenzy.main(MessageFrenzy)
