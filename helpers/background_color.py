from phase1.models import Config


class BackgroundColorMixin:

    @staticmethod
    def get_color():
        return Config.get_solo().background_color

    def get_context_data(self):
        context = super().get_context_data()
        context['background_color'] = self.get_color()
        return context
