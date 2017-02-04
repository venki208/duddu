from django.conf import settings # import the settings file

def general_settings(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return_dict = {
        'LOGIN_URL': settings.LOGIN_URL,
    }
    return return_dict
