from django.db import models

class Book(models.Model):
    
    REVIEW_STAR = (
        ("⭐","⭐"),
        ("⭐⭐","⭐⭐"),
        ("⭐⭐⭐","⭐⭐⭐"),
        ("⭐⭐⭐⭐","⭐⭐⭐⭐"),
        ("⭐⭐⭐⭐⭐","⭐⭐⭐⭐⭐"),
    )
    

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.CharField(max_length=5, choices=REVIEW_STAR)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Book"
    