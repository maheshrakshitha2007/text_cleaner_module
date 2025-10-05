#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# In[4]:


nltk.download('stopwords')
nltk.download('wordnet')


# In[5]:


class TextCleaner:
    def __init__(self, lowercase=True, remove_stopwords=True, lemmatize=True):
        self.lowercase = lowercase
        self.remove_stopwords = remove_stopwords
        self.lemmatize = lemmatize
        self.stop_words = set(stopwords.words('english'))
        self.filler_words = {"uh", "um", "like"}
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text):
     
        if self.lowercase:
            text = text.lower()

     
        text = text.translate(str.maketrans('', '', string.punctuation))

     
        words = text.split()

        
        cleaned_words = [
            w for w in words 
            if w not in self.filler_words and (not self.remove_stopwords or w not in self.stop_words)
        ]

        
        if self.lemmatize:
            cleaned_words = [self.lemmatizer.lemmatize(w) for w in cleaned_words]

       
        return ' '.join(cleaned_words)


# In[6]:


cleaner = TextCleaner()
sample_text = "Uh, I really like this movie! It's amazing, um, and beautiful."
print(cleaner.clean_text(sample_text))


# In[ ]:





# In[8]:


get_ipython().run_cell_magic('writefile', 'text_cleaner.py', '\nimport re\nimport string\nimport nltk\nfrom nltk.corpus import stopwords\nfrom nltk.stem import WordNetLemmatizer\n\nclass TextCleaner:\n    def __init__(self, lowercase=True, remove_stopwords=True, lemmatize=True):\n        self.lowercase = lowercase\n        self.remove_stopwords = remove_stopwords\n        self.lemmatize = lemmatize\n        self.stop_words = set(stopwords.words(\'english\'))\n        self.filler_words = {"uh", "um", "like"}\n        self.lemmatizer = WordNetLemmatizer()\n\n    def clean_text(self, text):\n        if self.lowercase:\n            text = text.lower()\n        text = text.translate(str.maketrans(\'\', \'\', string.punctuation))\n        words = text.split()\n        cleaned_words = [\n            w for w in words \n            if w not in self.filler_words and (not self.remove_stopwords or w not in self.stop_words)\n        ]\n        if self.lemmatize:\n            cleaned_words = [self.lemmatizer.lemmatize(w) for w in cleaned_words]\n        return \' \'.join(cleaned_words)\n')


# In[9]:


from text_cleaner import TextCleaner

cleaner = TextCleaner()
print(cleaner.clean_text("Uh, this is like really amazing and cool!"))


# In[ ]:




