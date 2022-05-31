from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ("Cars", "Cars"),
        ("Agro", "Agro"),
        ("Eda", "Eda"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            "media_type",
        ]

    def parse_data(self):
        if self.data['media_type'] == "Cars":
            cars_parser = parser.parser_func()
            for data in cars_parser:
                models.Cars.objects.create(**data)
        elif self.data['media_type'] == "Agro":
            agro_parser = parser.parser_func_agro()
            for data in agro_parser:
                models.Agro.objects.create(**data)
        elif self.data['media_type'] == "Eda":
            eda_parser = parser.parser_func_eda()
            for data in eda_parser:
                models.Eda.objects.create(**data)
