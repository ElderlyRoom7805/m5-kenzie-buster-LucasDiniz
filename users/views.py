from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer


class UserView(APIView):
    def post(self, request: Request) -> Response:
        new_user = UserSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        new_user.save()

        return Response(new_user.data, status.HTTP_201_CREATED)