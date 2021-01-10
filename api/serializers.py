from rest_framework import serializers

from api.models import Proxy, UserAgent, Comment, Account, AccountStatistics, Influencer


class ProxyListSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    status = serializers.CharField(source='get_status_display')
    accs_count = serializers.SerializerMethodField('get_accs')

    class Meta:
        model = Proxy
        fields = ('id', 'host', 'port', 'type', 'username', 'password', 'status', 'accs_count')

    def get_accs(self, instance):
        return instance.accounts.count()


class ProxyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proxy
        fields = ('host', 'port', 'type', 'username', 'password')


class ProxyDetailSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    status = serializers.CharField(source='get_status_display')
    accs_count = serializers.SerializerMethodField('get_accs')

    class Meta:
        model = Proxy
        fields = ('id', 'host', 'port', 'type', 'username', 'password', 'status', 'accs_count')

    def get_accs(self, instance):
        return instance.accounts.count()


class UserAgentListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    accs_count = serializers.SerializerMethodField('get_accs')

    class Meta:
        model = UserAgent
        fields = ('id', 'name', 'status', 'accs_count')

    def get_accs(self, instance):
        return instance.accounts.count()


class UserAgentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAgent
        fields = ('name', )


class UserAgentDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    accs_count = serializers.SerializerMethodField('get_accs')

    class Meta:
        model = UserAgent
        fields = ('id', 'name', 'status', 'accs_count')

    def get_accs(self, instance):
        return instance.accounts.count()


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'used_times')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', )


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'used_times')


class AccountStatisticsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatistics
        fields = ('login_count', 'comments_count', 'monitor_count')


class AccountListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    useragent = UserAgentDetailSerializer()
    proxy = ProxyDetailSerializer()
    statistics = AccountStatisticsDetailSerializer()
    infs_count = serializers.SerializerMethodField('get_infs')

    class Meta:
        model = Account
        fields = ('id', 'username', 'password', 'new_mail_login', 'new_mail_pass', 'old_mail_login', 'old_mail_pass',
                  'phone', 'status', 'useragent', 'proxy', 'statistics', 'infs_count')

    def get_infs(self, instance):
        return instance.influencers.count()


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'password', 'new_mail_login', 'new_mail_pass', 'old_mail_login', 'old_mail_pass',
                  'phone')


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('useragent', 'proxy')


class AccountDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    useragent = UserAgentDetailSerializer()
    proxy = ProxyDetailSerializer()
    statistics = AccountStatisticsDetailSerializer()
    infs_count = serializers.SerializerMethodField('get_infs')

    class Meta:
        model = Account
        fields = ('id', 'username', 'password', 'new_mail_login', 'new_mail_pass', 'old_mail_login', 'old_mail_pass',
                  'phone', 'status', 'useragent', 'proxy', 'statistics', 'infs_count')

    def get_infs(self, instance):
        return instance.influencers.count()


class InfluencerListSerializer(serializers.ModelSerializer):
    account = serializers.SlugRelatedField(slug_field='username', queryset=Account.objects.all())

    class Meta:
        model = Influencer
        fields = ('id', 'username', 'account', 'last_post_days', 'last_post_id')


class InfluencerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = ('username', )


class InfluencerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = ('account', 'last_post_id', 'last_post_days')


class InfluencerDetailSerializer(serializers.ModelSerializer):
    account = serializers.SlugRelatedField(slug_field='username', queryset=Account.objects.all())

    class Meta:
        model = Influencer
        fields = ('id', 'username', 'account', 'last_post_days', 'last_post_id')
