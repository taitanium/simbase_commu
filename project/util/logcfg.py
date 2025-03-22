""" 日志和配置文件加载 """

from loguru import logger
import os,shutil,yaml

from tools import timeSeq,path_combine_relavabs
from config import cfg

class logcfg:
    '''日志和配置文件加载'''
    def __init__(self,config_path:str='./config/config.yaml') -> None:

        # 全局配置部分
        self.conf = {} #设置项字典
        self.cfg_dir = config_path #当前加载配置的位置
        self.cur_work_dir = os.getcwd() #当前工作目录
        self._loadConfigfile_(config_path)

        # 日志部分
        assert self.conf['log_dir'] is not None,"invaid basic configs"

        self.logenable = self.conf['log_enable']

        if self.logenable:
            self._log_folder_init()
            self.loggerOutId = logger.add(path_combine_relavabs(self.logfolder_dir,"./record.log"), rotation="10 MB")
            # 保存配置文件
            self._save_cur_config()
            self._init_log_funcs()            
    def loadConfig(self,cfg_dir:str):
        '''加载配置文件
           可以递归地进行加载 在配置文件内可以使用`_base_`指定其他配置文件
        '''
        self._loadConfigfile_(cfg_dir)
    
    def _loadConfigfile_(self,cfg_dir:str):
        with open(cfg_dir) as f:
            conf0:dict = yaml.load(f, Loader=yaml.FullLoader)
        
        if '_base_' in conf0.keys():
            # 递归加载
            for one_base in conf0['_base_']:
                self._loadConfigfile_(path_combine_relavabs(self.cur_work_dir,one_base))
            # 加载进全局conf
            conf0.pop('_base_')
        self.conf = {**self.conf,**conf0}

    def _log_folder_init(self)-> None:
        '''日志记录文件夹创建'''
        # 文件名
        folder_name = f"log{timeSeq()}_{self.conf['log_folder_postfix_arr'][self.conf['log_proj_mode']]}"
        log_out_folder = self.conf['log_dir']
        # 创建
        self.logfolder_dir = path_combine_relavabs(log_out_folder,f"./{folder_name}")
        os.mkdir(self.logfolder_dir)
    
    def _save_cur_config(self)->None:
        '''保存当前配置'''
        with open(path_combine_relavabs(self.logfolder_dir,"./cur_config.yaml"),'w') as f:
            yaml.dump(self.conf,f)
    
    def _init_log_funcs(self)->None:
        #日志记录函数
        self.info = logger.info
        self.success = logger.success
        self.debug = logger.debug
        self.trace = logger.trace
        self.warning = logger.warning
        self.critical = logger.critical
        self.error = logger.error
    
if __name__ == "__main__":
    lc = logcfg(r"D:\jorn\marls\simbase_commu\configs\frame_test\basic.yaml")
