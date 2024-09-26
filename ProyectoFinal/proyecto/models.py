from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} ({self.celular})"

class Producto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre
    
class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "PENDIENTE", "Pendiente"
        EN_PROCESO = "EN_PROCESO", "En proceso"
        COMPLETADO = "COMPLETADO", "Completado"

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)

    def __str__(self) -> str:
        return f"Pedido de {self.producto.nombre} para {self.cliente.nombre}"