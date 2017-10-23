"""URLs module for routing with API app."""
from django.conf.urls import url, include
from rest_framework import routers
from apps.api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tenants', views.TenantViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'facets', views.FacetViewSet)
router.register(r'properties', views.PropertyViewSet)
router.register(r'document_versions', views.DocumentVersionViewSet)
router.register(r'depictions', views.DepictionViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
