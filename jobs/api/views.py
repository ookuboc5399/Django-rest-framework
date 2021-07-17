from rest_framework import generics
from jobs.models import JobOffer
from jobs.api.serislizers import JobOfferSerializer


class ListView(generics.ListCreateAPIView):
    queryset = JobOffer.objects