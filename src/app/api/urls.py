# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter

from app.api.account.views import AccountViewSet
from app.api.podcast.views import PodcastViewSet

router = DefaultRouter()

router.register(r'accounts', AccountViewSet)
router.register(r'podcasts', PodcastViewSet)

urlpatterns = router.urls
