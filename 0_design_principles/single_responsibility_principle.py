# SRP: one class, one task
# do not overload a class with too many respo

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    # crud tasks
    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # persistence tasks
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


# solution: class for persistence
# delegate persistence for any kind of object
class PersistenceManager:
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()

    def load_from_file(filename):
        pass


j = Journal()
j.add_entry("I wrote some code.")
j.add_entry("I found many bugs.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = 'journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
