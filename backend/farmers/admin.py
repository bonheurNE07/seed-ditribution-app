from django.contrib import admin
from .models import Farmer, Village, Cell, Species, SeedDistribution

admin.site.register(Farmer)
admin.site.register(Village)
admin.site.register(Cell)

admin.site.register(Species)
admin.site.register(SeedDistribution)
