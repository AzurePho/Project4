from .common import GenreSerializer
from games.serializers.common import GameSerializer

# extending the GenreSerializer gives us the name of the id of the genre
class PopulatedGenreSerializer(GenreSerializer):
    # then we add the albums using the AlbumSerializer. Each Album has the ID of the genres, so 
    # the serialiser goes and matches all albums with the ID of the genre it is deserializing and
    # adds the data in
        games = GameSerializer(many=True)