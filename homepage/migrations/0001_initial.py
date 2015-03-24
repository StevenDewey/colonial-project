# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=75, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('phone', models.TextField(max_length=40)),
                ('security_question', models.TextField(max_length=200)),
                ('security_answer', models.TextField(max_length=200)),
                ('requires_reset', models.BooleanField(default=False)),
                ('organization_name', models.TextField(blank=True, max_length=200, null=True)),
                ('organization_type', models.TextField(blank=True, max_length=40, null=True)),
                ('date_appointed_agent', models.DateField(blank=True, null=True)),
                ('relationship', models.TextField(blank=True, max_length=200, null=True)),
                ('emergency_contact', models.TextField(blank=True, max_length=200, null=True)),
                ('emergency_phone', models.TextField(blank=True, max_length=200, null=True)),
                ('emergency_relationship', models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('street1', models.TextField(max_length=200)),
                ('street2', models.TextField(blank=True, max_length=200, null=True)),
                ('city', models.TextField(max_length=100)),
                ('state', models.TextField(max_length=20)),
                ('zip_code', models.TextField(max_length=20)),
                ('country', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'addresses',
                'ordering': ['state', 'city', 'zip_code', 'street1', 'street2'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('place_number', models.PositiveIntegerField()),
                ('coordinator', models.ForeignKey(related_name='coordinates', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartLineItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('quantity', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('description', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfigurationParameters',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('sales_tax_rate', models.DecimalField(decimal_places=4, max_digits=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DamageFee',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('waived', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('map_file_name', models.TextField(max_length=200)),
                ('venue_name', models.TextField(max_length=200, null=True)),
                ('address', models.ForeignKey(related_name='+', null=True, to='homepage.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LateFee',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('waived', models.BooleanField(default=False)),
                ('days_late', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('order_date', models.DateTimeField()),
                ('phone', models.TextField()),
                ('date_packed', models.DateTimeField()),
                ('date_paid', models.DateTimeField(null=True)),
                ('date_shipped', models.DateTimeField(null=True)),
                ('tracking_number', models.TextField(max_length=50, null=True)),
                ('customer', models.ForeignKey(related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('handled_by', models.ForeignKey(related_name='handledby_set', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('packed_by', models.ForeignKey(related_name='packedby_set', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('payment_processed_by', models.ForeignKey(related_name='paymentprocessedby_set', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('shipped_by', models.ForeignKey(related_name='shippedby_set', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('ships_to', models.ForeignKey(related_name='+', to='homepage.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParticipantRole',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('type', models.TextField(max_length=40)),
                ('area', models.ForeignKey(to='homepage.Area')),
                ('participant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date_taken', models.DateTimeField()),
                ('place_taken', models.TextField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('manufacturer', models.TextField(max_length=80)),
                ('average_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sku', models.TextField(max_length=20)),
                ('order_form_name', models.TextField(max_length=200, null=True)),
                ('production_time', models.TextField(max_length=200, null=True)),
                ('category', models.ForeignKey(related_name='+', to='homepage.Category')),
                ('photo', models.OneToOneField(null=True, to='homepage.Photograph')),
                ('vendor', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RentalItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_out', models.DateTimeField(auto_now_add=True)),
                ('date_in', models.DateTimeField()),
                ('date_due', models.DateTimeField()),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=3)),
                ('order', models.ForeignKey(to='homepage.Order')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(to='homepage.Order')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StockedProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('quantity_on_hand', models.IntegerField(null=True)),
                ('shelf_location', models.TextField(max_length=40, null=True)),
                ('order_file', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SerializedProduct',
            fields=[
                ('stockedproduct_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, primary_key=True, to='homepage.StockedProduct')),
                ('serial_number', models.TextField(max_length=100, unique=True, null=True)),
                ('type', models.TextField(max_length=100)),
                ('date_acquired', models.DateField(auto_now_add=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('for_sale', models.BooleanField(default=True)),
                ('condition_new', models.BooleanField(default=True)),
                ('notes', models.TextField()),
                ('size', models.TextField(max_length=40, null=True)),
                ('size_modifier', models.TextField(max_length=40, null=True)),
                ('gender', models.TextField(max_length=40, null=True)),
                ('color', models.TextField(max_length=40, null=True)),
                ('pattern', models.TextField(max_length=40, null=True)),
                ('start_year', models.PositiveIntegerField(null=True)),
                ('end_year', models.PositiveIntegerField(null=True)),
                ('note', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('homepage.stockedproduct',),
        ),
        migrations.CreateModel(
            name='RentalProduct',
            fields=[
                ('serializedproduct_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, primary_key=True, to='homepage.SerializedProduct')),
                ('times_rented', models.IntegerField()),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('replacement_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('homepage.serializedproduct',),
        ),
        migrations.AddField(
            model_name='stockedproduct',
            name='photo',
            field=models.ForeignKey(to='homepage.Photograph', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stockedproduct',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, related_name='polymorphic_homepage.stockedproduct_set', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stockedproduct',
            name='product_specification',
            field=models.ForeignKey(related_name='+', null=True, to='homepage.ProductSpecification'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serializedproduct',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='saleitem',
            name='product',
            field=models.ForeignKey(related_name='+', to='homepage.StockedProduct'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rentalitem',
            name='rental_product',
            field=models.ForeignKey(related_name='+', to='homepage.RentalProduct'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='latefee',
            name='order',
            field=models.ForeignKey(to='homepage.Order'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='latefee',
            name='rental_item',
            field=models.ForeignKey(related_name='+', to='homepage.RentalItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='damagefee',
            name='order',
            field=models.ForeignKey(to='homepage.Order'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='damagefee',
            name='rental_item',
            field=models.ForeignKey(related_name='+', to='homepage.RentalItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartlineitem',
            name='stocked_product',
            field=models.ForeignKey(to='homepage.StockedProduct'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartlineitem',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='event',
            field=models.ForeignKey(to='homepage.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='participants',
            field=models.ManyToManyField(through='homepage.ParticipantRole', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='photo',
            field=models.ForeignKey(to='homepage.Photograph', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='supervisor',
            field=models.ForeignKey(related_name='supervises', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ForeignKey(related_name='+', null=True, to='homepage.Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_name='user_set', related_query_name='user', to='auth.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ForeignKey(related_name='+', null=True, blank=True, to='homepage.Photograph'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_name='user_set', related_query_name='user', to='auth.Permission'),
            preserve_default=True,
        ),
    ]
