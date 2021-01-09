from django.contrib import admin

from api.models import Proxy, UserAgent, Account, Influencer, Comment, AccountStatistics, AccountActivity

admin.site.register(
    [
        Proxy,
        UserAgent,
        Account,
        Influencer,
        Comment,
        AccountStatistics,
        AccountActivity
    ]
)
