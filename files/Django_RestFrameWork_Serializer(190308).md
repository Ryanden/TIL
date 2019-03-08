## Django RestFrameWork

### Serializer

- UserSerializer

  >User serializer를 사용하는 경우 단순히 목록을 json형태로 받는것 이외에도 다양한 방법이 있다.

  ```python
  class UserSerializer(serializers.ModelSerializer):
      username = serializers.EmailField(
          validators=[UniqueValidator(queryset=User.objects.all())])
      password = serializers.CharField(
          max_length=12, min_length=1, allow_blank=False, write_only=True)
      nickname = serializers.CharField(
          max_length=20, validators=[UniqueValidator(queryset=User.objects.all())])
  
      class Meta:
          model = User
  
          fields = (
              'pk',
              'username',
              'nickname',
              'password',
              'phone_number',
              'img_profile',
              'like_products',
              'carts',
              'recipes',
              'items',
          )
  
  # 유저 정보를 serializer에서 받아서 수정 할 수 있는 방법
      def update(self, instance, validated_data):
  
          if validated_data.get('username'):
              return instance
  
          if validated_data.get('phone_number'):
              instance.phone_number = validated_data.get('phone_number')
  
          if validated_data.get('img_profile'):
              instance.img_profile = validated_data.get('img_profile')
  
          if validated_data.get('nickname'):
              instance.nickname = validated_data.get('nickname')
  
          instance.save()
          return instance
  # 유저 정보를 받아서 db에 저장하는 방식도 가능하다.
      def create(self, validated_data):
          User.objects.create_user(
              username=validated_data['username'],
              password=validated_data['password'],
              nickname=validated_data['nickname'],
              phone_number=validated_data['phone_number'],
          )
  
          return validated_data
  ```

  

  