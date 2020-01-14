from rest_framework.serializers import HyperlinkedModelSerializer

from ghosts import models


class BoastsAndRoastsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.BoastsAndRoasts

        fields = [
            'id',
            'is_boast',
            'content',
            'upvote',
            'downvote',
            'total_votes',
            'post_date'
        ]
