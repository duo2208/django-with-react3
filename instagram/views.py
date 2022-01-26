from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

# def post_list(request):
    # request.method => 2개 분기

# def post_detail(request, pk):
    # request.method => 3개 분기
