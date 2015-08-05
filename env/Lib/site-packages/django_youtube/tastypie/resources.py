from tastypie.resources import Resource


class YoutubeResource(Resource):
    """
    Api resource for youtube operations
    GET:
        Creates a new browser based upload instance to initiate upload on youtube
        Returns the post_url and token
    """

    class Meta:
        allowed_methods = ['get']
