from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import CreatorBaseModel
from common.validators import validate_positive


class ExamTemplate(CreatorBaseModel):
    """Model definition for ExamTemplate."""

    name = models.CharField(_("name"), max_length=128)
    # description = models.TextField(blank=True)
    duration = models.DurationField(_("duration"))
    # models.IntegerField(default=0, validators=[validate_positive])
    full_marks = models.DecimalField(
        _("full_marks"), max_digits=5, decimal_places=2, default=0
    )
    pass_marks = models.DecimalField(
        _("pass_marks"), max_digits=5, decimal_places=2, default=0
    )
    display_num_questions = models.PositiveIntegerField(
        _("display_num_questions"), default=1
    )
    # exam_type = models.CharField(max_length=10, choices=(
    #     ('S', 'SINGLE'), ('M', 'MULTIPLE')), default='S')

    class Meta:
        verbose_name = _("Exam Template")
        verbose_name_plural = _("Exam Templates")

    def __str__(self):
        return self.name


class ExamStatus:
    CREATED = "created"
    STARTED = "started"
    FINISHED = "finished"
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"

    CHOICES = [
        (CREATED, "Created"),
        (STARTED, "Started"),
        (FINISHED, "Finished"),
        (SCHEDULED, "Scheduled"),
        (CANCELLED, "Cancelled"),
    ]


# Create your models here.


class Exam(CreatorBaseModel):
    """Model definition for Exam."""

    name = models.CharField(_("name"), max_length=128)
    category = models.ManyToManyField(
        "courses.CourseCategory",
        verbose_name=_("categories"),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    # TODO: Add course field here after course app is created
    # Also how to relate course to exams?
    # course = models.ForeignKey("courses.Course",
    #                            verbose_name=_("course"),
    #                            related_name="%(app_label)s_%(class)s_related",
    #                            related_query_name="%(app_label)s_%(class)ss",
    #                            on_delete=models.SET_NULL,
    #                            null=True,
    #                            blank=True)
    status = models.CharField(
        _("status"),
        max_length=16,
        choices=ExamStatus.CHOICES,
        default=ExamStatus.CREATED,
    )
    price = models.DecimalField(
        _("price"),
        max_digits=5,
        decimal_places=2,
        default=Decimal("0.0"),
        validators=[validate_positive],
    )
    template = models.ForeignKey(
        ExamTemplate,
        verbose_name=_("template"),
        related_name="exams",
        on_delete=models.CASCADE,
    )
    # tags = models.ManyToManyField("tags.Tag", verbose_name=_("tags"), blank=True)
    # full marks and pass marks are attribute of the exam template

    class Meta:
        """Meta definition for Exam."""

        verbose_name = "Exam"
        verbose_name_plural = "Exams"
        ordering = ["-created_at"]

    def __str__(self):
        """Unicode representation of Exam."""
        return self.name

    def change_status(self, status):
        self.status = status
        self.save()

    @property
    def current_status(self):
        return self.status

    # FSM State transition methods
    def start_exam(self):
        self.change_status(ExamStatus.STARTED)

    def finish_exam(self):
        self.change_status(ExamStatus.FINISHED)

    def schedule_exam(self):
        self.change_status(ExamStatus.SCHEDULED)

    def cancel_exam(self):
        self.change_status(ExamStatus.CANCELLED)


# class SectionTemplate(models.Model):
class Section(models.Model):
    """Model definition for Section."""

    name = models.CharField(_("name"), max_length=64)
    num_of_questions = models.IntegerField(_("num_of_questions"), default=0)
    pos_marks = models.DecimalField(
        _("pos_marks"), max_digits=5, decimal_places=2, default=Decimal("2.0")
    )
    neg_marks = models.DecimalField(
        _("neg_marks"), max_digits=5, decimal_places=2, default=Decimal("0.4")
    )
    template = models.ForeignKey(
        ExamTemplate, verbose_name=_("template"), on_delete=models.CASCADE
    )

    class Meta:
        """Meta definition for Section."""

        verbose_name = "Section"
        verbose_name_plural = "Sections"

    def __str__(self):
        """Unicode representation of Section."""
        return self.name


# class Section(models.Model):
#     """Model definition for Section."""

#     exam = models.ForeignKey(
#         Exam,
#         verbose_name=_("exam"),
#         related_name=_("sections"),
#         on_delete=models.CASCADE,
#     )
#     template = models.ForeignKey(
#         SectionTemplate,
#         verbose_name=_("template"),
#         relate3d_name=_("sections"),
#         on_delete=models.CASCADE
#     )

#     class Meta:
#         """Meta definition for Section."""

#         verbose_name = 'Section'
#         verbose_name_plural = 'Sections'

#     def __str__(self):
#         """Unicode representation of Section."""
#         return f'{self.name}'


class Question(models.Model):
    """Model definition for Question."""

    detail = models.TextField(_("detail"))
    img = models.ImageField(_("img"), upload_to="questions/", null=True, blank=True)
    exam = models.ForeignKey(
        Exam,
        verbose_name=_("exam"),
        related_name=_("questions"),
        on_delete=models.CASCADE,
    )
    section = models.ForeignKey(
        Section,
        verbose_name=_("section"),
        related_name=_("sections"),
        on_delete=models.CASCADE,
    )
    feedback = models.TextField(_("feedback"), blank=True, null=True)

    class Meta:
        """Meta definition for Question."""

        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ["exam", "id"]

    def __str__(self):
        """Unicode representation of Question."""
        return f"{self.exam}_{self.id}"


class Option(models.Model):
    """Model definition for Option."""

    detail = models.TextField(_("detail"))
    correct = models.BooleanField(_("correct"), default=False)
    question = models.ForeignKey(
        Question,
        verbose_name=_("question"),
        related_name=_("options"),
        on_delete=models.CASCADE,
    )
    img = models.ImageField(_("img"), upload_to="options/", null=True, blank=True)

    class Meta:
        """Meta definition for Option."""

        verbose_name = "Option"
        verbose_name_plural = "Options"
        ordering = ["question", "id"]

    def __str__(self):
        """Unicode representation of Option."""
        return f"{self.question}_{self.id}"