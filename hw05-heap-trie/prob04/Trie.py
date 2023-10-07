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
        return self.iterate_root_children()
    
    def iterate_root_children(self, current = None, prefix = "", results = []):
        print("INSIDE iterate")
        print("prefix =", prefix)

        # set current to root node
        if current is None:
            current = self.root

        # what does sorted do?
        # key = char
        # node = TrieNode object
        # children = { 'h':TrieNode, 'r':TrieNode }

        #items = current.children.items()
        #print("items =", items)
        #print("length items =", len(items))

        for key, node in sorted(current.children.items()):

            if key == self.end_char:
                # if node.freq > 1:
                #     results.append(prefix)
                # else:
                    results.append(prefix[0])

            # elif len(prefix) == node.freq:
            #     results.append(prefix)

            else:
                if node is not None and node.freq > 1:
                    print("node value =", node.value)
                    print("node frequency =", node.freq)
                    print("prefix =", prefix)
                
                if node.freq > 1 and len(prefix) == node.freq:
                    results.append(prefix)

                self.iterate_root_children(node, prefix + key, results)

        print("results =", results)
        return results


    def shortest_prefix(self, current = None, prefix = "", results = []):

        # set current to root node
        if current is None:
            current = self.root
        

        
        # for each of current's children, iterate through the chars
        for child in current.children:

            if len(current.children) > 1:
                print("number children =", len(current.children[child]))


            if child == "*":
                print("LAST LETTER")
                results.append(prefix[0])
                prefix = ""
            
                # ?? - how do I go to the next child of the root node?

            else:
                # add char to prefix
                prefix += child

                # update current
                return self.shortest_prefix(current.children[child], prefix, results)
            
            current = current.children[child]
            print("prefix =", prefix)


        return results


    # def shortest_prefix(self, current = None, prefix = "", i = 0, results = []):

    #     # set current to root node
    #     if current is None:
    #         current = self.root

    #     # child is a char => 'a', 'c'
    #     for i, child in enumerate(current.children):

    #         print("current.children =", current.children.i)

    #         # length of current.children:
    #         #length = len(current.children)
    #         #print("length =", length)

    #         if child == "*":
    #             print("INSIDE END")
    #             results.append(prefix[0])
    #             # repeat with next child and an empty prefix
    #             i += 1

    #         else:
    #             prefix += child
    #             print("prefix =", prefix)
    #             #current = current.children[child]
    #             return self.shortest_prefix(current.children[child], prefix, i, results)
            
    #         return self.shortest_prefix(current.children[i], "", i, results)

    #     return results
     

            # if length == 0:

            # results.append(child)
        
            # does child have any children?
            # YES
            # => this prefix is not unique
            # => add child character to prefix
            # => update current to its children
            # => call shortest_prefix with updated current and prefix
            # current = current.children[child]
            # print('current =', current)

            # NO
            # => then this child is the shortest unique prefix
            # add prefix to results
            # set 
            #searchResults = self.search(child)
            #print("searchResults =", searchResults.value)


            #print('child =', child)
  
            #print("result =", results)

          
        #return results


    


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
    
