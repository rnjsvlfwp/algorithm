genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    dict_genre_plays = dict()
    length_genres = len(genre_array)
    genre_sum = 0
    result = []

    for dict_index in range(length_genres):
        if genres[dict_index] not in dict_genre_plays:
            dict_genre_plays[genres[dict_index]] = play_array[dict_index]
        else:
            dict_genre_plays[genres[dict_index]] += play_array[dict_index]

    sorted_dict_genre_plays = sorted(dict_genre_plays, reverse=True)

    dict_index_plays = dict()
    for a_genre in sorted_dict_genre_plays:
        for genre_index in range(length_genres):
            if genre_array[genre_index] == a_genre:
                dict_index_plays[genre_index] = play_array[genre_index]

        sorted_dict_index_plays = sorted(dict_index_plays.items(), key=lambda x: x[1], reverse=True)
        dict_index_plays = dict()

        for a_tuple in sorted_dict_index_plays:
            result.append(a_tuple[0])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
