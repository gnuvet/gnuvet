#!/usr/bin/python
"""The GnuVet main program."""
# TODO:
# reorganise db_state thing:  If db dont work set db None (or so)
# special search (medication, clin hist)
# g|setattr(self, cp) won't work: w_cli -- well don't see why: test
# adapt knowledge to login|gv_auth()
# gvdir reconsider: for startup other than login # ???
# Reconsider switchoff things with db loss
# Add group/institution in payment -- for TGD|Racetrack etc.

from sys import argv, platform, stderr
from os import path as os_path
from getopt import gnu_getopt, GetoptError
from datetime import date
from PyQt4.QtGui import (QMainWindow, QLabel, QFont, QAction, QApplication)
from PyQt4.QtCore import pyqtSignal
from util import querydb

import dbmod
import gv_qrc
import gv_version
from keycheck import Keycheck
from main_ui import Ui_Mainform

class Gnuv_MainWin(QMainWindow):
    """The GnuVet Main Window."""
    # signals
    gvquit = pyqtSignal(bool)
    dbstate  = pyqtSignal(object)
    ##helpsig  = pyqtSignal(str) ?
    # addcli       = pyqtSignal(tuple)
    # addedcli     = pyqtSignal(tuple)
    # patid        = pyqtSignal(int)

    # instance vars
    db        = None
    origin      = 'origin'
    user      = None  # are we authenticated?
    x_pos, y_pos = 100, 50

    def __init__(self, options={}):
        super(Gnuv_MainWin, self).__init__(None)
        self.w = Ui_Mainform()
        self.w.setupUi(self)
        self.options = options
        self.offspring = []    # visible children for gv_quitconfirm
        self.w.yesPb.clicked.connect(self.gv_exit)
        self.w.noPb.clicked.connect(self.gv_quitno)
        #    ACTIONS
        # devel:
        debugA = QAction(self)
        debugA.setAutoRepeat(False)
        debugA.setShortcut('Ctrl+D')
        self.addAction(debugA)
        debugA.triggered.connect(self.debugf)
        # end devel
        self.dbA = QAction(self.tr('&Reconnect to db'), self)
        self.dbA.setAutoRepeat(0) # default autoRepeat is True!
        self.dbA.setStatusTip(self.tr('Try to reconnect to database'))
        self.dbA.setShortcut(self.tr('Ctrl+R'))
        self.patA = QAction(self.tr('&Patients'), self)
        self.patA.setAutoRepeat(0)
        self.patA.setStatusTip(self.tr('Search for Patients'))
        self.patA.setShortcut(self.tr('Ctrl+P'))
        self.cliA = QAction(self.tr('&Clients'), self)
        self.cliA.setAutoRepeat(0)
        self.cliA.setShortcut(self.tr('Ctrl+C'))
        self.cliA.setStatusTip(self.tr('Search for Clients'))
        self.vaccremA = QAction(self.tr('&Vacc. Reminders'), self)
        self.vaccremA.setAutoRepeat(0)
        self.vaccremA.setShortcut(self.tr('Ctrl+V'))
        self.vaccremA.setStatusTip(self.tr('Check vacc. reminders'))
        self.ssearchA = QAction(self.tr('&Special Search'), self)
        self.ssearchA.setAutoRepeat(0)
        self.ssearchA.setShortcut(self.tr('Ctrl+S'))
        self.ssearchA.setStatusTip(
            self.tr('Search in medication/clinical history/seen date etc.'))
        self.appointA = QAction(self.tr('&Appointments'), self)
        self.appointA.setAutoRepeat(0)
        self.appointA.setShortcut(self.tr('Ctrl+A'))
        self.appointA.setStatusTip(self.tr('Open appointment diary'))
        #    ETC.PP.:
        # ordA jouA finA medA srvA sysA stkA
        chuserA = QAction(self.tr('Change &User'), self)
        chuserA.setAutoRepeat(0)
        chuserA.setShortcut(self.tr('Ctrl+U'))
        chuserA.setStatusTip(self.tr('Login as different user'))
        quitA = QAction(self.tr('&Quit'), self)
        quitA.setAutoRepeat(0)
        quitA.setShortcut(self.tr('Ctrl+Q'))
        quitA.setStatusTip(self.tr('Exit GnuVet'))
        helpA = QAction(self.tr('&Help'), self)
        helpA.setAutoRepeat(0)
        helpA.setShortcut('F1')
        helpA.setStatusTip(self.tr('context sensitive Help'))
        aboutA = QAction(self.tr('About &GnuVet'), self)
        aboutA.setAutoRepeat(0)
        aboutA.setStatusTip(self.tr('GnuVet version information'))
        #    MENUS
        self.w.taskM.addAction(self.dbA)
        self.w.taskM.addSeparator()
        self.w.taskM.addAction(self.patA)
        self.w.taskM.addAction(self.cliA)
        self.w.taskM.addSeparator()
        self.w.taskM.addAction(self.appointA)
        self.w.taskM.addAction(self.vaccremA)
        # ordA Sep jouA finA
        self.w.taskM.addSeparator()
        self.w.taskM.addAction(self.ssearchA)
        self.w.taskM.addSeparator()
        self.w.taskM.addAction(chuserA)
        self.w.taskM.addAction(quitA)
        self.w.taskM.setSeparatorsCollapsible(1)
        # maintM: medA srvA sysA stkA userA
        self.w.helpM.addAction(helpA)
        self.w.helpM.addSeparator()
        self.w.helpM.addAction(aboutA)
        #    CONNECTIONS
        self.dbA.triggered.connect(self.db_reconnect)
        self.patA.triggered.connect(self.sae_patact)
        self.cliA.triggered.connect(self.sae_cliact)
        self.vaccremA.triggered.connect(self.vacc_reminders)
        self.appointA.triggered.connect(self.openapp)
        # self.appointA ordA jouA finA medA srvA sysA stkA
        chuserA.triggered.connect(self.chuser)
        quitA.triggered.connect(self.gv_quitconfirm)
        helpA.triggered.connect(self.gv_helpmain)
        aboutA.triggered.connect(self.about)
        self.keycheck = Keycheck(self)
        self.installEventFilter(self.keycheck)
        # login:
        #self.gv_authq()
        # devel
        self.user = 'enno'
        self.staffid = 1
        self.db_connect(self.user)
        if self.db: # hierwei, gvdir_check ghört weiter rauf glaubich
            self.w.lLb.setText(self.user)
            self.gvdir_check()
        if not(hasattr(self, 'warning') and self.warning.isVisible()):
            self.show()
        # end devel

    def about(self):
        """Launch 'About' window: quite useless but common."""
        if hasattr(self, 'aboutw'):
            self.aboutw.show()
        else:
            import gv_about
            lang = ('lang' in self.options and self.options['lang'] or 'en')
            self.aboutw = gv_about.About(self, lang)

    def chuser(self):
        """Login as different user, closing all open windows but main."""
        if self.db and not isinstance(self.db, str):
            if hasattr(self.db, 'close'):
                self.db.close()
        for window in self.findChildren(QMainWindow):
            window.close()
        self.user = None
        self.passwd = None
        self.w.lLb.setText(self.tr('no login'))
        self.w.no_dbconn.show()
        self.gv_authq()

    def closeEvent(self, event):
        event.ignore()
        self.gv_quitconfirm()

    def db_connect(self, user=None, passwd=None, dbhost=None):
        args = {}
        if user:
            args['user'] = user
            self.user = user
        if passwd:
            args['passwd'] = passwd
        if dbhost:
            args['host'] = dbhost
        self.dbh = dbmod.Db_handler(**args)
        ## # devel:
        ## self.user = user
        ## self.passwd = passwd
        ## self.dbhost = dbhost
        ## # end devel
        self.db = self.dbh.db_connect()
        if not self.db or isinstance(self.db, str):
            self.db_state(self.db)
            return
        self.user = user
        self.passwd = passwd
        self.dbhost = dbhost
        self.dbdep_enable()
        self.curs = self.db.cursor()
        try:
            res = querydb(
                self,
                'select stf_func,stf_id from staff where stf_logname=%s',
                (user,))
            if res is None:  return # db error hierwei check db_state!
            res = self.curs.fetchall()
        except (OperationalError, AttributeError):
            self.db_state(self.db)
            return
        if not res:
            return
        for p in res:
            self.staffrole = p[0]
            # devel:
            #self.staffid = p[1]

    def db_reconnect(self):
        """Try reconnecting to db."""
        args = {}
        if self.user:
            args['user'] = self.user
        if self.passwd:
            args['passwd'] = self.passwd
        if self.dbhost:
            args['host'] = self.dbhost
        self.dbh = dbmod.Db_handler(**args)
        self.db = self.dbh.db_connect()
        if not self.db or isinstance(self.db, str):
            return
        self.dbdep_enable()
        self.curs = self.db.cursor()
        self.dbstate.emit(self.db)

    def db_state(self, msg=''):
        """Actions to be taken on db loss or gain."""
        dberr = msg and True or False
        if dberr:
            self.db = None
        self.w.no_dbconn.setVisible(dberr)
        self.dbdep_enable(not dberr)
        if not hasattr(self, 'warnw'):
            from warn import Warning
        if not msg:
            msg = self.tr('Unspecified db error.')
        self.warnw = Warning(self, self.tr('GnuVet: Db Error'), msg)
        if not self.isVisible():
            self.warnw.closed.connect(self.show)
        self.w.statusbar.clearMessage()
    
    def dbdep_enable(self, yes=True):
        """En- or disable db dependent features, signal children of db state."""
        self.patA.setEnabled(yes)
        self.cliA.setEnabled(yes)
        self.ssearchA.setEnabled(yes)
        self.appointA.setEnabled(yes)
        # ordA jouA finA medA srvA sysA stkA
        self.w.maintM.setEnabled(yes)
        self.dbA.setVisible(not yes)
        self.dbA.setEnabled(not yes)
        if yes:
            self.w.statusbar.showMessage(self.tr('Ready ...'), 10000)
        self.w.no_dbconn.setVisible(not yes)

    def debugf(self): #hierwei spaetestens
        pass

    def gvdir(self): # hierwei, s. util.py re win32
        """Return name of working dir."""
        # win: (winApiPath, 'gnuvet')
        # mac: (homePath, 'Library/Preferences/gnuvet')
        # *nx: ('/usr/share/gnuvet' or '~' + /.gnuvet)
        if not 'sysinfo' in locals():
            from util import sysinfo
        self.syspath, self.userdir, self.optfile = sysinfo()
        if self.staffid == 1:
            return self.syspath
        else:
            home = '~' + self.user
            if os_path.expanduser(home) != home:
                return os_path.join(os_path.expanduser(home), self.userdir)
            else: # no such user on system
                return self.syspath

    def gvdir_check(self):
        """Check working dir (at startup), create if necessary."""
        gvdir = self.gvdir()
        if not 'os_access' in locals():
            from os import access as os_access
        if not os_path.exists(gvdir):
            if not 'os_mkdir' in locals():
                from os import mkdir as os_mkdir
            try:
                os_mkdir(gvdir)
            except OSError:
                stderr.write('Couldn\'t create dir "{}"\n'.format(gvdir))
                exit(13)
        elif not os_path.isdir(gvdir):
            if not 'os_rename' in locals():
                from os import rename as os_rename
            try:
                os_rename(gvdir, gvdir + '.bak')
                stderr.write('WARN: renamed existing file "{0}" to '
                             '"{0}.bak"\n'.format(gvdir))
            except OSError:
                stderr.write('Couldn\'t rename "{0}" to "{0}.bak"\n'.
                             format(gvdir))
                exit(13)
            if not 'os_mkdir' in locals():
                from os import mkdir as os_mkdir
            try:
                os_mkdir(gvdir)
            except OSError:
                stderr.write('Couldn\'t create dir "{}"!\n'.format(gvdir))
                exit(13)
        elif not os_access(gvdir, 7):
            stderr.write('WARN: Directory "{}" is not writeable!\n'.
                         format(gvdir))
            exit(13)

    def gv_auth(self):
        """Try connecting to db with given user and pass."""
        user = str(self.w.logname.text().toLatin1())
        passwd = str(self.w.logpass.text().toLatin1())
        self.w.logname.setText('')
        self.w.logpass.setText('')
        self.w.logname.setFocus()
        dbhost = 'dbnost' in self.options and self.options['dbhost'] or None
        self.db_connect(user, passwd, dbhost)
        if not self.db or isinstance(self.db, str):
            self.w.statusbar.showMessage(self.tr('Login incorrect'), 20000)
        else:
            self.w.lFr.setEnabled(0)
            self.w.lFr.hide()
            self.w.lLb.setText(user)
            self.w.logokPb.clicked.disconnect(self.gv_auth)
            self.optread(user)
            self.savedread()
            self.user = user
            self.passwd = passwd
            self.dbhost = dbhost

    def gv_authq(self):
        """Show login frame."""
        self.w.lFr.setEnabled(1)
        self.w.lFr.show()
        self.w.logokPb.clicked.connect(self.gv_auth)
        self.w.logokPb.setDefault(1)
        self.keycheck.enter.connect(self.w.logokPb.click)
        
    def gv_exit(self):
        """Say goodbye, dignified, signal offspring to save unsaved changes."""
        if self.db and not isinstance(self.db, str):
            self.dbh.db_close()
        self.gvquit.emit(True)
        #print self.tr('Thank You for using GnuVet.')
        exit()

    def gv_help(self, help_doc='toc.html'):
        """Launch help window and display help_doc."""
        if hasattr(self, 'helpw'):
            self.helpw.show()
            self.helpw.raise_()
            self.helpw.show_help(help_doc)
        else:
            if not 'gv_help' in locals():
                import gv_help
            self.helpw = gv_help.Help(self, help_doc)

    def gv_helpmain(self):
        """Launch help window and display mainform.html"""
        if hasattr(self, 'helpw'):
            self.helpw.show()
            self.helpw.raise_()
            self.helpw.show_help('mainform.html')
        else:
            if not 'gv_help' in locals():
                import gv_help
            self.helpw = gv_help.Help(self, 'mainform.html')

    def gv_quitconfirm(self):
        """Ask for confirmation to quit GnuVet."""
        self.w.menubar.setEnabled(0)
        self.w.gnuLb.hide()
        self.w.lFr.hide()
        self.w.lFr.setEnabled(0)
        self.w.no_dbconn.hide()
        self.w.qFr.setEnabled(1)
        self.w.qFr.show()
        for window in self.findChildren(QMainWindow):
            if window.isVisible():
                self.offspring.append(window)
        for window in self.offspring:
            window.hide()
        if not self.isVisible():
            self.show()

    def gv_quitno(self):
        """Oops, no, don't quit!"""
        self.gvquit.emit(False)
        self.w.qFr.setEnabled(0)
        self.w.qFr.hide()
        self.w.gnuLb.show()
        if not self.db or isinstance(self.db, str):
            self.w.no_dbconn.show()
        self.w.menubar.setEnabled(1)
        for window in self.offspring:
            window.show()
        self.offspring = []

    def name_newwin(self, name='w', cnt=None):
        """Return unique name for a new window."""
        if not cnt:
            cnt = ('maxwinnum' in self.options and
                   self.options['maxwinnum'] or 3)
        startname = name[:]
        for i in xrange(cnt):
            if not hasattr(self, name+str(i+1)):
                name = name + str(i+1)
                break
            else:
                continue
        if name != startname:
            return name
        return None

    def openapp(self):
        """Open appointment diary."""
        if not self.today:
            self.today = date.today()
        if not hasattr(self, 'appointw'):
            from appoint import Appointer
            self.appointw = Appointer(self, self.today)
        else:
            self.appointw.raise_()
        self.appointw.show()
        
    def opencli(self, cid=0):
        """Launch Client window."""
        errmsg = self.dbh.db_check(self.curs)
        if errmsg:
            self.db_state(errmsg)
            return
        wc = 'wc{}'.format(cid)
        if hasattr(self, wc):
            self.wc.show()
            self.wc.raise_()
            return
        else:
            import client
            self.wc = client.Client(self, cid)
            self.xy_incr(self.wc)
        self.wc.show()

    def openfin(self):
        """Finalysis "dialog"."""
        pass

    def openjou(self):
        """Journal "dialog"."""
        # journals are just summaries of monies per time
        pass

    def openord(self):
        """Order "dialog"."""
        pass

    def openpat(self, pid=0):
        """Launch Patient window -- ids signalled from saepat."""
        errmsg = self.dbh.db_check(self.curs)
        if errmsg:
            self.db_state(errmsg)
            return
        wp = 'wp{}'.format(pid)
        if hasattr(self, wp):
            self.wp.show()
            self.wp.raise_()
            return
        else:
            import patient
            self.wp = patient.Patient(self, pid)
            self.xy_incr(self.wp)
            self.wp.show()

    def opensys(self):
        """System "dialog"."""
        pass

    def optread(self, user=None):
        """Read (optional) options file for customised settings."""
        if not 'read_options' in locals():
            from options import read_options
        self.options.update(read_options(user))

    def optwrite(self, userfile=''):
        """Write customised settings to user file."""
        # hierwei: implement
        if not 'write_options' in locals():
            from options import write_options
        pass

    def sae_cliact(self, trg=0): # triggered(checked=False) hierwei
        """Wrapper for action signal."""
        self.sae_cli()
        
    def sae_cli(self, cid=0, act='s'):
        """Open Search-Add-Edit Client window."""
        errmsg = self.dbh.db_check(self.curs)
        if errmsg:
            self.db_state(errmsg)
            return
        cp = self.name_newwin('saecliw')
        if not cp:
            self.w.statusbar.showMessage(self.tr(
                'Open client windows maximum count reached.'), 10000)
            return
        if not 'Saecli' in locals():
            from saecli import Saecli
        setattr(self, cp, Saecli(self, act, cid))
        self.xy_incr(getattr(self, cp))
        getattr(self, cp).show()

    def sae_patact(self, trg=0): # triggered(checked=False)
        """Wrapper for action signal."""
        self.sae_pat()
        
    def sae_pat(self, patid=0, act='s'):
        """Search-Add-Edit Patient window."""
        errmsg = self.dbh.db_check(self.curs)
        if errmsg:
            self.db_state(errmsg)
            return
        sp = self.name_newwin('saepatw')
        if not sp:
            self.w.statusbar.showMessage(self.tr(
                'Open patient windows maximum count reached.'), 10000)
            return
        if not 'Saepat' in locals():
            from saepat import Saepat
        setattr(self, sp, Saepat(self, act, patid))
        self.xy_incr(getattr(self, sp))
        getattr(self, sp).show()
            
    def sae_med(self):
        """Search-Add-Edit Medication window."""
        pass

    def sae_srv(self):
        """Search-Add-Edit Service window."""
        pass

    def sae_stk(self):
        """Search-Add-Edit Stock window."""
        pass

    def savedread(self):
        """Read optional savedstate file on startup."""
        gvdir = self.gvdir()
        if os_path.exists(gvdir + 'savestate'):
            pass # for now

    def state_restore(self):
        """Restore pre-crash state."""
        pass

    def vacc_reminders(self):
        """Prepare printing of vacc reminder letters."""
        today = date.today()
        res = querydb(
            self,
            'select vd_pid,vt_type from vdues,vtypes,patients where vt_id='
            'vd_type and vd_pid=p_id and not rip and vd_due<%s', (today,))
        if res is None:  return # db error
        pats = []
        types = []
        for e in res:
            pats.append(e[0])
            types.append(e[1])
        # hierwei: dict?
        
    def state_write(self, save_things=[]):
        """Write unsaved changes to file for later restoration."""
        # hierwei
        if hasattr(self, 'warning'):
            try:
                self.warning.closed.disconnect(self.show)
            except TypeError:
                pass
        self.gvdir_check()
        sfile = os_path.join(self.gvdir(), 'savestate')
        try:
            f = open(sfile, 'w')
            f.write('\n'.join(save_things))
            f.close()
        except IOError:
            if not hasattr(self, 'warning'):
                from warn import Warning
        self.warning = Warning(self, self.tr('GnuVet: Warning'), 
                               self.tr("Couldn't save unsaved Changes!"))
        self.warning.setWindowModality(2) # be top of w-tree
        #self.warning.show()

    def xy_decr(self):
        """Adjust position for new child window -- after closing another one.
        Called from children's closeEvent."""
        if self.x_pos > 25: # was 114:
            self.x_pos -= 25
        if self.y_pos > 20: # was 69:
            self.y_pos -= 20

    def xy_incr(self, child):
        """Move child window and increase x and y for next window."""
        child.move(self.x_pos, self.y_pos)
        self.x_pos += 25
        self.y_pos += 20

# ==================================================

def main():
    shopts = 'hV'
    lopts  = ['help', 'version']
    from options import read_options
    options = read_options()
    lang = 'lang' in options and options['lang'] or 'en'
    try:
        opts, args = gnu_getopt(argv[1:], shopts, lopts)
    except GetoptError as err:
        print(str(err))
        print(gv_version.help[lang])
        exit(2)
    ex = False
    for o, p in opts:
        if o in ('-h', '--help'):
            print(gv_version.help[lang])
            ex = True
        if o in ('-V', '--version'):
            print(gv_version.version)
            print(gv_version.copyleft[lang].format('\n'))
            ex = True
    if ex:
        exit(2)
    mw = Gnuv_MainWin(options)
    exit(a.exec_())

if __name__ == '__main__':
    a = QApplication(argv)
    a.setStyle('plastique')
    main()
