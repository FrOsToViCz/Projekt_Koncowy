from django.forms.widgets import RadioSelect


class StarRatingWidget(RadioSelect):
    template_name = 'widgets/star_rating.html'

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        option['attrs']['class'] = 'star-rating'
        return option
