## Django RESTFARMEWORK

### Method(Get, Post, Patch, Delete)

- Get

  > Get을 사용하는 다양한 방법이 있다. 가장 쉽게 만드는 방법은 ListAPIView를 사용한다.

  ```python
  # class를 사용하여 User 리스트 전체를 가져온다.
  class UserList(generics.ListAPIView):
      queryset = User.objects.all()
      serializer_class = UserSerializer
  
  # 이번엔 전체중에서 특정 유저만 가지고 오는 예제이다.
  # permission_classes를 사용하면 식별가능한(로그인하고있는) 유저의 정보만 가져온다.
  # RetrieveUpdateDestroyApiView를 사용하면 클래스 하나로 조회, 수정, 삭제가 한번에 가능하다.
  class UserDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = User.objects.all()
      serializer_class = UserSerializer
      permission_classes = (
          permissions.IsAuthenticatedOrReadOnly,
      )
  
      def get(self, request, *args, **kwargs):
          return self.retrieve(request, *args, **kwargs)
  
      def patch(self, request, *args, **kwargs):
          return self.partial_update(request, *args, **kwargs)
  
      def destroy(self, request, *args, **kwargs):
          instance = self.get_object()
          self.perform_destroy(instance)
          return Response(status=status.HTTP_204_NO_CONTENT)
  ```

- Post

  > Post의 경우엔 조금 특별한 방법을 사용한다.

  ```python
  # APIView 안에 있는 get, post를 오버라이딩(재정의)하여 사용한다.
  class UserCreate(APIView):
      queryset = User.objects.all()
      serializer_class = UserSerializer
  
      def get(self, request):
          serializer = UserSerializer(User.objects.all(), many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)
  
      def post(self, request):
          serializer = UserSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  ```

