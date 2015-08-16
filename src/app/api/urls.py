# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter

from app.api.account.views import AccountViewSet

router = DefaultRouter()

router.register(r'accounts', AccountViewSet)

urlpatterns = router.urls
