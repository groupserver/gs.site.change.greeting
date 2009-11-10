# coding=utf-8
from zope.formlib import form
from zope.component import createObject
from Products.Five.formlib.formbase import PageForm
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from abel.greeting.interfaces import IChangeGreeting

class ChangeGreeting(PageForm):
    label = u'Change Greeting'
    pageTemplateFileName = 'browser/templates/changegreeting.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IChangeGreeting)
    
    def __init__(self, context, request):
        PageForm.__init__(self, context, request)
        self.siteInfo = createObject('groupserver.SiteInfo', context)

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_set(self, action, data):
        self.status = u"I don't handle change!"

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status=u'<p>%s</p>' % errors[0]
        else:
            self.status = u'<p>There were errors:</p>'

