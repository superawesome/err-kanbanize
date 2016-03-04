from errbot import BotPlugin, botcmd, re_botcmd
import re
import time
import requests
import json


class Kanbanize(BotPlugin):
    def get_configuration_template(self):
        return {'SUBDOMAIN': u'', 'APIKEY': u'', 'BOARDID': 1, 'CHANNEL': u''}


    @botcmd
    def expedited(self, msg, args):
        bugs_found = self.check_expedited()
        if bugs_found == False:
            return "0 unassigned, unfinished expedited bugs found! w00t!"
        else:
            return None


    def check_expedited(self):
        # get Kanbanize bugs
        headers = {'apikey': self.config['APIKEY'], 'Content-Type': 'application/json'}
        data = { 'boardid': self.config['BOARDID'] }
        r = requests.post('https://%s.kanbanize.com/api/kanbanize/get_all_tasks/format/json' % self.config['SUBDOMAIN'], headers=headers, data=json.dumps(data))
        tasks = r.json()

        # print the ones that are in the Expedited lane, not done, and not assigned
        retval = False
        for i in tasks:
            if i['lanename'] == 'Expedited' and i['columnname'] != 'Done' and i['assignee'] == "None":  # yeah, it's literally the string "None"
                retval = True
                message = "webops: Expedited bug: %s" % i['extlink']
                self.send(self.config['CHANNEL'], message, message_type='groupchat')

        # return whether we printed anything - used by the command to run the check on-demand
        return retval


    def activate(self):
        super(Kanbanize, self).activate()
        self.start_poller(600, self.check_expedited)
