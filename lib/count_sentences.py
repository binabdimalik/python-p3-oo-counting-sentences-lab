#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        text = self.value
        text = text.replace('?', '.')
        text = text.replace('!', '.')
        potential_sentences = text.split('.')
        valid_sentences = [s for s in potential_sentences if s.strip()]
        return len(valid_sentences)
