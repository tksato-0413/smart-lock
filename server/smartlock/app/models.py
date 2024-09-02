from django.db import models
from django.contrib.auth.models import User

class Key(models.Model):
    # 鍵の名前やその他の属性
    name = models.CharField(max_length=100)
    # 鍵の状態（例: 有効, 無効）
    status = models.BooleanField(default=True)
    # 鍵に関連するユーザー
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='keys')

    def __str__(self):
        return self.name
