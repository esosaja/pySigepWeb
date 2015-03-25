# -*- coding: utf-8 -*-

from base_xml import BaseXML


class CodigoServicoAdicional(BaseXML):

    def __init__(self, value=None):
        self.valor = value

    def xml(self):
        return '<codigo_servico_adicional>%s</codigo_servico_adicional>' % \
               self.valor


class ValorDeclarado(BaseXML):

    def xml(self):
        return '<valor_declarado>%s</valor_declarado>' % self.valor


class ServicoAdicional(BaseXML):

    def __init__(self):
        self.codigo_servico_adicional = []
        self.codigo_servico_adicional.append(CodigoServicoAdicional('025'))
        self.valor_declarado = '000000000,00'

    def xml(self):
        xml = '<servico_adicional>'
        for csa in self.codigo_servico_adicional:
            xml += csa.xml()
        xml += self.valor_declarado.xml()
        xml += '</servico_adicional>'
        return xml
