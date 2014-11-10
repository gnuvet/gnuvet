"""Client window."""
# TODO:
# add buttons for patient: New MarkAsRIP
#     ChangeOwner only from patient window
#  and resp Actions/functions
from datetime import date
from decimal import Decimal as D
from psycopg2 import OperationalError
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QAction, QMainWindow, QMenu
import gv_qrc
from keycheck import Keycheck
from util import ch_conn, gprice, money, querydb # ch_conn so far unused
from client_ui import Ui_Client

class Client(QMainWindow):
    """The client window, from which to choose a patient and such."""
    # signals:
    gvquit   = pyqtSignal(bool)
    helpsig  = pyqtSignal(str)
    savestate = pyqtSignal(str)

    # vars:
    db_err = changes = shutdown = False

    def __init__(self, parent=None, clid=0):
        super(Client, self).__init__(parent)
        self.conns  = {} # pyqt bug, disconnect() w/o arg can segfault
        self.sigs   = {}
        self.clid = clid
        self.w = Ui_Client()
        self.w.setupUi(self)
        keych = Keycheck(self)
        self.installEventFilter(keych)
        #    LOCAL VARIABLES
        #    ACTIONS
        closeA = QAction(self.tr('Close &Window'), self)
        closeA.setAutoRepeat(0)
        closeA.setShortcut(self.tr('Ctrl+W'))
        closeA.setStatusTip(self.tr('Close this window'))
        self.dbA = QAction(self.tr('&Reconnect to database'), self)
        self.dbA.setAutoRepeat(0)
        self.dbA.setShortcut(self.tr('Ctrl+R'))
        self.dbA.setStatusTip(self.tr('Try to reconnect to database'))
        aboutA = QAction(self.tr('About &Gnuvet'), self)
        aboutA.setAutoRepeat(0)
        aboutA.setStatusTip(self.tr('GnuVet version info'))
        helpA = QAction(self.tr('&Help'), self)
        helpA.setAutoRepeat(0)
        helpA.setShortcut(self.tr('F1'))
        helpA.setStatusTip(self.tr('context sensitive help'))
        quitA = QAction(self.tr('&Quit GnuVet'), self)
        quitA.setAutoRepeat(0)
        quitA.setShortcut(self.tr('Ctrl+Q'))
        quitA.setStatusTip(self.tr('Quit GnuVet'))
        self.editA = QAction(self.tr('&Edit Client'), self)
        self.editA.setAutoRepeat(0)
        self.editA.setShortcut(self.tr('Ctrl+E'))
        self.editA.setStatusTip(self.tr('Edit client record'))
        self.mrgA = QAction(self.tr('&Merge Client'), self)
        self.mrgA.setAutoRepeat(0)
        self.mrgA.setStatusTip(
            self.tr('Merge this client\'s accounts if you have more than one'))
        self.newpatA = QAction(self.tr('&Patient'), self)
        self.newpatA.setAutoRepeat(0)
        self.newpatA.setShortcut(self.tr('Ctrl+P'))
        self.newpatA.setStatusTip(self.tr("Add a patient to this client"))
        self.newsaleA = QAction(self.tr('S&ale'), self)
        self.newsaleA.setAutoRepeat(0)
        self.newsaleA.setShortcut(self.tr('Ctrl+A'))
        self.newsaleA.setStatusTip(self.tr('Enter patient-unrelated sale'))
        self.newpayA = QAction(self.tr('Pa&yment'), self)
        self.newpayA.setAutoRepeat(0)
        self.newpayA.setShortcut(self.tr('Ctrl+Y'))
        self.newpayA.setStatusTip(self.tr('Take payment'))
        self.rippatA = QAction(
            self.tr('&Mark patient deceased'), self)
        self.rippatA.setAutoRepeat(0)
        self.rippatA.setShortcut(self.tr('Ctrl+K'))
        self.rippatA.setStatusTip(self.tr('Mark selected patient as deceased'))
        # ...
        #    MENUES
        taskM = QMenu(self.w.menubar)
        taskM.setTitle(self.tr('&Task'))
        self.w.menubar.addAction(taskM.menuAction())
        newM = QMenu(self.w.menubar)
        newM.setTitle(self.tr('&New'))
        self.w.menubar.addAction(newM.menuAction())
        helpM = QMenu(self.w.menubar)
        helpM.setTitle(self.tr('&Help'))
        self.w.menubar.addAction(helpM.menuAction())
        #    SUBMENUES
        taskM.addAction(self.dbA)
        taskM.addSeparator()
        taskM.addAction(self.editA)
        taskM.addAction(self.mrgA)
        taskM.addAction(self.rippatA)
        taskM.addSeparator()
        taskM.addAction(closeA)
        taskM.addAction(quitA)
        taskM.setSeparatorsCollapsible(1)
        newM.addAction(self.newpatA)
        newM.addAction(self.newsaleA)
        newM.addAction(self.newpayA)
        helpM.addAction(helpA)
        helpM.addSeparator()
        helpM.addAction(aboutA)
        #    ACTION CONNECTIONS
        closeA.triggered.connect(self.close)
        self.editA.triggered.connect(self.editc)
        helpA.triggered.connect(self.help_self)
        quitA.triggered.connect(self.gv_quitconfirm)
        self.mrgA.triggered.connect(self.merge)
        self.newpatA.triggered.connect(self.addpat)
        self.newsaleA.triggered.connect(self.sale)
        self.newpayA.triggered.connect(self.payment)
        self.rippatA.triggered.connect(self.rip)
        #    PARENT CONNECTIONS
        if parent: # devel if
            self.dbA.triggered.connect(parent.db_connect)
            aboutA.triggered.connect(parent.about)
            parent.gvquit.connect(self.gv_quit)
            parent.dbstate.connect(self.db_state)
            ## self.savestate.connect(parent.state_write)
            self.helpsig.connect(parent.gv_help)
            self.db = parent.db
            self.staffid = parent.staffid
            self.options = parent.options
        else:
            import dbmod
            dbh = dbmod.Db_handler('enno')
            self.db = dbh.db_connect()
            self.staffid = 1
            from options import read_options
            self.options = read_options()
        #    BUTTON CONNECTIONS
        self.w.cancelPb.clicked.connect(self.close)
        #    INIT
        #ch_conn(self, 'enter', self.keych.enter, self.w.mainPb.click)
        #self.w.mainPb.clicked.connect(self.whatever)
        self.dbA.setVisible(0)
        self.dbA.setEnabled(0)
        try:
            self.curs = self.db.cursor()
        except (OperationalError, AttributeError) as e: # no db connection
            print('db.cursor(): {}'.format(e))
            self.db_state()
            return
        logname = 'no login' # neu
        lname = querydb(
            self,
            'select stf_logname from staff where stf_id=%s', (self.staffid,))
        if lname is None:  return # db error
        logname = lname[0][0]
        self.w.lLb.setText(logname)
        self.cli_data()
        self.get_pats()

    def addpat(self):
        print('client.addpat not yet implemented')
        
    def cli_data(self):
        """Collect client data."""
        result = querydb(
            self,
            'select t_title,c_sname,c_mname,c_fname,housen,street,village,city,'
            'region,postcode,c_telhome,c_telwork,c_mobile1,c_mobile2,c_email,'
            'baddebt,c_reg,c_last,c_anno from clients,titles,addresses where '
            't_id=c_title and c_address=addr_id and c_id=%s',
            (self.clid,))
        if result is None:  return # db error
        for res in result:
            name = ' '.join([res[0], res[1]])
            if res[2]:
                name = ', '.join([name, res[2]])
            name = ' '.join([name, res[3]])
            self.w.nameLb.setText(name)
            self.w.addr1Lb.setText(', '.join([e for e in res[4:6] if e]))
            self.w.addr2Lb.setText(', '.join([e for e in res[6:8] if e]))
            self.w.addr3Lb.setText(res[9])
            self.w.telhomeLb.setText(self.tr('Home: ') + res[10])
            self.w.telworkLb.setText(self.tr('Work: ') + res[11])
            self.w.mobile1Lb.setText(res[12])
            self.w.mobile2Lb.setText(res[13])
            self.w.emailLb.setText(res[14])
            self.w.bdPix.setVisible(res[15])
            self.w.regdateLb.setText(res[16].strftime('%d.%m.%y'))
            self.w.ldateLb.setText(res[17].strftime('%d.%m.%y'))
            ## self.w.annotxtLb.setText(res[18])
            self.w.annotxtLb.setText('This is our first client, being the first sentient being to have brought patients to our GnuVet practice.')
        cbal = D('0.00')
        pats = querydb(
            self,
            'select p_id from patients where p_cid=%s', (self.clid,))
        if pats is None:  return # db error
        pats = [e[0] for e in pats]
        for p in pats:
            ## hierwei: error if no accN table!
            addend = querydb(
                self,
                'select acc_npr,vat_rate,count from acc{0},prod{1},vats '
                'where acc_vat=vat_id and acc_prid=prod{1}.id and acc_pid='
                '%s and acc_paid is null'.format(self.clid, p), (p,))
            if addend is None:  return # db error
            for e in addend:
                cbal += money(gprice(e[0], e[1]), e[2])
        self.w.balanceLb.setText(str(cbal))
        
    def closeEvent(self, ev):
        if self.parent():
            self.parent().xy_decr()

    def dbdep_enable(self, yes=True):
        """En- or disable db dependent actions."""
        for action in (self.editA, self.mrgA, self.payA, self.saleA):
            action.setEnabled(yes)
        self.dbA.setVisible(not yes)
        self.dbA.setEnabled(not yes)
        
    def db_state(self, msg=''):
        """Actions to be taken on db loss or gain."""
        self.dberr = msg and True or False
        self.w.no_dbconn.setVisible(self.dberr)
        self.dbstate.emit(not self.dberr)
        self.dbdep_enable(not self.dberr)
        if not hasattr(self, 'warnw'):
            from warn import Warning
        self.warnw = Warning(self, self.tr('GnuVet: Db Error'), msg)
        if not self.isVisible(): # ?
            self.warnw.closed.connect(self.show)

    def editc(self):
        pass

    def get_pats(self):
        """Collect this client's patients."""
        result = querydb(
            self,
            'select p_name,xbreed,breed_abbr,breed_name,sex,neutd,case when '
            "b1.bcol is not null then b1.bcol else '' end||case when b2.bcol "
            "is not null then '-'||b2.bcol else '' end||case when b3.bcol is "
            "not null then '-'||b3.bcol else '' end,dob,dobest,vicious,rip "
            'from patients,breeds,colours,basecolours b1,basecolours b2,'
            'basecolours b3 where p_cid=%s and breed=breed_id and colour='
            'col_id and b1.bcol_id=col1 and b2.bcol_id=col2 and b3.bcol_id='
            'col3 order by p_name', (self.clid,))
        if result is None:  return # db error
        if not result:
            self.w.plist.append_row(
                [self.tr('No patients on this clients record')])
            self.w.plist.set_colwidth(0, self.w.plist.width())
            return
        pheader = map(self.tr,
                      ['Name', 'Breed', 'Sex', 'Colour', 'dob', 'vic', 'rip'])
        self.w.plist.set_headers(pheader)
        for res in result:
            self.w.plist.append_row([
                res[0],
                res[1] and res[2] + '-X' or res[2], # breed
                res[4]+(res[5] is None and '-n?' or res[5] and '-n' or ''), #sex
                res[6], # colour
                res[8] and '({})'.format(res[7].strftime('%d.%m.%y')) or
                res[7].strftime('%d.%m.%y'), # dob
                res[9] and 'v' or '',
                res[10] and 'rip' or ''])
            self.w.plist.cell(len(self.w.plist.lrows)-1, 2).setToolTip(res[3])
        self.w.plist.set_colwidth(0, 100)
        self.w.plist.set_colwidth(1, 100)
        self.w.plist.set_colwidth(2, 100)
        self.w.plist.set_colwidth(3, 200)
        self.w.plist.set_colwidth(4, 100)
        self.w.plist.set_colwidth(5, 50)
        self.w.plist.set_colwidth(6, 50)
        self.w.plist.setFocus()

    def gv_quit(self, quitnow=False):
        """Signal children if quitting GnuVet or not."""
        self.shutdown = quitnow
        self.gvquit.emit(quitnow)
        if quitnow:
            self.close()
    
    def gv_quitconfirm(self):
        if self.parent():
            self.parent().gv_quitconfirm()
        else:
            exit()
        
    def help_self(self):
        self.helpsig.emit('client.html')

    def merge(self):
        print('client.merge not yet implemented')

    def payment(self):
        print('client.payment not yet implemented')
        
    def rip(self):
        print('client.rip not yet implemented')

    def sale(self):
        print('client.sale not yet implemented')
        
if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    a = QApplication([])
    ding = Client(None, 2)
    ding.show()
    exit(a.exec_())
