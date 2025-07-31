from lib.song import Song
from lib.tag import Tag
from lib.song_tag import SongTag

def run():

    song_one = Song.find_by_title("Pickup Artist")
    tag_one = Tag.find_by_title("BPM: 120")


    print(Song.get_all())
    print(Tag.get_all())
    print(SongTag.get_all())

    

if __name__ == "__main__":
    run()
    

