from django.db import models

class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    post_image = models.FileField(verbose_name="Resim Ekle", blank=True, null=True)
    content = models.CharField(max_length=10000, null=True, blank=True, verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma tarihi")

    def __str__(self):
        return self.content
