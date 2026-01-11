from models.ModelProduto import ModelProduto
from models.Produtos import Produto
import json
from abc import ABC, abstractmethod
import xml.etree.cElementTree as ET
from xml.dom import minidom

class ViewAPI(ABC):
    
    @abstractmethod
    def renderizar(self, dados):
        pass

    @abstractmethod
    def renderizar_erro(self, msg):
        pass

class ViewJSON(ViewAPI):

    def renderizar(self, dados):
        dados_json = None
        if isinstance(dados, list):
            dados_json = [item.to_dict() for item in dados]

        elif hasattr(dados, 'to_dict'):
            dados_json = dados.to_dict()

        else:
            dados_json = dados

        return json.dumps(dados_json)
    
    def renderizar_erro(self, mensagem: str) -> str:
        erro_dict = {
            "status": "erro",
            "mensagem": mensagem
        }

        return json.dumps(erro_dict)
    
class ViewXML(ViewAPI):

    def renderizar(self, dados):
        root = ET.Element('produtos')
        dados_dict = None

        if isinstance(dados, list):
            dados_dict = [item.to_dict() for item in dados]
        
        elif hasattr(dados, 'to_dict'):
            dados_dict = [dados.to_dict()]
        
        else:
            dados_dict = [dados]

        for item in dados_dict:
            produto = ET.SubElement(root, 'produto')
            for key, value in item.items():
                ET.SubElement(produto, key).text = str(value)

        return ET.tostring(root, encoding='unicode')
    
    def renderizar_erro(self, msg):
        root = ET.Element('erro')
        ET.SubElement(root, 'mensagem').text = str(msg)
        return ET.tostring(root, encoding='unicode')
    
