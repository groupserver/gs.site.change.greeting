# coding=utf-8
from zope.interface.interface import Interface
from zope.schema import TextLine

class IChangeGreeting(Interface):
    greeting = TextLine(title=u'Greeting',
      description=u'The greeting, salutation and facilitation that '\
        u'you want to appear on the homepage.',
      required=True)

