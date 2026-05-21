from django.db import migrations

# Replace hotlink-protected alkaramstudio.com URLs with working Unsplash fashion images
CLOTHING_IMAGE_REPLACEMENTS = {
    1: 'https://images.unsplash.com/photo-1583394838336-acd977736f90?auto=format&fit=crop&q=80&w=800',
    2: 'https://images.unsplash.com/photo-1571513800374-df1bbe650e56?auto=format&fit=crop&q=80&w=800',
    3: 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&q=80&w=800',
    4: 'https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&q=80&w=800',
    5: 'https://images.unsplash.com/photo-1469334031218-e382a71b716b?auto=format&fit=crop&q=80&w=800',
}

def fix_product_image_urls(apps, schema_editor):
    Product = apps.get_model('api', 'Product')
    for product_id, new_url in CLOTHING_IMAGE_REPLACEMENTS.items():
        try:
            product = Product.objects.get(pk=product_id)
            # Only replace if it's an alkaramstudio.com URL
            image_str = str(product.image)
            if 'alkaramstudio.com' in image_str:
                product.image = new_url
                product.save(update_fields=['image'])
        except Product.DoesNotExist:
            pass


def reverse_fix(apps, schema_editor):
    # Non-destructive reverse: do nothing
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_herobanner'),
    ]

    operations = [
        migrations.RunPython(fix_product_image_urls, reverse_fix),
    ]
