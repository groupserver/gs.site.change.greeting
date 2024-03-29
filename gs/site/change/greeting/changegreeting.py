# coding=utf-8
from zope.formlib import form
from gs.content.form.form import SiteForm
from zope.component import createObject
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from interfaces import IChangeGreeting

class ChangeGreeting(SiteForm):
    label = u'Change Greeting'
    pageTemplateFileName = 'browser/templates/changegreeting.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IChangeGreeting)
    greetingProp = 'greeting'
    
    def __init__(self, context, request):
        SiteForm.__init__(self, context, request)
        self.__groupsInfo = None
        self.__userInfo = None
        
    def setUpWidgets(self, ignore_request=False):
        divisionConfig = self.context.DivisionConfiguration
        data = {
          'greeting': divisionConfig.getProperty(self.greetingProp, 'Hi'),
        }
        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self, data=data,
            ignore_request=ignore_request)
        assert self.widgets
       
    @property
    def userInfo(self):
        if self.__userInfo == None:
            self.__userInfo = createObject('groupserver.LoggedInUser', 
              self.context)
        return self.__userInfo
    
    @property
    def groupsInfo(self):
        if  self.__groupsInfo == None:
            self.__groupsInfo = createObject('groupserver.GroupsInfo', 
                self.context)
        return self.__groupsInfo
        
    def groupMembership(self):
        groups = self.groupsInfo.get_member_groups_for_user(
            self.userInfo.user, self.userInfo.user)
        retval = [createObject('groupserver.GroupInfo', g) for g in groups]
        retval.sort(key=lambda group: group.name.lower())
        assert type(retval) == list
        return retval

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_set(self, action, data):
        assert data, 'No data'
        greeting = data['greeting']
        assert self.greetingProp, 'No greeting'
        
        divisionConfig = self.context.DivisionConfiguration
        if hasattr(divisionConfig, self.greetingProp):
            divisionConfig.manage_changeProperties(REQUEST=None,
                **{self.greetingProp: greeting})
        else:
            divisionConfig.manage_addProperty(self.greetingProp, 
                '', 'string')
            divisionConfig.manage_changeProperties(REQUEST=None,
                **{self.greetingProp: greeting})

        self.status = u"Changed the greeting to <q>%s</q>" % greeting
            

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status=u'<p>%s</p>' % errors[0]
        else:
            self.status = u'<p>There were errors:</p>'

