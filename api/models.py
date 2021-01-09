from django.db import models
from django.utils import timezone
from softdelete.models import SoftDeleteModel


class Proxy(SoftDeleteModel):
    TYPES = (
        ('HTTP', 'http_https'),
        ('SOCKS', 'socks'),
        ('FTP', 'ftp'),
    )

    STATUSES = (
        ('CREATED', 'created'),
        ('ACTIVE', 'active'),
        ('INACTIVE', 'inactive'),
    )

    host = models.CharField(max_length=16)
    port = models.CharField(max_length=8)
    type = models.CharField(max_length=8, choices=TYPES, default='HTTP')
    username = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=256, choices=STATUSES, default='CREATED')

    class Meta:
        db_table = 'api_proxy'
        verbose_name = 'proxy'
        verbose_name_plural = 'proxies'

    def __str__(self):
        return self.host + self.port


class UserAgent(SoftDeleteModel):
    STATUSES = (
        ('CREATED', 'created'),
        ('ACTIVE', 'active'),
        ('INACTIVE', 'inactive'),
    )

    name = models.CharField(max_length=256)
    status = models.CharField(max_length=256, choices=STATUSES, default='CREATED')

    class Meta:
        db_table = 'api_useragent'
        verbose_name = 'user agent'
        verbose_name_plural = 'user agents'

    def __str__(self):
        return self.name


class Account(SoftDeleteModel):
    STATUSES = (
        ('CREATED', 'created'),
        ('ACTIVE', 'active'),
        ('INACTIVE', 'inactive'),
    )

    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    new_mail_login = models.CharField(max_length=256, blank=True, null=True)
    new_mail_pass = models.CharField(max_length=256, blank=True, null=True)
    old_mail_login = models.CharField(max_length=256, blank=True, null=True)
    old_mail_pass = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    status = models.CharField(max_length=256, choices=STATUSES, default='CREATED')
    useragent = models.ForeignKey(UserAgent, on_delete=models.DO_NOTHING, related_name='accounts', blank=True, null=True)
    proxy = models.ForeignKey(Proxy, on_delete=models.DO_NOTHING, related_name='accounts', blank=True, null=True)

    class Meta:
        db_table = 'api_account'
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

    def __str__(self):
        return self.username


class Influencer(SoftDeleteModel):
    username = models.CharField(max_length=256)
    last_post_id = models.CharField(max_length=256, blank=True, null=True, default=None)
    last_post_days = models.IntegerField(default=0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='influencers')

    class Meta:
        db_table = 'api_influencer'
        verbose_name = 'influencer'
        verbose_name_plural = 'influencers'

    def __str__(self):
        return self.username


class Comment(SoftDeleteModel):
    text = models.CharField(max_length=256)
    used_times = models.IntegerField(default=0)

    class Meta:
        db_table = 'api_comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.text


class AccountStatistics(SoftDeleteModel):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='statistics')
    login_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    monitor_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'api_account_statistics'
        verbose_name = 'account statistics'
        verbose_name_plural = 'account statistics'

    def __str__(self):
        return str(self.account)


class AccountActivity(SoftDeleteModel):
    TYPES = (
        ('LOGIN', 'login'),
        ('MONITOR', 'monitor'),
        ('COMMENT', 'comment'),
    )

    STATUSES = (
        ('DEFAULT', 'default'),
        ('SUCCESS', 'success'),
        ('ERROR', 'error'),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='activity')
    type = models.CharField(max_length=8, choices=TYPES)
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE, related_name='activity')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='activity')
    datetime = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=256, choices=STATUSES, default='DEFAULT')

    class Meta:
        db_table = 'api_account_activity'
        verbose_name = 'account activity'
        verbose_name_plural = 'account activities'

    def __str__(self):
        return str(self.account)
