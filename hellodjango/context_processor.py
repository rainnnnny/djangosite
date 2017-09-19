from django.conf import settings as original_settings

def settings(request):
    return {'settings': original_settings}

def AccInfo(request):
    return {'current_Acc': request.COOKIES.get("id_logged_in")}
