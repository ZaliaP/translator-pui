from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, default='user')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

class Translation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_text = models.TextField()
    translated_text = models.TextField()
    source_lang = models.CharField(max_length=5, default='auto')
    target_lang = models.CharField(max_length=5)
    is_saved = models.BooleanField(default=False)

    class Meta:
        db_table = 'translations'

class FavoriteLang(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language_code = models.CharField(max_length=5)

    class Meta:
        db_table = 'favorite_lang'

class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tag'

class TagTranslation(models.Model):
    translation = models.ForeignKey(Translation, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tag_translations'