from .serializers import BidsSerializer, BidsCreateSerializer, BidsHistorySerializer, BidsHistoryCreateSerializer
from rest_framework import generics, viewsets, status, filters
from rest_framework.response import Response
from .models import Bids, BidsHistory
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Q
# Create your views here.

class BidsListView(generics.ListAPIView):
  """
    Returns a list of all Bids.

    Accepts optional query parameters for filtering and search.
    Returns a list of all Bids. or an empty array if no Bids exist.
  """

  permission_classes = [IsAuthenticated]
  # queryset = Bids.objects.all( )
  serializer_class = BidsSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['user__first_name', 'user__last_name', 'user__email', 'quantity', 'price', 'start_time', 'close_time', 'created_at', 'updated_at']

  def get_queryset(self):
    queryset = Bids.objects.filter(
      Q(user = self.request.user)
    )
    return queryset

bids_list = BidsListView.as_view()

class BidsViewSets(viewsets.ModelViewSet):

  permission_classes = [IsAuthenticated]
  # queryset = Bids.objects.all()
  serializer_class = BidsSerializer

  def get_queryset(self):
    queryset = Bids.objects.filter(
      Q(user = self.request.user)
    )
    return queryset

  def get_serializer_class(self):
    if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
      return BidsCreateSerializer
    return BidsSerializer
  
  def retrieve(self, request, pk=None, *args, **kwargs):
    """
      Returns a specific Bid.

      Accepts a required `pk` parameter.
      Returns a specific Bids. or a 404 if it does not exist.
    """
    try:
      bids = self.get_queryset().get(id=pk)
      serializer = self.get_serializer(bids)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Bids.DoesNotExist:
      return Response(
        data={
          "message": "Bid does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except Bids.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple Bids exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def create(self, request):
    """
      Creates a new Bid.

      Accepts a required `user`, `quantity`, `price`, `start_time`, `close_time` parameter.
      Returns the created Bid.
    """
    try:
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response(
        data={
          "error": str(e),
          "message": "Bid not created"
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def update(self, request, pk=None):
    """
      Updates a specific Bid.

      Accepts a required `pk` parameter.
      Returns the updated Bid.
    """
    try:
      bids = self.get_queryset().get(id=pk)
      serializer = self.get_serializer(bids, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Bids.DoesNotExist:
      return Response(
        data={
          "message": "Bid does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except Bids.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple Bids exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
  def partial_update(self, request, pk=None):
    """
      Updates a specific Bid.

      Accepts a required `pk` parameter.
      Returns the updated Bid.
    """
    try:
      bids = Bids.objects.get(id=pk)
      serializer = self.get_serializer(bids, data=request.data, partial=True)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Bids.DoesNotExist:
      return Response(
        data={
          "message": "Bid does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except Bids.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple Bids exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
  def destroy(self, request, pk=None):
    """
      Deletes a specific Bid.

      Accepts a required `pk` parameter.
      Returns the deleted Bid.
    """
    try:
      bids = Bids.objects.get(id=pk)
      serializer = self.get_serializer(bids)
      bids.delete()
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Bids.DoesNotExist:
      return Response(
        data={
          "message": "Bid does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except Bids.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple Bids exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
      
# bids_viewset = BidsViewSets.as_view()

class BidsHistoryListView(generics.ListAPIView):
  """
    Returns a list of all BidsHistory.

    Accepts optional query parameters for filtering and search.
    Returns a list of all BidsHistory. or an empty array if no BidsHistory exist.
  """

  permission_classes = [IsAuthenticated]
  # queryset = BidsHistory.objects.all()
  serializer_class = BidsHistorySerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['user__first_name', 'user__last_name', 'user__email', 'quantity', 'price', 'start_time', 'close_time', 'created_at', 'updated_at']

  def get_queryset(self):
      queryset = BidsHistory.objects.filter(
        Q(user = self.request.user)
      )
      return queryset

  def get_serializer_class(self):
    if self.action == 'create':
      return BidsHistoryCreateSerializer
    return BidsHistorySerializer
  
  def list(self, request, id=None, *args, **kwargs):
    # queryset = self.get_queryset().filter(bid=kwargs['id'])
    queryset = self.get_queryset().filter(bid=id)
    serializer = BidsHistorySerializer(queryset, many=True)
    return Response(serializer.data)
    
bids_history = BidsHistoryListView.as_view()


class BidsHistoryViewSets(viewsets.ModelViewSet):

  permission_classes = [IsAuthenticated]
  # queryset = BidsHistory.objects.all()
  serializer_class = BidsHistorySerializer

  def get_queryset(self):
      queryset = Bids.objects.filter(
        Q(user = self.request.user) |
        Q(user__role = 'admin')
      )
      return queryset
  
  def get_serializer_class(self):
    if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
      return BidsHistoryCreateSerializer
    return BidsHistorySerializer
  
  def retrieve(self, request, pk=None, *args, **kwargs):
    """
      Returns a specific BidHistory.

      Accepts a required `pk` parameter.
      Returns a specific BidsHistory. or a 404 if it does not exist.
    """
    try:
      bids_history = BidsHistory.objects.get(id=pk)
      serializer = self.get_serializer(bids_history)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except BidsHistory.DoesNotExist:
      return Response(
        data={
          "message": "BidHistory does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except BidsHistory.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple BidsHistory exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def create(self, request):
    """
      Creates a new BidHistory.

      Accepts a required `user`, `quantity`, `price`, `start_time`, `close_time` parameter.
      Returns the created BidHistory.
    """
    try:
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response(
        data={
          "error": str(e),
          "message": "Bid history not created"
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def list(self, request, *args, **kwargs):
    """
      Returns a list of all BidsHistory.

      Accepts optional query parameters for filtering and search.
      Returns a list of all BidsHistory. or an empty array if no BidsHistory exist.
    """
    try:
      queryset = self.get_queryset()
      serializer = BidsHistorySerializer(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdminBidsViewSets(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated, IsAdminUser]
  serializer_class = BidsSerializer

  def get_queryset(self):
    queryset = Bids.objects.all()
    return queryset
  
  def get_serializer_class(self):
    if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
      return BidsCreateSerializer
    return BidsSerializer
  
  def retrieve(self, request, pk=None, *args, **kwargs):
    """
      Returns a specific Bid.

      Accepts a required `pk` parameter.
      Returns a specific Bids. or a 404 if it does not exist.
    """
    try:
      bids = self.get_queryset().get(id=pk)
      serializer = self.get_serializer(bids)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Bids.DoesNotExist:
      return Response(
        data={
          "message": "Bid does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except Bids.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple Bids exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def create(self, request):
    """
      Creates a new Bid.

      Accepts a required `user`, `quantity`, `price`, `start_time`, `close_time` parameter.
      Returns the created Bid.
    """
    try:
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response(
        data={
          "error": str(e),
          "message": "Bid not created"
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def update(self, request, pk=None):
    """
      Updates a specific Bid.

      Accepts a required `pk` parameter.
      Returns the updated Bid.
    """
    try:
      bids = self.get_queryset().get(id=pk)
      serializer = self.get_serializer(bids, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Bids.DoesNotExist:
      return Response(
        data={
          "message": "Bid does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except Bids.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple Bids exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  def partial_update(self, request, pk=None):
    """
      Updates a specific Bid.

      Accepts a required `pk` parameter.
      Returns the updated Bid.
    """
    try:
      bids = self.get_queryset().get(id=pk)
      serializer = self.get_serializer(bids, data=request.data, partial=True)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Bids.DoesNotExist:
      return Response(
        data={
          "message": "Bid does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except Bids.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple Bids exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def destroy(self, request, pk=None):
    """
      Deletes a specific Bid.

      Accepts a required `pk` parameter.
      Returns the deleted Bid.
    """
    try:
      bids = self.get_queryset().get(id=pk)
      serializer = self.get_serializer(bids)
      bids.delete()
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Bids.DoesNotExist:
      return Response(
        data={
          "message": "Bid does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except Bids.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple Bids exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

class AdminBidsHistoryViewSets(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated, IsAdminUser]
  serializer_class = BidsHistorySerializer

  def get_queryset(self):
    queryset = BidsHistory.objects.all(
    )
    return queryset
  
  def get_serializer_class(self):
    if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
      return BidsHistoryCreateSerializer
    return BidsHistorySerializer
  
  def retrieve(self, request, pk=None, *args, **kwargs):
    """
      Returns a specific BidHistory.

      Accepts a required `pk` parameter.
      Returns a specific BidsHistory. or a 404 if it does not exist.
    """
    try:
      bids_history = self.get_queryset().get(id=pk)
      serializer = self.get_serializer(bids_history)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except BidsHistory.DoesNotExist:
      return Response(
        data={
          "message": "BidHistory does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except BidsHistory.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple BidsHistory exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def create(self, request):
    """
      Creates a new BidHistory.

      Accepts a required `user`, `quantity`, `price`, `start_time`, `close_time` parameter.
      Returns the created BidHistory.
    """
    try:
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response(
        data={
          "error": str(e),
          "message": "Bid history not created"
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def list(self, request, *args, **kwargs):
    """
      Returns a list of all BidsHistory.

      Accepts optional query parameters for filtering and search.
      Returns a list of all BidsHistory. or an empty array if no BidsHistory exist.
    """
    try:
      queryset = self.get_queryset()
      serializer = BidsHistorySerializer(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def update(self, request, pk=None):
    """
      Updates a specific BidHistory.

      Accepts a required `pk` parameter.
      Returns the updated BidHistory.
    """
    try:
      bids_history = self.get_queryset().get(id=pk)
      serializer = self.get_serializer(bids_history, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    except BidsHistory.DoesNotExist:
      return Response(
        data={
          "message": "BidHistory does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except BidsHistory.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple BidsHistory exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  def partial_update(self, request, pk=None):
    """
      Updates a specific BidHistory.

      Accepts a required `pk` parameter.
      Returns the updated BidHistory.
    """
    try:
      bids_history = self.get_queryset().get(id=pk)
      serializer = self.get_serializer(bids_history, data=request.data, partial=True)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    except BidsHistory.DoesNotExist:
      return Response(
        data={
          "message": "BidHistory does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except BidsHistory.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple BidsHistory exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def destroy(self, request, pk=None):
    """
      Deletes a specific BidHistory.

      Accepts a required `pk` parameter.
      Returns the deleted BidHistory.
    """
    try:
      bids_history = self.get_queryset().get(id=pk)
      serializer = self.get_serializer(bids_history)
      bids_history.delete()
      return Response(serializer.data, status=status.HTTP_200_OK)
    except BidsHistory.DoesNotExist:
      return Response(
        data={
          "message": "BidHistory does not exist"
        },
        status=status.HTTP_404_NOT_FOUND)
    except BidsHistory.MultipleObjectsReturned:
      return Response(
        data={
          "message": "Multiple BidsHistory exist"
        },
        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(
        data={
          "message": str(e)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class AdminBidHistoryListView(generics.ListAPIView):
  """
    Returns a list of all hostories for a single bid.

    Accepts optional query parameters for filtering and search.
    Returns a list of all BidsHistory. or an empty array if no BidsHistory exist.
  """

  permission_classes = [IsAuthenticated, IsAdminUser]
  # queryset = BidsHistory.objects.all()
  serializer_class = BidsHistorySerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['user__first_name', 'user__last_name', 'user__email', 'quantity', 'price', 'start_time', 'close_time', 'created_at', 'updated_at']

  def get_queryset(self):
      queryset = BidsHistory.objects.all()
      return queryset

  def get_serializer_class(self):
    if self.action == 'create':
      return BidsHistoryCreateSerializer
    return BidsHistorySerializer
  
  def list(self, request, id=None, *args, **kwargs):
    # queryset = self.get_queryset().filter(bid=kwargs['id'])
    queryset = self.get_queryset().filter(bid=id)
    serializer = BidsHistorySerializer(queryset, many=True)
    return Response(serializer.data)
  
admin_bids_history = AdminBidHistoryListView.as_view()
