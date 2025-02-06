class CountedIterator:
    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)  # The original iterator
        self.counter = 0  # Counter to keep track of the number of items iterated

    def __next__(self):
        """Override the next method to fetch the next item and increment the counter."""
        try:
            item = next(self.iterator)  # Get the next item from the iterator
            self.counter += 1  # Increment the counter
            return item
        except StopIteration:
            raise StopIteration  # Raise StopIteration when the iterator is exhausted

    def get_count(self):
        """Return the number of items that have been iterated over."""
        return self.counter
