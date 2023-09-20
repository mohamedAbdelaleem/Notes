from djoser.email import PasswordResetEmail
from django.conf import settings

SITE_NAME = 'Notes keep'

class CustomPasswordResetEmail(PasswordResetEmail):
    
    def get_context_data(self):
        
        context = super().get_context_data()
        context.update({
            'domain': settings.FRONT_END_DOMAIN,
            'site_name': SITE_NAME,
        })
        
        # context["url"] =
        return context
