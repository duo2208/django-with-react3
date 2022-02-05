from rest_framework.authtoken.views obtain_auth_token

urlpatterns += [
    path('api-token-auth/', obtain_auth_token)
]