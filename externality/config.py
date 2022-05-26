

class _ExternalComponent(object):
    TAG_INFOGRAPHICS = r'Infographics'
    TAG_PRESENTATION = r'Presentation'
    TAG_VIDEO = r'Video'
    TAG_COLLABORATIVE = r'Collaborative'
    TAG_POLL = r'Poll'
    TAG_SCREEN_RECORDER = r'Screen Recorder'

    ALL_TAGS = [TAG_INFOGRAPHICS, TAG_PRESENTATION, TAG_VIDEO, TAG_COLLABORATIVE, TAG_POLL, TAG_SCREEN_RECORDER]

    def __init__(self, icon, name, description, tags, paying, site_link):
        self._icon = icon
        self._name = name
        self._description = description
        self._tags = list(tags) if isinstance(tags, [list, tuple]) else [tags]
        self._paying = paying
        self._site_link = site_link

        if not all([tag in ALL_TAGS for tag in self._tags]):
            raise NameError('Unsupported tags : {}'.format(str(self._tags)))

    def __str__(self):
        return self._name


SUPPORTED_EXTERNAL_RESOURCES = [
    _ExternalComponent(
        icon='None', name='Genially',
        tags='', paying='',
        site_link=r'https://genial.ly/en/',
        description='Helps you record and share interactive videos. Users can log social reactions into your content to help you maximize engagement.'
    ),
    _ExternalComponent(
        icon='None', name='Canva',
        tags='', paying='',
        site_link=r'https://www.canva.com/',
        description='Design absolutely anything, from logos and social media content to documents, prints and more.'
    )
]
