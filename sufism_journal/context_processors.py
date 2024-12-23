def theme(request):
    return {'is_superuser': request.user.is_superuser}
