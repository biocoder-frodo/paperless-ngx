# Generated by Django 1.9 on 2016-01-26 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0006_auto_20160123_0430"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="match",
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name="tag",
            name="matching_algorithm",
            field=models.PositiveIntegerField(
                blank=True,
                choices=[
                    (1, "Any"),
                    (2, "All"),
                    (3, "Literal"),
                    (4, "Regular Expression"),
                ],
                help_text='Which algorithm you want to use when matching text to the OCR\'d PDF.  Here, "any" looks for any occurrence of any word provided in the PDF, while "all" requires that every word provided appear in the PDF, albeit not in the order provided.  A "literal" match means that the text you enter must appear in the PDF exactly as you\'ve entered it, and "regular expression" uses a regex to match the PDF.  If you don\'t know what a regex is, you probably don\'t want this option.',
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="colour",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "#a6cee3"),
                    (2, "#1f78b4"),
                    (3, "#b2df8a"),
                    (4, "#33a02c"),
                    (5, "#fb9a99"),
                    (6, "#e31a1c"),
                    (7, "#fdbf6f"),
                    (8, "#ff7f00"),
                    (9, "#cab2d6"),
                    (10, "#6a3d9a"),
                    (11, "#b15928"),
                    (12, "#000000"),
                    (13, "#cccccc"),
                ],
                default=1,
            ),
        ),
    ]