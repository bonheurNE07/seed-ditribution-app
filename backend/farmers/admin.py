from django.contrib import admin
from .models import Farmer, Village, Cell, Species, DistributedItem, Distribution

admin.site.register(Farmer)
admin.site.register(Village)
admin.site.register(Cell)

admin.site.register(Species)
admin.site.register(Distribution)
admin.site.register(DistributedItem)
