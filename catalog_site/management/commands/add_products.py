from django.core.management import BaseCommand

from catalog_site.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        cat1, _ = Category.objects.get_or_create(name='Cat 1')
        cat2, _ = Category.objects.get_or_create(name='Cat 2')

        products = [
            {'name': 'Prod 3', 'desc': 'prod num 3', 'price': 22, 'category': cat1},
            {'name': 'Prod 4', 'desc': 'prod num 4', 'price': 122, 'category': cat2},
            {'name': 'Prod 5', 'desc': 'prod num 5', 'price': 252, 'category': cat2},
            {'name': 'Prod 6', 'desc': 'prod num 6', 'price': 622, 'category': cat1},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product}'))
            else:
                self.stdout.write(self.style.WARNING(f'product already exists: {product}'))