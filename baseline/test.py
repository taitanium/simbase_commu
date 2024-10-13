import sys,os
sys.path.append("E:\BITer\jorn\stage3\simBase_commu")

from project.util.config import cfg
from project.util.logger import inLogg

if __name__ == "__main__":
    cfgs = cfg()
    inlogs = inLogg(cfgs)