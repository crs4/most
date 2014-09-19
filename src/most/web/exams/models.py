from django.db import models
from django.utils.translation import ugettext_lazy as _


class ExamState(models.Model):
    code = models.IntegerField(_('State code'))
    description = models.CharField(_('State description'), max_length=25)


class Exam(models.Model):

    creation_datetime = models.DateTimeField(_('Creation DateTime'))
    modification_datetime = models.DateTimeField(_('Modification DateTime'), null=True, blank=True)
    deactivation_datetime = models.DateTimeField(_('Deactivation Date Time'), null=True, blank=True)
    is_active = models.BooleanField(_('Is active (set to false for delation)?'), default=True)
    is_teleconsultation = models.BooleanField(_('Is a teleconsultation?'), default=False)
    state = models.ForeignKey('ExamState', related_name='exam')
    notes = models.TextField(_('Summary'), max_length=500, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s | %s [%s %s]' % ( self.id, self.name,self.patient, self.clinician, self.creation_date_time.strftime("%d %B %Y"))

    class Meta:
        verbose_name = _("Exam")
        verbose_name_plural = _("Exams")


class Eco(models.Model):
    pass