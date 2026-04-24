from django.db import models


class Education(models.Model):
    LEVEL_CHOICES = [
        ('school', 'School'),
        ('college', 'College'),
        ('university', 'University'),
        ('other', 'Other'),
    ]

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='school')
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, blank=True,
                              help_text="e.g. SSC, HSC, BSc in Computer Science")
    period = models.CharField(max_length=50, blank=True,
                              help_text="e.g. 2019 – 2021")
    location = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='education/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0,
                                        help_text="Lower numbers show first")

    class Meta:
        ordering = ['order', '-id']
        verbose_name = 'Education entry'
        verbose_name_plural = 'Education entries'

    def __str__(self):
        return f"{self.get_level_display()} — {self.institution}"
