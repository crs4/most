# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from datetime import date, datetime
import string
from django.core.exceptions import ValidationError
from utils import make_new_uid
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class TaskGroup(models.Model):
    """Class TaskGroup

    Attributes:
        title                   (django.db.models.CharField)    : task group title
        description             (django.db.models.CharField)    : task group description
        task_group_type         (django.db.models.CharField)    : task group type
        hospital                (django.db.models.CharField)    : task group's hospital
        is_health_care_provider (django.db.models.BooleanField) : task group able to play specialized role
    """
    TASK_GROUP_TYPES = (
        ('SP', 'Service Provider'),
        ('HF', 'Health Care Facilities'),
    )

    title = models.CharField(_('Title'), max_length=100, unique=True)
    description = models.CharField(_('Description'), max_length=100, help_text=_('e.g. "Pediatric Cardiology"'))
    task_group_type = models.CharField(_('Task group type'), choices=TASK_GROUP_TYPES, max_length=2)
    hospital = models.CharField(_('Hospital'), max_length=100, default=None, null=True, blank=True)  # TODO (OPTIONAL) :: create Hospital class
    users = models.ManyToManyField('MostUser', related_name='task_group_related', null=True, blank=True,
                                   verbose_name=_('MOST Users'))
    is_health_care_provider = models.BooleanField(_('Is health care provider?'), default=True)
    is_active = models.BooleanField(_('Is active?'), default=True)

    # hospital = models.ForeignKey("Hospital", verbose_name=_("Hospital"))
    # task_group_type = models.CharField(_("Task group type"), max_length=50, null=True, blank=True,
    #                                    help_text=_("The S.S.D. (e.g. \"Patologia Cardiaca\")"))
    # secretariat_phone = models.CharField(_("Secretariat phone"), max_length=50, null=True, blank=True)
    # secretariat_fax = models.CharField(_("Secretariat fax"), max_length=50, null=True, blank=True)
    # director = models.CharField(_("Director"), max_length=150)
    # head_office_phone = models.CharField(_("Head office phone"), max_length=50, null=True, blank=True)
    # head_office_email = models.EmailField(_("Head office email"), null=True, blank=True)
    # tc_service = models.BooleanField(_("Offers teleconsultation service?"),
    #     help_text=_("select if the task group offers an teleconsultation service"), default=False)
    # devices = models.ManyToManyField(Device, verbose_name=_("Devices"), related_name="taskgroups", null=True, blank=True)

    def clinicians_count(self):
        return self.users.filter(clinician_related__isnull=False).count()

    def clean(self):
        # If is_health_care_provider == True and task_group_type != 'HF', raise exception
        if not self.task_group_type == 'HF' and self.is_health_care_provider:
            raise ValidationError(_('Only health care facilities can provide health care service.'))

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        db_table = 'most_task_group'
        verbose_name = _('Task Group')
        verbose_name_plural = _('Task Groups')


class MostUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, password=None):
        if not (username and first_name and last_name and email):
            raise ValueError('Users must have a username, a first_name, a last_name and an email')
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password):
        user = self.create_user(
            username,
            first_name,
            last_name,
            email,
            password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MostUser(AbstractBaseUser):
    """Class UserProfile

    Attributes:
        uid                     (django.db.models.CharField)        : autogenerated unique identification number
        user                    (django.contrib.auth.models.User)   : predefined django user model
        numeric_password    (   django.db.models.CharField)         : numeric password (for app login purpose)
        user_type               (django.db.models.CharField)        : user type
        gender                  (django.db.models.CharField)        : user gender
        phone                   (django.db.models.CharField)        : user phone number
        mobile                  (django.db.models.CharField)        : user mobile phone number
        certified_email         (django.db.models.EmailField)       : user certified email
        creation_timestamp      (django.db.models.DateTimeField)    : user creation timestamp
        last_modified_timestamp (django.db.models.DateTimeField)    : user last modification timestamp
        deactivation_timestamp  (django.db.models.DateTimeField)    : user deactivation timestamp
        is_health_care_provider  (django.db.models.BooleanField)    : clinician able to play specialized role
    """
    USER_TYPES = (
        ('AD', _('Administrative')),
        ('TE', _('Technician')),
        ('CL', _('Clinician')),
        ('ST', _('Student')),
    )
    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
        ('U', _('Unknown')),
    )

    username = models.CharField(_('Username'), max_length=30, unique=True)
    first_name = models.CharField(_('User first name'), max_length=50)
    last_name = models.CharField(_('User last name'), max_length=50)
    email = models.EmailField(_('User email address'), max_length=255)
    birth_date = models.DateField(_('User birth date'), null=True, blank=True)
    is_staff = models.BooleanField(_('Is the user staff?'), default=True)
    is_active = models.BooleanField(_('Is the user active?'), default=True)
    # is_superuser = models.BooleanField(_('Is the user superuser?'), default=False)
    is_admin = models.BooleanField(_('Is the user superuser?'), default=False)
    # user = models.ForeignKey(User)
    uid = models.CharField(max_length=40, default=make_new_uid, unique=True)
    numeric_password = models.CharField(max_length=4, null=True, blank=True, verbose_name=_('Numeric password'),
                                        help_text=_('4 numbers code'))
    user_type = models.CharField(_('User type'), choices=USER_TYPES, max_length=2, default='ST')
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES, default='U')
    phone = models.CharField(_('Phone'), max_length=20, null=True, blank=True)  # TODO: validation rules
    mobile = models.CharField(_('Mobile phone'), max_length=20, null=True, blank=True)  # TODO: validation rules
    certified_email = models.EmailField(_('Certified email'), null=True, blank=True)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_modified_timestamp = models.DateTimeField(auto_now=True)
    deactivation_timestamp = models.DateTimeField(null=True, blank=True, default=None)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', ]

    objects = MostUserManager()

    def get_full_name(self):
        return u'%s %s [%s]' % (self.last_name, self.first_name, self.get_user_type_display())

    def get_short_name(self):
        return u'%s [%s]' % (self.username, self.user_type)

    def __unicode__(self):
        return u'%s %s' % (self.last_name, self.first_name)

    def to_dictionary(self):
        try:
            birth_date = u'%s' % self.birth_date.strftime('%d %b %Y') if self.birth_date else None
        except Exception, e:
            birth_date = u'%s' % datetime.strptime(self.birth_date, '%Y-%m-%d').strftime('%d %b %Y') \
                if self.birth_date else None
        user_dictionary = {
            'id': u'%s' % self.id,
            'uid': u'%s' % self.uid,
            'username': u'%s' % self.username,
            'first_name': u'%s' % self.first_name,
            'last_name': u'%s' % self.last_name,
            'birth_date': birth_date,
            'is_staff': self.is_staff,
            'is_active': self.is_active,
            'is_admin': self.is_admin,
            'user_type': {
                'code': u'%s' % self.user_type,
                'value': u'%s' % self.get_user_type_display()
            },
            'gender': {
                'code': u'%s' % self.gender,
                'value': u'%s' % self.get_gender_display()
            },
            'email': u'%s' % self.email,
            'phone': u'%s' % self.phone if self.phone else None,
            'mobile': u'%s' % self.mobile if self.mobile else None,
            'certified_email': u'%s' % self.certified_email if self.certified_email else None
        }
        return user_dictionary

    # def clean(self):
    #     # If numeric_password is not numeric and length of numeric_password is not 4, raise exception
    #     if not (self.numeric_password.isdigit() and len(self.numeric_password) == 4):
    #         raise ValidationError(_('Numeric password has to be 4 digit number.'))
    #
    # def save(self, *args, **kwargs):
    #     if self.user_type == 'TE':
    #         self.user.is_staff = True
    #     super(UserProfile, self).save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'most_user'
        verbose_name = _('MOST user')
        verbose_name_plural = _('MOST users')


class ClinicianUser(models.Model):
    """Class ClinicianUserProfile

    Attributes:
        user_profile        (django.db.models.ForeignKey :: UserProfile)    : numeric password (for app login purpose)
        clinician_type      (django.db.models.CharField)                    : clinician type
        specialization      (django.db.models.CharField)                    : clinical specialization
    """
    CLINICIAN_TYPES = (
        ('DR', _('Doctor')),
        ('OP', _('Operator')),
    )

    user = models.ForeignKey('MostUser', related_name='clinician_related')
    clinician_type = models.CharField(_('Clinician type'), choices=CLINICIAN_TYPES, max_length=2)
    specialization = models.CharField(_('Clinical specialization'), null=True, blank=True, max_length=50)
    # If is_health_care_provider == True and clinician_type == 'DO', it can play the specialized role
    is_health_care_provider = models.BooleanField(_('Is health care provider?'), default=True)

    def get_full_name(self):
        full_name = u'[%s] %s' % (self.clinician_type, self.user)
        if self.specialization:
            full_name += u'- %s' % self.specialization
        return full_name

    def __unicode__(self):
        clinician_string = u'%s %s' % (self.get_clinician_type_display(), self.user)
        if self.specialization:
            clinician_string += u' (%s)' % self.specialization
        if self.is_health_care_provider:
            clinician_string += u' - Provider'
        return clinician_string

    def clean(self):
        # If is_health_care_provider == True and clinician_type != 'DO', raise exception
        if not self.clinician_type == 'DR' and self.is_health_care_provider:
            raise ValidationError(_('Only doctors can provide health care service'))

    class Meta:
        db_table = 'most_clinician_user'
        verbose_name = _('Clinician User')
        verbose_name_plural = _('Clinician Users')
