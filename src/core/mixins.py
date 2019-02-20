from django import forms
from django.forms.utils import ErrorList


class FormUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            user = self.request.user
            form.instance.user = user
            form.save()
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = \
                ErrorList(['Please login to continue'])
            return super(FormUserNeededMixin, self).form_invalid(form)


class OwnerAllowedMixin(object):
    def form_valid(self, form):
        if self.request.user == form.instance.user:
            return super(OwnerAllowedMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = \
                ErrorList(['Only owner is allowed to edit'])
            return super(OwnerAllowedMixin, self).form_invalid(form)
