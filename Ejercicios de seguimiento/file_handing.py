import re

#read forbidden words that we will ignore through this process
wrong_words_file = open('english.txt', 'r', encoding='utf-8').read()
wrong_words = wrong_words_file.split()

songs = {}

def different_words_in_song(song):
    song_set = set(song)
    return len(song_set)

def different_word_in_all_songs():
    all_lyrics = list(songs.values())

    different_words = []
    #Joining all the songs into one array
    for array in all_lyrics:
        different_words.extend(array)

    #Converting it to a set
    print(f'The songs use {len(set(different_words))} different words')
    return different_words

def remove_punct(song):
    new_song = []
    for word in song:
        word = re.sub(r'[^\w\s]', '', word)
        new_song.append(word)
    return new_song


def reading_songs():
    #Saving total songs
    for i in range(3):
        song = open(f'song{i + 1}.txt', 'r', encoding='utf-8').read()
        remove_spaces = song.lower().split()
        
        final_song = remove_punct(remove_spaces)

        songs[f'song{i + 1}'] = final_song


def get_diff_words_single_song(): 
    for song in songs:
        actual_song = []
        for lyric in songs[song]:
            actual_song.append(lyric)
        print(f'- {song} has {different_words_in_song(actual_song)} different words')

def get_5_most_used_words():
    most_used_words = {}
    #Converting the separate lyrics array into a single one
    unified_list = list(songs.values())
    final_list = []
    for lyrics in unified_list:
        final_list.extend(lyrics)

    #Counting the words
    for word in final_list:
        #Ignore word if it's in forbidden list
        if word in wrong_words:
            continue
        #add to the word in dict
        elif word in most_used_words:
            most_used_words[word] += 1
        #Create a new word in the dictionary
        else:
            most_used_words[word] = 1

    sorted_dict = dict(sorted(most_used_words.items(), key=lambda x: x[1], reverse=True))

    print(f'The five more used words are: ')
    for i in range(5):
        print(i + 1, list(sorted_dict.keys())[i])

def main():
    #Reading songs
    reading_songs()
    #Getting different words used in a single song
    get_diff_words_single_song()
    #Getting different words used in all songs
    different_word_in_all_songs()

    #Use the list we got from the lattest function to use it to get the 5 most used words
    get_5_most_used_words()

main()