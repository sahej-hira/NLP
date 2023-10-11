#!/usr/bin/env python
# coding: utf-8

# In[21]:


# corpus
# tokenization
# vectorization


# # corpus
# 

# In[22]:


corpus = "I think almost everyone used social media now. Not everyone. Twitter is our parent’s social media, instagram is our social media. Instagram suits gen-z  more comparatively . Twitter is more professional whereas instagram is more fun types. Twitter is political, whereas instagram is more of a gossip club, you can stack someone, since its more like a portfolio, usually used by models, celebrities, entertainers etc."


# # Tokenization

# In[23]:


# tokenization:

# Yes, tokenization can remove stopwords in NLP. 
# Stopwords are commonly used words that may not carry much information and may be able to be removed with little information loss.
# Tokenization is a technique for breaking down a piece of text into small units, called tokens. 
# To remove stopwords, the sentences must be converted into word tokens first, and then the stop words can be removed using a function like `remove_stopwords()`.
# The NLTK library in Python has a list of stopwords stored in 16 different languages, including English.





# ### Token
# 

# In[24]:


import nltk


# In[25]:


from nltk.tokenize import sent_tokenize, word_tokenize


# In[26]:


nltk.download('punkt')


# In[27]:


w_tokens = word_tokenize(corpus)
#print(w_tokens)


# ### Removing stopwords

# In[28]:


nltk.download('stopwords')


# In[31]:


from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


# In[33]:


# removing stopwords
filteredlist = [word for word in w_tokens if word.lower() not in stop_words]
print(filteredlist)


# In[38]:


# removing special characteres using isalnum():
filteredlist = [i for i in filteredlist if i.isalnum() == True]
print(filteredlist)


# # Vectorization

# In[39]:


# sentence
# vectorization 


# In[40]:


sentence = "Twitter is more of a professional setup, whereas instagram is unprofessional"


# In[42]:


# create list with each word
# vectorize
words = sentence.split(' ')   
# words will be a list
vector = []
for i in words:
    if i in filteredlist:
        count = 1
    else:
        count = 0
    vector.append(count)
print(vector)
    
    
    


# In[ ]:




