

#import necessary libraries
from googletrans import Translator

#get the text to be translated and the language to translate to
text = input('Enter the text to be translated: ')
language = input('Enter the language to translate to: ')

#create the translator object
translator = Translator()

#translate the text
translation = translator.translate(text, dest=language).text

#get the file name from the user
filename = input('Enter the file name for the translation: ')

#open the file and write the translation to it
with open(filename, 'w', encoding='utf-8') as f:
    f.write(translation)