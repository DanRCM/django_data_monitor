from django.db import models

# Create your models here.
class DashboardModel(models.Model):
    # No necesitamos campos reales para este ejercicio, solo los permisos
    
    class Meta:
        # Aquí definimos permisos personalizados
        permissions = [
            ("index_viewer", "Can show to index view (function-based)"),
        ]