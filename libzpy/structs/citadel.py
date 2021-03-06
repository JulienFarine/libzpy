from libzpy.libs.structure import DataStructure,StructList
from libzpy.libs.structure import c_word,c_dword,c_byte
import libzpy.structs.zeus as zeus

class Header(DataStructure):
    _have_data=False
    _fields_ = [ ('junk',c_byte*12), ('size',c_dword), ('flags',c_dword), ('count',c_dword),('md5',c_byte*0x10)]


class Item(zeus.Item):

    def __init__(self,*args,**kwargs):
        super(Item,self).__init__(*args,**kwargs)
        self._flags['ITEMF_IS_ARGUMENT']       =  0x00100000
        self._flags['ITEMF_IS_MODULE_HASH']    =  0x00200000
        self._flags['ITEMF_IS_PROC_NAME_HASH'] =  0x00400000
        self._cfgids[20009] ='CFGID_DNS_FILTER'
        self._cfgids[20010] ='CFGID_CMD_LIST'
        self._cfgids[20011] ='CFGID_HTTP_MAGICURI_LIST'
        self._cfgids[20012] ='CFGID_FILESEARCH_KEYWORDS'
        self._cfgids[20013] ='CFGID_FILESEARCH_EXCLUDES_NAME'
        self._cfgids[20014] ='CFGID_FILESEARCH_EXCLUDES_PATH'
        self._cfgids[20015] ='CFGID_KEYLOGGER_PROCESSES'
        self._cfgids[20016] ='CFGID_KEYLOGGER_TIME'
        self._cfgids[20017] ='CFGID_FILESEARCH_MINYEAR'
        self._cfgids[20018] ='CFGID_WEBINJECTS_URL'
        self._cfgids[20019] ='CFGID_TOKENSPY_URL'
        self._cfgids[20020] ='CFGID_HTTPVIP_URLS'
        self._cfgids[20101] ='CFGID_VIDEO_QUALITY'
        self._cfgids[20102] ='CFGID_VIDEO_LENGTH'
        self._cfgids[20201] ='CFGID_MONEY_PARSER_ENABLED'
        self._cfgids[20202] ='CFGID_MONEY_PARSER_INCLUDE'
        self._cfgids[20203] ='CFGID_MONEY_PARSER_EXCLUDE'

        self._cfgids_n = self._cfgids.__class__(map(reversed, self._cfgids.items()))


    def is_captchasrv(self):
        return self.id == self._cfgids_n['CFGID_CAPTCHA_SERVER']

    def is_captchalist(self):
        return self.id == self._cfgids_n['CFGID_CAPTCHA_LIST']
    def is_notifysrv(self):
        return self.id == self._cfgids_n['CFGID_NOTIFY_SERVER']

    def is_notifylist(self):
        return self.id == self._cfgids_n['CFGID_NOTIFY_LIST']

_http_inj_flags = {
    'FLAG_IS_INJECT'                : 0x0001, 
    'FLAG_IS_CAPTURE'               : 0x0002, 
    'FLAG_REQUEST_POST'             : 0x0004,
    'FLAG_REQUEST_GET'              : 0x0008,
    'FLAG_ONCE_PER_DAY'             : 0x0010, 
    'FLAG_CAPTURE_NOTPARSE'         : 0x0100, 
    'FLAG_CAPTURE_TOFILE'           : 0x0200, 
    'FLAG_URL_CASE_INSENSITIVE'     : 0x1000, 
    'FLAG_CONTEXT_CASE_INSENSITIVE' : 0x2000 
}
class HttpInject_InjectBlock(zeus.HttpInject_InjectBlock):
    _flags = _http_inj_flags

class HttpInject_Header(DataStructure):
    _pack_ = 1
    _fields_ = [('flags',c_word),('size',c_word),('urlMask',c_word),
                ('postDataBlackMask',c_word),('postDataWhiteMask',c_word),
                ('contextMask',c_word)
                ]
    _flags = _http_inj_flags 

    def is_inject(self):
        return self.flags & self._flags['FLAG_IS_INJECT']
    def is_capture(self):
        return self.flags & self._flags['FLAG_IS_CAPTURE']

class HttpInject_HList(zeus.HttpInject_HList):
    struct = HttpInject_Header

class HttpInject_BList(zeus.HttpInject_BList):
    pass

class HttpInject_Captcha(DataStructure):
    _fields_ = [('size',c_word),('urlHostMask',c_word),('urlCaptcha',c_word)]


class WebFilter(zeus.WebFilter):
    def __init__(self,*args,**kwargs):
        super(WebFilter,self).__init__(*args,**kwargs)
        self._wf['#'] = 'MOVIE'
