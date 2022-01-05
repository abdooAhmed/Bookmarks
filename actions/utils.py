import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action


def create_action(user, verb, target=None):
    now = timezone.now()
    last_minut = now - datetime.timedelta(seconds=60)
    simila_actions = Action.objects.filter(user_id = user.id,verb=verb,created=last_minut)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        simila_actions = simila_actions.filter(target_ct=target_ct,target_id=target.id)
    if not simila_actions:
        action = Action(user=user,verb=verb,target=target)
        action.save()
        return True
    return False