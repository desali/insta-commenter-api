from django.urls import path

from api.views import ProxyListView, ProxyCreateView, ProxyDetailView, ProxyDetailPKView, UserAgentListView, \
    UserAgentCreateView, UserAgentDetailPKView, UserAgentDetailView, CommentListView, CommentCreateView, \
    CommentDetailPKView, CommentDetailView, ProxyDestroyView, UserAgentDestroyView, CommentDestroyView, AccountListView, \
    AccountCreateView, AccountDetailPKView, AccountDetailView, AccountDestroyView, InfluencerListView, \
    InfluencerCreateView, InfluencerDetailPKView, InfluencerDetailView, InfluencerDestroyView, AccountEditView, \
    InfluencerEditView

app_name = "api"
urlpatterns = [
    path('proxies/', ProxyListView.as_view(), name="proxy_list"),
    path('proxy/', ProxyCreateView.as_view(), name="proxy_create"),
    path('proxy/<int:pk>/', ProxyDetailPKView.as_view(), name="proxy_detail_pk"),
    path('proxy_by_host/', ProxyDetailView.as_view(), name="proxy_detail_host_port"),
    path('proxy/<int:pk>/delete/', ProxyDestroyView.as_view(), name="proxy_destroy_pk"),

    path('useragents/', UserAgentListView.as_view(), name="user_agent_list"),
    path('useragent/', UserAgentCreateView.as_view(), name="user_agent_create"),
    path('useragent/<int:pk>/', UserAgentDetailPKView.as_view(), name="user_agent_detail_pk"),
    path('useragent_by_name/', UserAgentDetailView.as_view(), name="user_agent_detail_name"),
    path('useragent/<int:pk>/delete/', UserAgentDestroyView.as_view(), name="useragent_destroy_pk"),

    path('comments/', CommentListView.as_view(), name="comment_list"),
    path('comment/', CommentCreateView.as_view(), name="comment_create"),
    path('comment/<int:pk>/', CommentDetailPKView.as_view(), name="comment_detail_pk"),
    path('comment_by_text/', CommentDetailView.as_view(), name="comment_detail_text"),
    path('comment/<int:pk>/delete/', CommentDestroyView.as_view(), name="comment_destroy_pk"),

    path('accounts/', AccountListView.as_view(), name="account_list"),
    path('account/', AccountCreateView.as_view(), name="account_create"),
    path('account/<int:pk>/', AccountDetailPKView.as_view(), name="account_detail_pk"),
    path('account_by_username/', AccountDetailView.as_view(), name="account_detail_username"),
    path('account/<int:pk>/edit/', AccountEditView.as_view(), name='account_edit'),
    path('account/<int:pk>/delete/', AccountDestroyView.as_view(), name="account_destroy_pk"),

    path('influencers/', InfluencerListView.as_view(), name="influencer_list"),
    path('influencer/', InfluencerCreateView.as_view(), name="influencer_create"),
    path('influencer/<int:pk>/', InfluencerDetailPKView.as_view(), name="influencer_detail_pk"),
    path('influencer_by_username/', InfluencerDetailView.as_view(), name="influencer_detail_username"),
    path('influencer/<int:pk>/edit/', InfluencerEditView.as_view(), name='influencer_edit'),
    path('influencer/<int:pk>/delete/', InfluencerDestroyView.as_view(), name="influencer_destroy_pk"),
]
