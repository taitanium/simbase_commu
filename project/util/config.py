import yaml

class cfg:
    '''配置文件加载与解析'''
    def __init__(self,cfg_dir:str=r"E:\BITer\jorn\stage3\simBase_commu\configs\basic.yaml") -> None:
        self.conf = None #设置项字典
        self.cfg_dir = cfg_dir #当前加载配置的位置
        self.loadConfig(cfg_dir)

    def loadConfig(self,cfg_dir:str):
        '''load conf yaml files'''
        with open(cfg_dir) as f:
            self.conf = yaml.load(f, Loader=yaml.FullLoader)

if __name__ == "__main__":
    cfgs = cfg()
    print(cfgs.conf)
