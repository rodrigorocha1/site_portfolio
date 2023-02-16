from abc import ABC, abstractmethod


class Pagina(ABC):

    @abstractmethod
    def gerar_pagina(self):
        pass
