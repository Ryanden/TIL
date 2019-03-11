## Django RestFrameWork

### Authentication

- User Authentication

  >접속을 희망하는 아이디와 비밀번호를 확인하여 그 유저에게 특정 토큰을 발급해주고, 토큰을 통해 현재 어떤 유저정보와 권한을 부여한다.

  ```python
  class AuthToken(APIView):
      def post(self, request):
          # 전달받은 데이터에서 username, password추출
          username = request.data.get('username')
          password = request.data.get('password')
  
          # authenticate실행
          user = authenticate(username=username, password=password)
  
          # authenticate가 성공한 경우
          if user:
              # Token을 가져오거나 없으면 생성
              token, __ = Token.objects.get_or_create(user=user)
              # Response에 돌려줄 데이터
              data = {
                  'token': token.key,
              }
              return Response(data)
          # authenticate에 실패한 경우
          raise AuthenticationFailed('인증정보가 올바르지 않습니다')
  
  ```

  

  