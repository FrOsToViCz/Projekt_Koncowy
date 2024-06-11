from django.forms.widgets import RadioSelect


class StarRatingWidget(RadioSelect):
    template_name = 'widgets/star_rating.html'

    def __init__(self, attrs=None):
        choices = [(i, '★' * i) for i in range(1, 6)]
        super().__init__(attrs, choices)
