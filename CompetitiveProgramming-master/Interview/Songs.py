def solution(songs, animations):
    ans = []
    song_dict = {}
    for song in songs:
        temp =song.split(':')
        song_dict[temp[0]] = int(temp[1])

    anim_dict = {}
    for anim in animations:
        temp = anim.split(':')
        anim_dict[temp[0]] = int(temp[1])

    for i in song_dict:
        for j in anim_dict:
            if song_dict[i]%anim_dict[j] == 0:
                ans.append(j + ':' +str(song_dict[i]//anim_dict[j]))
                break   

    return ans

print(solution(['notion:180','voy:185','samp:180'],['circle:360','sq:180','line:37']))