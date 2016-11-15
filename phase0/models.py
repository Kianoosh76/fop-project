from django.db import models


class Text(models.Model):
    text = models.TextField(max_length=10000)
    smallest_repeated_word = models.CharField(max_length=40)
    distinct_longest_words = models.IntegerField()

    def save(self, *args, **kwargs):
        words = self.text.split()
        max_length = 0
        max_len_repeat = {}
        repeats = {}
        for word in words:
            if len(word) > max_length:
                max_length = len(word)
                max_len_repeat.clear()
                max_len_repeat[word] = 1
            elif len(word) == max_length:
                max_len_repeat[word] = max_len_repeat.get(word, 0) + 1

            repeats[word] = repeats.get(word, 0) + 1

        max_repeat = 0
        smallest = ""
        for word, repeat in repeats.items():
            if repeat > max_repeat:
                max_repeat = repeat
                smallest = word
            elif repeat == max_repeat:
                smallest = min(smallest, word)

        self.smallest_repeated_word = smallest
        self.distinct_longest_words = len(max_len_repeat)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.text[0:min(len(self.text), 30)]