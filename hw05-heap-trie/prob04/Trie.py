class TrieNode:
    def __init__(self, value):
        self.children = {}
        self.value = value
        self.freq = 1

class Trie:
    def __init__(self):
        self.root = TrieNode("")
        self.end_char = "*"
            
    def insert(self, word):
        current = self.root
        for c in word:

            if c not in current.children:
                current.children[c] = TrieNode(c)
            else:
                current.children[c].freq += 1
            current = current.children[c]
        current.children[self.end_char] = None
        current.is_end = True

    def longest_prefix_from_array(self, array):

        # check for empty array
        if len(array) == 0:
            raise Exception("array is empty")
        
        # add each word to trie
        for word in array:
            self.insert(word)

        # find longest prefix
        return self.longest_prefix()

    def longest_prefix(self, current = None, prefix =""):
        
        # set current to root node
        if current is None:
            current = self.root

        # once there is more than 1 child, 
        # the longest prefix ends
        if len(current.children) != 1 or current == "*":
            if len(prefix) == 0:
                return None
            else: return prefix

        # longest prefix continues to build 
        # one character at a time
        if len(current.children) == 1:
            for child in current.children:
                prefix += child
                current = current.children[child]
        
        return self.longest_prefix(current, prefix)
    
    def shortest_prefix_from_array(self, array):

        # check for empty array
        if len(array) == 0:
            raise Exception("array is empty")
        
        # add each word to trie
        for word in array:
            self.insert(word)

        # find shortest prefix
        return self.shortest_prefix(None, "", [])
    
    def shortest_prefix(self, current = None, prefix = "", results = []):
    
        # set current to root node
        if current is None:
            current = self.root

        for key, node in sorted(current.children.items()):

            # iteration reaches end of word (*)
            if key == self.end_char:
                #print("end of word")
                if current.freq > 1:
                    #print("append for multiple child")
                    results.append(prefix)
                else:
                    #print("append for single child")
                    results.append(prefix[0])
                
            # iteration reaches node with children > 1
            # recursion call for multiple children
            elif node.freq > 1:
                self.shortest_prefix(node, prefix + key, results)

            else:
                if current.freq > 1:
                    #print("append for freq > 1")
                    results.append(prefix+key)
                    #print("continue")
                    continue
                
                #print("other recursion call")
                # recursion call for single child
                self.shortest_prefix(node, prefix + key, results)

        return results

    # Search receives a target string, s, and iterates through
    # each char, c, of the string.
    #
    # If the target string exists in the trie, search returns the
    # last TrieNode of the target string.
    # If the target string does not exist, search returns None.
    def search(self, s):
        if len(s) == 0:
            return None

        current = self.root
        for c in s:
            if c not in current.children:
                return None
            current = current.children[c]
        return current
    
    def delete(self, word, i=0, current=None):
        if i == len(word):
            return True

        if current is None:
            current = self.root
            word = word + self.end_char

        char = word[i]
        if char not in current.children:
            return False
        
        next_node = current.children[char]
        print("pre: ",word, char, i+1)
        should_delete_ref = self.delete(word, i + 1, next_node)
        print("post: ",word, char, i+1, should_delete_ref)

        if should_delete_ref:
            del current.children[char]
            return len(current.children) == 0
        return False
    
    def delete_preorder(self, word, i=0, current=None):
        if i == len(word):
            return True

        if current is None:
            current = self.root
            word = word + self.end_char

        char = word[i]
        if char not in current.children:
            return False
        
        next_node = current.children[char]

        del current.children[char]

        should_delete_ref = self.delete(word, i + 1, next_node)

        return False

    def print_keys(self, current):
        if current is None:
            return

        for c in current.children:
            self.print_keys(current.children[c])
            
    def print_words(self, node=None, word="", words=None):
        if words is None:
            words = []
        current = node
        if node is None:
            current = self.root
        
        for key, node in sorted(current.children.items()):
            if key == self.end_char:
                words.append(word)
            else:
                self.print_words(node, word + key, words)
        return words
    
    def autocomplete(self, prefix):
        current = self.search(prefix)
        if current is None:
            return None
        return self.print_words(current, prefix)
    
    def suggest(self, s):
        if s is None or len(s) == 0:
            return None
        suggestions = self.autocomplete(s)
        if suggestions is None or len(suggestions) == 0:
            return self.suggest(s[:-1])
        else:
            return suggestions
    
