from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model): # Post는 모델명(대문자로 시작), models.Model은 Post가 모델임을 선언
    # 아래는 Post라는 Class의 속서에 대한 정의
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
                                             # models.ForeingKey : 다른 모델의 값을 가져오도록 정의
    title = models.CharField(max_length=200) # models.CharField : 글자수가 제한된 텍스트 정의
    text = models.TextField()                # models.TextField : 글자수가 제한되지 않은 텍스트 정의
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): # def : 함수 또는 Method를 정의할 때 사용. publish는 Method의 이름
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title