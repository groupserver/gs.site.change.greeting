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
        self.__groupsInfo = None
        self.__userInfo = None
        
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
        self.status = u"I don't handle change!"

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status=u'<p>%s</p>' % errors[0]
        else:
            self.status = u'<p>There were errors:</p>'

