# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter

from app.api.account.views import AccountViewSet
from app.api.podcast.views import PodcastViewSet, EpisodeViewSet

router = DefaultRouter()

router.register(r'accounts', AccountViewSet)
router.register(r'podcasts', PodcastViewSet)
router.register(r'episodes', EpisodeViewSet)

urlpatterns = router.urls
