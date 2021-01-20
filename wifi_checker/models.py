from django.db import models


class Wifi(models.Model):
    instlCtprvnNm = models.CharField(max_length=20)    # 설치시도명
    instlSignguNm = models.CharField(max_length=20)    # 설치시군구
    instlNm = models.CharField(max_length=200)         # 설치장소명
    instlLcDesc = models.CharField(max_length=200)     # 설치장소상세
    svcProvdNm = models.CharField(max_length=20)       # 서비스제공사명
    latitude = models.CharField(max_length=20)         # 위도
    longitude = models.CharField(max_length=20)        # 경도
