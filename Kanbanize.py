from errbot import BotPlugin, botcmd, re_botcmd
import re
import time
import requests

class Kanbanize(BotPlugin):
    pass
#    @re_botcmd(pattern=r"^(.*)#cl$", prefixed=False, flags=re.IGNORECASE)
#    def something(self, msg, match):
#        """put something into the changelog"""
#
#        # -d "{\"criticality\": 2, \"unix_timestamp\": $WHEN, \"category\": \"puppet\", \"description\": \"$REPO; $REV; $WHODUNIT; $i\"}"
#
#        cl_message = match.group(1).strip()
#        data = {
#                'criticality': 2,
#                'unix_timestamp': int(time.time()),
#                'category': 'irc',
#                'description': msg.frm.nick + ': ' + cl_message
#        }
#        headers = {
#                'Content-Type': 'application/json'
#        }
#        r = requests.post("https://changelog.allizom.org/api/events", headers=headers, json=data)
#        #munged_name = msg.frm.nick[:1] + '\x030' + msg.frm.nick[1:]  # doesn't work, prints a 0 in the name ... how to do this?
#        munged_name = msg.frm.nick  # do nothing for now
#        self.send('#cl', "<%s> %s" % (munged_name, cl_message), message_type='groupchat')
#        # return "from %s: %s" % (msg.frm.nick, cl_message)


    def check_expedited(self):
        self.log.debug("This is where I should be checking the expedited lane in kanbanize.com and spewing stuff into #webops")


    def activate(self):
        super(Kanbanize, self).activate()
        self.start_poller(60, self.check_expedited)
