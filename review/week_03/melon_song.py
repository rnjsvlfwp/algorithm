genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 950, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    genres_play_dict = {}
    genre_array_length = len(genre_array)

    for genre_index in range(genre_array_length):
        if genre_array[genre_index] not in genres_play_dict:
            genres_play_dict[genre_array[genre_index]] = play_array[genre_index]
        else:
            genres_play_dict[genre_array[genre_index]] += play_array[genre_index]

    sorted_genres_play_dict = sorted(genres_play_dict, reverse=True)

    index = 0
    result = [0] * genre_array_length
    for a_genre in sorted_genres_play_dict:
        index_play_dict = {}
        for genres_play_index in range(genre_array_length):
            if a_genre == genre_array[genres_play_index]:
                index_play_dict[genres_play_index] = play_array[genres_play_index]

        sorted_index_play_dict = sorted(index_play_dict.items(),  key=lambda item: item[1], reverse=True)
        print(sorted_index_play_dict)

        for a_set in sorted_index_play_dict:
            result[a_set[0]] = index
            index += 1

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
