from .models import Product

class ProductService:
    @staticmethod
    def get_list(id):
        return Product.objects.filter(category=id)