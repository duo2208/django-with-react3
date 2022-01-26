from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

""" generic """
# class PublicPostListAPIView(generics.ListAPIView):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer

""" APIView """
# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serialzer = PostSerializer(qs, many=True)
#         return Response(serialzer.data)

# public_post_list = PublicPostListAPIView.as_view()

""" 함수 ver """
# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serialzer = PostSerializer(qs, many=True)
#     return Response(serialzer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True) # 알아서 필요한 serializer를 찾아줌
        # serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_obeject()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

        
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

# def post_list(request):
    # request.method => 2개 분기

# def post_detail(request, pk):
    # request.method => 3개 분기
