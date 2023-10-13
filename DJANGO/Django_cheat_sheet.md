## Django ORM Cheatsheet

#### Models and Fields:
- **Model Definition:**
  ```python
  from django.db import models

  class YourModel(models.Model):
      field1 = models.CharField(max_length=100)
      field2 = models.IntegerField()
      # ... Other fields
  ```

- **Field Types:**
  - `CharField`, `TextField`, `IntegerField`, `FloatField`, `BooleanField`, `DateTimeField`, `DateField`, `ForeignKey`, `ManyToManyField`, etc.

#### Database Operations:
- **Create (Insert):**
  ```python
  obj = YourModel(field1='value', field2=42)
  obj.save()
  ```

- **Read (Querysets):**
  ```python
  # Get all records
  all_records = YourModel.objects.all()

  # Filter records
  filtered_records = YourModel.objects.filter(field1='value')

  # Get a single record
  record = YourModel.objects.get(id=1)
  ```

- **Update:**
  ```python
  record = YourModel.objects.get(id=1)
  record.field1 = 'new value'
  record.save()
  ```

- **Delete:**
  ```python
  record = YourModel.objects.get(id=1)
  record.delete()
  ```

- **Aggregation:**
  ```python
  from django.db.models import Count, Sum, Avg

  # Count records
  count = YourModel.objects.count()

  # Sum of a field
  total = YourModel.objects.aggregate(Sum('field2'))

  # Average of a field
  avg_value = YourModel.objects.aggregate(Avg('field2'))
  ```

#### Relationships:
- **One-to-Many Relationship:**
  ```python
  class ParentModel(models.Model):
      # Fields

  class ChildModel(models.Model):
      parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
      # Other fields
  ```

- **Many-to-Many Relationship:**
  ```python
  class Tag(models.Model):
      name = models.CharField(max_length=50)

  class Article(models.Model):
      tags = models.ManyToManyField(Tag)
      # Other fields
  ```

- **One-to-One Relationship:**
  ```python
  class UserProfile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      # Other fields
  ```

#### Queryset Methods:
- **Filtering:**
  ```python
  YourModel.objects.filter(field1='value')
  ```

- **Exclude:**
  ```python
  YourModel.objects.exclude(field1='value')
  ```

- **Ordering:**
  ```python
  YourModel.objects.order_by('field1')  # Ascending
  YourModel.objects.order_by('-field1')  # Descending
  ```

- **Limit and Offset:**
  ```python
  YourModel.objects.all()[:10]  # Limit
  YourModel.objects.all()[10:20]  # Offset
  ```

- **Chaining:**
  ```python
  YourModel.objects.filter(field1='value').exclude(field2=42)
  ```

---
## Django ORM Comprehensive Cheatsheet

#### Models and Fields:
- **Model Definition:**
  ```python
  from django.db import models

  class YourModel(models.Model):
      field1 = models.CharField(max_length=100)
      field2 = models.IntegerField()
      # ... Other fields
  ```

- **Field Types:**
  - `AutoField`, `BigAutoField`, `BigIntegerField`, `BinaryField`, `BooleanField`, `CharField`, `DateField`, `DateTimeField`, `DecimalField`, `DurationField`, `EmailField`, `FileField`, `FloatField`, `ImageField`, `IntegerField`, `ManyToManyField`, `OneToOneField`, `PositiveIntegerField`, `SlugField`, `TextField`, `TimeField`, `UUIDField`, and more.

#### Database Operations:
- **Create (Insert):**
  ```python
  obj = YourModel(field1='value', field2=42)
  obj.save()
  ```

- **Bulk Create:**
  ```python
  YourModel.objects.bulk_create([YourModel(field1='value1'), YourModel(field1='value2')])
  ```

- **Read (Querysets):**
  ```python
  # Get all records
  all_records = YourModel.objects.all()

  # Filter records
  filtered_records = YourModel.objects.filter(field1='value')

  # Get a single record
  record = YourModel.objects.get(id=1)
  ```

- **Update:**
  ```python
  record = YourModel.objects.get(id=1)
  record.field1 = 'new value'
  record.save()
  ```

- **Bulk Update:**
  ```python
  YourModel.objects.filter(field1='old_value').update(field1='new_value')
  ```

- **Delete:**
  ```python
  record = YourModel.objects.get(id=1)
  record.delete()
  ```

- **Bulk Delete:**
  ```python
  YourModel.objects.filter(field1='value').delete()
  ```

- **Transactions:**
  ```python
  from django.db import transaction

  with transaction.atomic():
      # Your database operations within a transaction
  ```

- **Raw SQL Queries:**
  ```python
  from django.db import connection

  cursor = connection.cursor()
  cursor.execute("SELECT * FROM yourapp_yourmodel")
  ```

#### Relationships:
- **One-to-Many Relationship:**
  ```python
  class ParentModel(models.Model):
      # Fields

  class ChildModel(models.Model):
      parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
      # Other fields
  ```

- **Many-to-Many Relationship:**
  ```python
  class Tag(models.Model):
      name = models.CharField(max_length=50)

  class Article(models.Model):
      tags = models.ManyToManyField(Tag)
      # Other fields
  ```

- **One-to-One Relationship:**
  ```python
  class UserProfile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      # Other fields
  ```

#### Queryset Methods:
- **Filtering:**
  ```python
  YourModel.objects.filter(field1='value')
  ```

- **Exclude:**
  ```python
  YourModel.objects.exclude(field1='value')
  ```

- **OR Queries:**
  ```python
  from django.db.models import Q

  YourModel.objects.filter(Q(field1='value1') | Q(field1='value2'))
  ```

- **Ordering:**
  ```python
  YourModel.objects.order_by('field1')  # Ascending
  YourModel.objects.order_by('-field1')  # Descending
  ```

- **Limit and Offset:**
  ```python
  YourModel.objects.all()[:10]  # Limit
  YourModel.objects.all()[10:20]  # Offset
  ```

- **Chaining:**
  ```python
  YourModel.objects.filter(field1='value').exclude(field2=42)
  ```

#### Aggregation and Annotation:
- **Count:**
  ```python
  YourModel.objects.count()
  ```

- **Sum, Avg, Min, Max:**
  ```python
  from django.db.models import Sum, Avg, Min, Max

  YourModel.objects.aggregate(Sum('field2'))
  YourModel.objects.aggregate(Avg('field2'))
  ```

- **Group By:**
  ```python
  from django.db.models import Count

  YourModel.objects.values('field1').annotate(count=Count('id'))
  ```

#### F Expressions:
- **Using F to Update:**
  ```python
  from django.db.models import F

  YourModel.objects.filter(id=1).update(field2=F('field2') + 1)
  ```

- **Using F for Comparison:**
  ```python
  YourModel.objects.filter(field2__gt=F('field1'))
  ```

#### Transactions:
- **Atomic Transactions:**
  ```python
  from django.db import transaction

  with transaction.atomic():
      # Your database operations within a transaction
  ```

#### Raw SQL Queries:
- **Executing Raw SQL:**
  ```python
  from django.db import connection

  cursor = connection.cursor()
  cursor.execute("SELECT * FROM yourapp_yourmodel")
  ```

- **Parameterized Queries:**
  ```python
  cursor.execute("SELECT * FROM yourapp_yourmodel WHERE field=%s", [value])
  ```
