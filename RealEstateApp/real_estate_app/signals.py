from django.db.models.signals import pre_save
from django.dispatch import receiver

from real_estate_app.models import RealEstate, Agent, RealEstateAgent


@receiver(pre_save, sender=RealEstate)
def my_handler(sender, instance, **kwargs):

    old_instance = RealEstate.objects.filter(id=instance.id).first()

    if old_instance:
        if old_instance.is_sold != instance.is_sold:
            agent_real_estates = RealEstateAgent.objects.filter(real_estate=old_instance).all()
            for agent_real_estate in agent_real_estates:
                agent = agent_real_estate.agent
                agent.num_sales += 1
                agent.save()



