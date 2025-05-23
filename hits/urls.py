from django.urls import path
from .views import HitListCreateView, HitDetailView

urlpatterns = [
    path("hits", HitListCreateView.as_view(), name="hit-list-create"),
    path("hits/<slug:title_url>", HitDetailView.as_view(), name="hit-detail"),
]
