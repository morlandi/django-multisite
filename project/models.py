from django.db import models
#from django.db.models import signals
#from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField('name', max_length=128)

    class Meta:
        verbose_name_plural = "Customers"

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField('name', max_length=128)
    customer = models.ForeignKey(Customer, verbose_name="customer")

    class Meta:
        verbose_name_plural = "Projects"

    def __unicode__(self):
        return self.name


# class UserProfile(models.Model):

#     user = models.ForeignKey(User, editable=False, unique=True, verbose_name=_("User"))
#     active_company = models.ForeignKey(Company, null=True, blank=True, verbose_name=_(u'Active company'))

#     class Meta:
#         verbose_name = _(u"User profile")
#         verbose_name_plural = _(u"User profiles")
#         ordering = ('-user__date_joined',)

#     def __unicode__(self):
#         return _("Profile of user") + " %s %s (%s) <%s>" % (
#             self.user.first_name, self.user.last_name, self.user.username,
#             self.user.email)


# def create_default_user_profile(user):
#     try:
#         profile = UserProfile.objects.get(user=user)
#     except UserProfile.DoesNotExist:
#         profile = UserProfile()
#         profile.user = user
#         profile.save()


# def get_user_profile_ex(user):
#     if user.is_anonymous():
#         return None
#     try:
#         profile = user.get_profile()
#     except Exception, e:
#         create_default_user_profile(user)
#         profile = user.get_profile()
#     return profile


# def user_post_save(sender, instance, **kwargs):
#     created = kwargs.get('created', False)
#     create_default_user_profile(instance)
# signals.post_save.connect(user_post_save, sender=User)
