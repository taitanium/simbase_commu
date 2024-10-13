from loguru import logger
import os,shutil

from tools import timeSeq,path_combine_relavabs
from config import cfg
from torch.utils.tensorboard import SummaryWriter

class inLogg:
    '''日志记录 wrapped loguru 与调试相关数据存储'''
    def __init__(self,cfg:cfg) -> None:
        self.cfgs = cfg.conf

        #日志开关选项
        self.logenable = self.cfgs['log_enable']

        if(self.logenable):
            self._log_folder_init()
            self.loggerOutId = logger.add(path_combine_relavabs(self.logfolder_dir,"./record.log"), rotation="10 MB")
            #无记录的话 只会在控制台输出而无文件写入
            self._copy_cfg_save(cfg.cfg_dir)

        #日志记录函数
        self.info = logger.info
        self.success = logger.success
        self.debug = logger.debug
        self.trace = logger.trace
        self.warning = logger.warning
        self.critical = logger.critical
        self.error = logger.error

        logger.info("internal logger init Done!")

        self.writer = None
            # self.writer = SummaryWriter(log_dir=cfg.conf['log_dir']+"/tboard")
    
    def _log_folder_init(self)-> None:
        '''日志记录文件夹创建'''
        folder_name = f"log{timeSeq()}_{self.cfgs['log_folder_postfix_arr'][self.cfgs['log_proj_mode']]}"
        self.logfolder_dir = path_combine_relavabs(self.cfgs['log_dir'],f"./{folder_name}")
        os.mkdir(self.logfolder_dir)

    def _copy_cfg_save(self,org:str)->None:
        '''复制当前设置文件到日志文件夹备份'''
        shutil.copyfile(org,path_combine_relavabs(self.logfolder_dir,f"./curConfig.yaml"))

  
if __name__ == "__main__":
    cfgs = cfg()
    inlogs = inLogg(cfgs)

