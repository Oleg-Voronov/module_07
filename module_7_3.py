class WordsFinder:
    __PUNCTUATION = ('\n',',', '.', '=', '!', '?', ';', ':', ' - ')
    def __init__(self,*files):
        self.file_names = list(files)

    def get_all_words(self):
        rezz ={} # результат
        for f_name in self.file_names:
            string_of_words = ''
            with open(f_name,'r',encoding='utf-8') as file:
                string_of_words = file.read()
            string_of_words = string_of_words.lower()
            for punc in self.__PUNCTUATION:
                string_of_words = string_of_words.replace(punc,' ')
            chekk = False
            while not chekk: #проверка-удаление двойных пробелов
                str_ = string_of_words.replace('  ', ' ')
                if str_ == string_of_words: chekk = True
                string_of_words = str_
            rezz.update({f_name:string_of_words.split(' ')})
        return rezz

    def find(self,word):
        rezz = {} # результвт поиска
        word=word.lower()
        db_words = self.get_all_words()
        for name, words in db_words.items():
            for i in range(0,len(words)):
                if word == words[i]:
                    rezz.update({name:i+1})
                    break
        return rezz

    def count(self,word):
        rezz = {}  # результвт поиска
        word = word.lower()
        db_words = self.get_all_words()
        for name, words in db_words.items():
            count_ = 0 # сколько раз в файле
            for str_ in words:
                if word == str_: count_+=1
            if count_ > 0:
                rezz.update({name:count_})
        return rezz

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
