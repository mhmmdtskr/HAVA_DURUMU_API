from dataclasses import dataclass, field
from omegaconf import OmegaConf, DictConfig


@dataclass
class Configs:
    config: DictConfig

    @classmethod
    def getConfigs(cls, configs: dict):
        configs_ = OmegaConf.load(configs)
        return cls(configs_)
    
    @classmethod
    def createConfigWithFile(cls, path: str):
        configs = OmegaConf.load(path)
        return cls(configs)
