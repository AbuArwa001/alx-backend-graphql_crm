import graphene
from .models import Product  # Make sure Product model is imported
from graphene_django.types import DjangoObjectType

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "stock")

class UpdateLowStockProducts(graphene.Mutation):
    class Arguments:
        pass

    updated_products = graphene.List(ProductType)
    message = graphene.String()

    def mutate(self, info):
        low_stock_products = Product.objects.filter(stock__lt=10)
        updated = []

        for product in low_stock_products:
            product.stock += 10
            product.save()
            updated.append(product)

        return UpdateLowStockProducts(
            updated_products=updated,
            message=f"{len(updated)} product(s) restocked."
        )

class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()
