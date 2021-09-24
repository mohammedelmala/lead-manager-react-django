from rest_framework import permissions, viewsets
from lead.models import Lead
from lead.serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [
        permissions.AllowAny
    ]
