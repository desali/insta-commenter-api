from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from api.models import Proxy, UserAgent, Comment, Account, AccountStatistics, Influencer
from api.serializers import ProxyListSerializer, ProxyCreateSerializer, ProxyDetailSerializer, UserAgentListSerializer, \
    UserAgentCreateSerializer, UserAgentDetailSerializer, CommentListSerializer, CommentCreateSerializer, \
    CommentDetailSerializer, AccountListSerializer, AccountCreateSerializer, AccountDetailSerializer, \
    InfluencerListSerializer, InfluencerCreateSerializer, InfluencerDetailSerializer, AccountUpdateSerializer, \
    InfluencerUpdateSerializer


class ProxyListView(ListAPIView):
    serializer_class = ProxyListSerializer
    queryset = Proxy.objects.all()


class ProxyCreateView(CreateAPIView):
    serializer_class = ProxyCreateSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        proxy = self.perform_create(serializer)
        return Response(ProxyDetailSerializer(proxy).data)


class ProxyDetailPKView(RetrieveAPIView):
    serializer_class = ProxyDetailSerializer
    queryset = Proxy.objects.all()


class ProxyDetailView(ListAPIView):
    serializer_class = ProxyDetailSerializer

    def get_queryset(self):
        host = self.request.query_params["host"]
        port = self.request.query_params["port"]

        return Proxy.objects.filter(host=host, port=port).all()


class ProxyDestroyView(DestroyAPIView):
    queryset = Proxy.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"status": "deleted"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        Account.objects.filter(proxy=instance).update(proxy=None)
        instance.delete()


class UserAgentListView(ListAPIView):
    serializer_class = UserAgentListSerializer
    queryset = UserAgent.objects.all()


class UserAgentCreateView(CreateAPIView):
    serializer_class = UserAgentCreateSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_agent = self.perform_create(serializer)
        return Response(UserAgentDetailSerializer(user_agent).data)


class UserAgentDetailPKView(RetrieveAPIView):
    serializer_class = UserAgentDetailSerializer
    queryset = UserAgent.objects.all()


class UserAgentDetailView(ListAPIView):
    serializer_class = UserAgentDetailSerializer

    def get_queryset(self):
        name = self.request.query_params["name"]

        return UserAgent.objects.filter(name=name).all()


class UserAgentDestroyView(DestroyAPIView):
    queryset = UserAgent.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"status": "deleted"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        Account.objects.filter(useragent=instance).update(useragent=None)
        instance.delete()


class CommentListView(ListAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()


class CommentCreateView(CreateAPIView):
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment = self.perform_create(serializer)
        return Response(CommentDetailSerializer(comment).data)


class CommentDetailPKView(RetrieveAPIView):
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()


class CommentDetailView(ListAPIView):
    serializer_class = CommentDetailSerializer

    def get_queryset(self):
        text = self.request.query_params["text"]

        return Comment.objects.filter(text=text).all()


class CommentDestroyView(DestroyAPIView):
    queryset = Comment.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"status": "deleted"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()


class AccountListView(ListAPIView):
    serializer_class = AccountListSerializer
    queryset = Account.objects.all()


class AccountCreateView(CreateAPIView):
    serializer_class = AccountCreateSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account = self.perform_create(serializer)
        account_statistics = AccountStatistics.objects.create(account=account)
        return Response(AccountDetailSerializer(account).data)


class AccountEditView(UpdateAPIView):
    serializer_class = AccountUpdateSerializer
    queryset = Account.objects.all()

    def perform_update(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        account = self.perform_update(serializer)
        return Response(AccountDetailSerializer(account).data)


class AccountDetailPKView(RetrieveAPIView):
    serializer_class = AccountDetailSerializer
    queryset = Account.objects.all()


class AccountDetailView(ListAPIView):
    serializer_class = AccountDetailSerializer

    def get_queryset(self):
        username = self.request.query_params["username"]

        return Account.objects.filter(username=username).all()


class AccountDestroyView(DestroyAPIView):
    queryset = Account.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"status": "deleted"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        Influencer.objects.filter(account=instance).update(account=None)
        instance.activity.delete()
        instance.statistics.delete()
        instance.delete()


class InfluencerListView(ListAPIView):
    serializer_class = InfluencerListSerializer
    queryset = Influencer.objects.all()


class InfluencerCreateView(CreateAPIView):
    serializer_class = InfluencerCreateSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        influencer = self.perform_create(serializer)
        return Response(InfluencerDetailSerializer(influencer).data)


class InfluencerEditView(UpdateAPIView):
    serializer_class = InfluencerUpdateSerializer
    queryset = Influencer.objects.all()

    def perform_update(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        influencer = self.perform_update(serializer)
        return Response(InfluencerDetailSerializer(influencer).data)


class InfluencerDetailPKView(RetrieveAPIView):
    serializer_class = InfluencerDetailSerializer
    queryset = Influencer.objects.all()


class InfluencerDetailView(ListAPIView):
    serializer_class = InfluencerDetailSerializer

    def get_queryset(self):
        username = self.request.query_params["username"]

        return Influencer.objects.filter(username=username).all()


class InfluencerDestroyView(DestroyAPIView):
    queryset = Influencer.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"status": "deleted"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()
