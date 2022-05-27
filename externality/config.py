

class _ExternalComponent(object):
    """Hold information of an external web content component
    """
    TAG_INFOGRAPHICS = r'Infographics'
    TAG_PRESENTATION = r'Presentation'
    TAG_VIDEO = r'Video'
    TAG_COLLABORATIVE = r'Collaborative'
    TAG_POLL = r'Poll'
    TAG_SCREEN_RECORDER = r'Screen Recorder'

    ALL_TAGS = [TAG_INFOGRAPHICS, TAG_PRESENTATION, TAG_VIDEO, TAG_COLLABORATIVE, TAG_POLL, TAG_SCREEN_RECORDER]

    def __init__(self, icon, name, description, tags, paying, site_link):
        self.icon = icon
        self.name = name
        self.description = description
        self.tags = list(tags) if isinstance(tags, (list, tuple)) else [tags]
        self.paying = paying
        self.site_link = site_link

        if not all([tag in _ExternalComponent.ALL_TAGS for tag in self.tags]):
            raise NameError('Unsupported tags : {}'.format(str(self.tags)))

    def get_tags_set(self):
        return set(self.tags)

    def __str__(self):
        return self.name


class SupportedExternalResources(object):
    """An iterable object definition for listed `Tags` & `Sites`
    """
    def __init__(self):
        self._listed_tags = set()
        self._resources = []

        self._add_resource(
            icon='None', name='Canva',
            tags=_ExternalComponent.TAG_PRESENTATION,
            paying='',
            site_link=r'https://www.canva.com/',
            description='Design absolutely anything, from logos and social media content to documents, prints and more.'
        )
        self._add_resource(
            icon='None', name='Genially',
            tags=[_ExternalComponent.TAG_PRESENTATION, _ExternalComponent.TAG_INFOGRAPHICS],
            paying='',
            site_link=r'https://genial.ly/en/',
            description='Helps you record and share interactive videos. Users can log social reactions into your content to help you maximize engagement.'
        )
        self._add_resource(
            icon='None', name='H5P',
            tags=[_ExternalComponent.TAG_PRESENTATION, _ExternalComponent.TAG_INFOGRAPHICS, _ExternalComponent.TAG_VIDEO],
            paying='',
            site_link=r'https://h5p.org/',
            description='Create interactive video, presentation or animated content (such as accordion, chart, collage, image slider, dialogue, chart...)'
        )
        self._add_resource(
            icon='None', name='Loom',
            tags=_ExternalComponent.TAG_SCREEN_RECORDER,
            paying='',
            site_link=r'https://www.loom.com/',
            description='Record quick videos of your screen and cam.'
        )

    def _add_resource(self, *args, **kwargs):
        external_component = _ExternalComponent(*args, **kwargs)
        self._listed_tags.update(external_component.get_tags_set())
        self._resources.append(external_component)

    def __iter__(self):
        return iter(self._resources)

    @property
    def listed_tags(self):
        return list(self._listed_tags)


SUPPORTED_EXTERNAL_RESOURCES = SupportedExternalResources()
