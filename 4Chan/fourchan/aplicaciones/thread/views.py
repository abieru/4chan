from django.views.generic.base import TemplateView


class ThreadView(TemplateView):

    template_name = "thread/thread.html"