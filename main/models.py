import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=100) # Nama produk, maksimal 100 karakter
    price = models.IntegerField() # Harga produk dalam bentuk integer (misal Rp)
    description = models.TextField() # Deskripsi produk, bisa panjang
    thumbnail = models.URLField() # URL gambar thumbnail produk
    category = models.CharField(max_length=100) # Kategori produk, contoh: "Baju", "Sepatu"
    is_featured = models.BooleanField(default=False) # Menandai produk favorit/unggulan
    created_at = models.DateTimeField(auto_now_add=True) # Tanggal dan waktu produk ditambahkan (otomatis diisi)
    views = models.IntegerField(default=0) # Jumlah view/product dilihat oleh user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # Tugas 4

    def __str__(self): 
        return f"{self.name} - {self.stock}"

