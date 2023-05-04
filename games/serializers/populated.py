from .common import GameSerializer
from genres.serializers.populated import PopulatedGenreSerializer
from comments.serializers.populated import PopulatedCommentSerializer
from devs.serializers.common import DevSerializer
from jwt_auth.serializers.common import UserSerializer


class PopulatedGameSerializer(GameSerializer):
    genres = PopulatedGenreSerializer(many=True)
    comments = PopulatedCommentSerializer(many=True)
    dev = DevSerializer()
    owner = UserSerializer()