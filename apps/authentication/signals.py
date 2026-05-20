# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from apps.authentication.models import User
# from apps.onboarding.models import OnboardingProgress
# from apps.profile.models import UserProfile
# from apps.shell.models import ShellPreference
# from apps.startup.models import StartupProfile


# @receiver(post_save, sender=User)
# def create_related_user_profiles(sender, instance, created, **kwargs):
#     if not created:
#         return

#     UserProfile.objects.get_or_create(user=instance)
#     StartupProfile.objects.get_or_create(user=instance)
#     OnboardingProgress.objects.get_or_create(user=instance)
#     ShellPreference.objects.get_or_create(user=instance)


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.utils import ProgrammingError  # Add this import

from apps.authentication.models import User
from apps.onboarding.models import OnboardingProgress
from apps.profile.models import UserProfile
from apps.shell.models import ShellPreference
from apps.startup.models import StartupProfile


@receiver(post_save, sender=User)
def create_related_user_profiles(sender, instance, created, **kwargs):
    if not created:
        return

    # Wrap writes in a try/except block to keep management commands safe
    try:
        UserProfile.objects.get_or_create(user=instance)
        StartupProfile.objects.get_or_create(user=instance)
        OnboardingProgress.objects.get_or_create(user=instance)
        ShellPreference.objects.get_or_create(user=instance)
    except ProgrammingError:
        # Bypasses profile initialization gracefully if tables don't exist yet
        pass