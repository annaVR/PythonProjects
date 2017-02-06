__author__ = 'anna'

"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [[] for i in range(10000)]

    def print_hash_table(self):
        for elem in self.table:
            if elem:
                print(self.table.index(elem), elem)

    def calculate_hash_value(self, string):
        """Helper function to calculate a
        hash value from a string."""
        h_value = ord(string[0]) * 100 + ord(string[1])
        return h_value


    def store(self, string):
        """Input a string that's stored in
        the table."""
        h_value = self.calculate_hash_value(string)
        self.table[h_value].append(string)

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # h_value = ord(string[0])*100 + ord(string[1])
        h_value = self.calculate_hash_value(string)
        if self.table[h_value] != []:
            if string in self.table[h_value]:
                return h_value
        return -1


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print('Should be -1:', hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print('Should be 8568:', hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print('Should be 8568:', hash_table.lookup('UDACIOUS'))

hash_table.print_hash_table()