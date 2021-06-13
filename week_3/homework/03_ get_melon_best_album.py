genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다. index
# 3. 장르 내에서 재생 횟수가 같다면 고유 번호가 낮은 노래 먼저 수록한다.
# 장르 별(key)로 우선 재생된 횟수(value)를 저장해야 한다. : 딕 사용하자
# 장르 별로 곡의 정보(인덱스, 재생횟수) 배열로 묶어 저장한다.

def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {}
    genre_total_play_array_dick = {}
    n = len(genre_array)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        # 딕은 초기값이기 때문에 아무것도 없는 none에서 시작 
        # none 일 경우에는 값만 저장할 수 있도록 제어
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            # 장르별로 여러 곡이 저장될 것이기 때문에 배열로 저장한다.
            genre_total_play_array_dick[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            # 장르 토탈이 있다는 것은 이미 배열이 존재한다는 것
            # 때문에 있는 배열에 append 로 추가하면 됨
            genre_total_play_array_dick[genre].append([i, play])
    print(genre_total_play_dict)
    print(genre_total_play_array_dick)

    # 가장 많은 재생 횟수를 가진 노래로 순으로 정렬하려면
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item : item[1], reverse=True)
    print(sorted_genre_play_array)

    result = []

    for genre, _value in sorted_genre_play_array:
        # [1, 600], [4, 2500]
        index_play_array = genre_total_play_array_dick[genre]
        sorted_index_play_array = sorted(index_play_array, key=lambda  item: item[1], reverse=True)
        # print(sorted_index_play_array)

        for i in range(len(sorted_index_play_array)):
            if i > 1:
                break
            result.append(sorted_index_play_array[i][0])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!