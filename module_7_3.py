import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    # Приводим строку к нижнему регистру и удаляем пунктуацию
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', string.punctuation))
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Позиция начинается с 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


# Пример использования:
if __name__ == "__main__":
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
    print(finder1.get_all_words())
    print(finder1.find('captain'))
    print(finder1.count('captain'))