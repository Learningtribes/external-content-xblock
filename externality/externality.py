"""TO-DO: Write a description of what this XBlock is."""

from django.template import Context, Template
from django.utils.translation import ugettext as _
import pkg_resources
from xblock.core import XBlock
from xblock.fields import Integer, String, Scope
from xblock.fragment import Fragment
from xblock.exceptions import JsonHandlerError


class ExternalContentXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    display_name = String(
        help=_("The name of the component seen by the learners."),
        display_name=_("Title Name"),
        default=_("External Web Content"),      # name that appears in advanced settings studio menu
        scope=Scope.settings
    )

    name = String(
        help=_("The name of the component seen by the learners."),
        display_name=_("Display Name"),
        scope=Scope.user_state
    )

    iframe_url = String(
        display_name=_("iFrame URL"),
        help=_("Copy/Paste the iFrame link from your external tool here, more...https://csc.learning-tribes.com/2021/05/26/adding-a-genially-component/"),
        default="",
        scope=Scope.user_state
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        return pkg_resources.resource_string(__name__, path).decode("utf8")

    def render_template(self, template_path, context={}):
        """Evaluate a template by resource path, applying the provided context"""
        template = Template(self.resource_string(template_path))

        return template.render(Context(context))

    def xblock_field_list(self, field_names):
        """Handy helper for getting a dictionary of fields"""
        xblock = self

        return [
            {
                'name': field,
                'value': getattr(xblock, field),
                'help': getattr(xblock.__class__, field).help,
                'display_name': getattr(xblock.__class__, field).display_name,
                'type': type(getattr(xblock.__class__, field)).__name__
            } for field in field_names
        ]

    def student_view(self, context=None):
        """
        The primary view of the ExternalContentXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("templates/html/externality.html")

        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/externality.css"))
        frag.add_javascript(self.resource_string("static/js/src/externality.js"))
        frag.initialize_js('ExternalContentXBlock')

        return frag

    def studio_view(self, context=None):
        """
        The studio view of the ExternalContentXBlock, with form
        """
        frag = Fragment()
        frag.add_content(
            self.render_template(
                'templates/html/studio-externality.html',
                {'self': self, 'fields': self.xblock_field_list(['name', 'iframe_url'])}
            )
        )
        frag.add_css(self.resource_string("static/css/externality.css"))
        frag.add_javascript(self.resource_string("static/js/src/studio-externality.js"))
        frag.initialize_js('ExternalContentXBlock')

        return frag

    @XBlock.json_handler
    def publish_completion(self, data, dispatch):  # pylint: disable=unused-argument
        """
        Entry point for completion for student_view.
        Parameters:
            data: JSON dict:
                key: "completion"
                value: float in range [0.0, 1.0]
            dispatch: Ignored.
        Return value: JSON response (200 on success, 400 for malformed data)
        """
        completion_service = self.runtime.service(self, 'completion')

        # if completion_service is None:
        #     raise JsonHandlerError(500, u"No completion service found")
        # elif not completion_service.completion_tracking_enabled():
        #     raise JsonHandlerError(404, u"Completion tracking is not enabled and API calls are unexpected")
        # if not isinstance(data['completion'], (int, float)):
        #     message = u"Invalid completion value {}. Must be a float in range [0.0, 1.0]"
        #     raise JsonHandlerError(400, message.format(data['completion']))
        # elif not 0.0 <= data['completion'] <= 1.0:
        #     message = u"Invalid completion value {}. Must be in range [0.0, 1.0]"
        #     raise JsonHandlerError(400, message.format(data['completion']))

        self.runtime.publish(self, "completion", data)

        return {"result": "ok"}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ExternalContentXBlock",
             """<externality/>
             """),
            ("Multiple ExternalContentXBlock",
             """<vertical_demo>
                <externality/>
                <externality/>
                <externality/>
                </vertical_demo>
             """),
        ]
