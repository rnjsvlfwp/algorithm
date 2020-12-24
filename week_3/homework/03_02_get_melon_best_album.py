genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    dict_total_genre_plays = dict()
    dict_each_genre_plays = dict()
    length_genres = len(genre_array)
    result = []

    for dict_index in range(length_genres):
        if genre_array[dict_index] not in dict_total_genre_plays:
            dict_total_genre_plays[genre_array[dict_index]] = play_array[dict_index]
            dict_each_genre_plays[genre_array[dict_index]] = [[dict_index, play_array[dict_index]]]
        else:
            dict_total_genre_plays[genre_array[dict_index]] += play_array[dict_index]
            dict_each_genre_plays[genre_array[dict_index]].append([dict_index, play_array[dict_index]])


    sorted_total_dict_index_plays = sorted(dict_total_genre_plays.items(), key=lambda items: items[1], reverse=True)
    print(sorted_total_dict_index_plays)

    for key, value in sorted_total_dict_index_plays:
        index_play_array = dict_each_genre_plays[key]
        # print(index_play_array)
        sorted_index_play_array = sorted(index_play_array, key=lambda items: items[1], reverse=True)
        print(sorted_index_play_array)
        for index in range(len(sorted_index_play_array)):
            result.append(sorted_index_play_array[index][0])

    return result








print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
