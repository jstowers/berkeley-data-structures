#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from dsa.Trie import Trie


# In[ ]:


t = Trie()
t.insert("better")
t.insert("call")
t.insert("saul")
t.insert("break")
t.insert("breaking")
t.insert("bad")
t.insert("badly")
t.insert("bask")
t.insert("basket")
t.insert("basketball")
print(t.print_words())


# search
# * returns trie node if found
# * returns none if the string is not found
# 

# In[ ]:


node = t.search("bad")


# In[ ]:


node


# In[ ]:


node.children


# In[ ]:


node = t.search("ba")


# In[ ]:


node.children


# In[ ]:


node = t.search("good")


# In[ ]:


node = t.search("baddest")


# autocomplete - return words that match given prefix

# In[ ]:


t.autocomplete("a")


# In[ ]:


t.autocomplete("b")


# In[ ]:


t.autocomplete("bad")


# suggest - return closest match by prefix

# In[ ]:


t.suggest("b")


# In[ ]:


t.suggest("brown")


# In[ ]:


t.suggest("believe")


# In[ ]:


t.suggest("minton")


# In[ ]:


t.suggest("breakneck")


# #### delete
# 
# 

# In[ ]:


t.print_words()


# ##### delete should be post order

# In[ ]:


t.delete("breaking")


# In[ ]:


t.print_words()


# In[ ]:


t.delete("breaking")


# In[ ]:


t.print_words()


# In[ ]:


t.insert("breaking")


# In[ ]:


t.print_words()


# In[ ]:


t.delete("breaking")


# In[ ]:


t.print_words()


# ##### delete preorder has unintended results

# In[ ]:


t.delete_preorder("saul")


# In[ ]:


t.print_words()


# In[ ]:


t.delete_preorder("break")


# In[ ]:


t.print_words()


# In[ ]:





# ### Tries vs Arrays

# naive word list - find words with prefix

# In[ ]:


def naive_word_list(word_file):
    with open(word_file) as f:
        wl = [word.strip() for word in f.readlines()]
    return wl

def find_words(wl, prefix):
    return [word for word in wl if word.startswith(prefix)]

wl = naive_word_list("words.txt")
            
len(wl)         


# In[ ]:


find_words(wl, 'automat')


# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'matches = find_words(wl, "automat")\nmatches = find_words(wl, "x")\nmatches = find_words(wl, "chroma")\nmatches = find_words(wl, "multi")\n')


# In[ ]:





# trie find words with prefix is much faster

# In[ ]:


from dsa.Trie import Trie


# In[ ]:


def create_spelling_tries(word_file):
    trie = Trie()
    with open(word_file) as f:
        for word in f.readlines():
            trie.insert(word.strip())

    return trie


        


# In[ ]:


t = create_spelling_tries("words.txt")


# In[ ]:


t.autocomplete('automat')


# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'matches = t.autocomplete("automat")\nmatches = t.autocomplete("x")\nmatches = t.autocomplete("chroma")\nmatches = t.autocomplete("multi")\n')


# spell checker

# In[ ]:


def check_sentence(tries, sentence):
    misspellings = []
    new_string = sentence.translate(str.maketrans('', '', '.?!@#()&%$'))
    for word in new_string.lower().split():
        print(word)
        if not tries.search(word):
            misspellings.append(word)
            
    return misspellings

check_sentence(t, "Thsi is a mispeled sentense.")


# In[ ]:




