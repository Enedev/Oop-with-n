import re

forbidden_words_file = open('english.txt', 'r', encoding='utf-8').read()
forbidden_words = forbidden_words_file.split()

songs_data = {}

def count_unique_words_in_song(song):
    unique_words = set(song)
    return len(unique_words)

def count_unique_words_in_all_songs():
    all_lyrics = list(songs_data.values())

    unique_words = []
    for lyrics in all_lyrics:
        unique_words.extend(lyrics)

    print(f'The songs contain {len(set(unique_words))} different words')
    return unique_words

def remove_punctuation(song):
    sanitized_song = []
    for word in song:
        word = re.sub(r'[^\w\s]', '', word)
        sanitized_song.append(word)
    return sanitized_song

def read_songs_data():
    for i in range(3):
        song_text = open(f'song{i + 1}.txt', 'r', encoding='utf-8').read()
        song_text = song_text.lower().split()
        
        sanitized_song = remove_punctuation(song_text)
        songs_data[f'song{i + 1}'] = sanitized_song

def get_unique_words_per_song():
    for song_name, lyrics in songs_data.items():
        unique_words_count = count_unique_words_in_song(lyrics)
        print(f'- {song_name} has {unique_words_count} unique words')

def get_top_5_most_used_words():
    word_counts = {}
    all_lyrics = list(songs_data.values())
    all_lyrics = [word for sublist in all_lyrics for word in sublist]

    for word in all_lyrics:
        if word in forbidden_words:
            continue
        elif word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    print(f'The top 5 most used words are:')
    for i in range(5):
        print(f'{i + 1}. {sorted_word_counts[i][0]}')

def main():
    read_songs_data()
    get_unique_words_per_song()
    count_unique_words_in_all_songs()
    get_top_5_most_used_words()

main()
