frequencies = []

with open('input.txt', 'r') as f:
    frequencies = f.readlines()


def find_resulting_freq(frequencies):
    resulting_freq = 0
    for freq in frequencies:
        resulting_freq += int(freq)
    return resulting_freq


def find_first_freq_twice(frequencies):
    resulting_freq = 0
    previous_freqs = {}
    while True:
        for freq in frequencies:
            resulting_freq += int(freq)
            if resulting_freq in previous_freqs:
                return resulting_freq
            previous_freqs[resulting_freq] = False


first_part = find_resulting_freq(frequencies)
print('First part: {0}'.format(first_part))

second_part = find_first_freq_twice(frequencies)
print('Second part: {0}'.format(second_part))
