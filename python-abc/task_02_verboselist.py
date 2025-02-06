class VerboseList(list):
    def append(self, item):
        """Override append to print a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Override extend to print a message."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Override remove to print a message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Override pop to print a message."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
