from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Account
from .serializers import AccountSerializer


# Create your views here.
@api_view()
def list_account(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def account_detail(request, pk):
    try:
        account = Account.objects.get(pk=pk)
        serializer = AccountSerializer(account)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return Response({"message": "Account does not exist"}, status=status.HTTP_404_NOT_FOUND)
