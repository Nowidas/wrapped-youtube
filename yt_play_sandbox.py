import pafy
import os
import vlc

os.add_dll_directory(os.getcwd())
to_play_querry = features[features['playlist_name'] == 'Noviyaa'][['video_id', 'video_feature_acousticness']].dropna().sort_values('video_feature_acousticness', ascending=True)
to_play_querry = list(to_play_querry['video_id'])
p = vlc.MediaPlayer()
for q in to_play_querry:
    url = "https://www.youtube.com/watch?v=" + q
    video = pafy.new(url, basic=False)
    try:
        best = video.getbest()
    except:
        print('NEXT song')
    finally:
        playurl = best.url
        print(playurl)

        p.set_media(playurl)
        p.play()

        from time import sleep

        sleep(10)  # Or however long you expect it to take to open vlc
        while p.is_playing():
            try:
                sleep(2)
            except:
                p.stop()
                break
        print('NEXT song')