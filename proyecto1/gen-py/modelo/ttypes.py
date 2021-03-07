#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class Indicadores(object):
    talaArbol = 1
    talaArbol_volumenSalvado = 2
    talaArbol_neta = 3
    perdidasNaturales = 4
    incrementoBruto = 5
    incrementoNeto = 6
    cambioNeto = 7
    intensidadUso = 8

    _VALUES_TO_NAMES = {
        1: "talaArbol",
        2: "talaArbol_volumenSalvado",
        3: "talaArbol_neta",
        4: "perdidasNaturales",
        5: "incrementoBruto",
        6: "incrementoNeto",
        7: "cambioNeto",
        8: "intensidadUso",
    }

    _NAMES_TO_VALUES = {
        "talaArbol": 1,
        "talaArbol_volumenSalvado": 2,
        "talaArbol_neta": 3,
        "perdidasNaturales": 4,
        "incrementoBruto": 5,
        "incrementoNeto": 6,
        "cambioNeto": 7,
        "intensidadUso": 8,
    }


class Data(object):
    """
    Attributes:
     - pedigree
     - dataUnit

    """


    def __init__(self, pedigree=None, dataUnit=None,):
        self.pedigree = pedigree
        self.dataUnit = dataUnit

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.pedigree = Pedigree()
                    self.pedigree.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.dataUnit = DataUnit()
                    self.dataUnit.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Data')
        if self.pedigree is not None:
            oprot.writeFieldBegin('pedigree', TType.STRUCT, 1)
            self.pedigree.write(oprot)
            oprot.writeFieldEnd()
        if self.dataUnit is not None:
            oprot.writeFieldBegin('dataUnit', TType.STRUCT, 2)
            self.dataUnit.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.pedigree is None:
            raise TProtocolException(message='Required field pedigree is unset!')
        if self.dataUnit is None:
            raise TProtocolException(message='Required field dataUnit is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Pedigree(object):
    """
    Attributes:
     - true_as_of_secs

    """


    def __init__(self, true_as_of_secs=None,):
        self.true_as_of_secs = true_as_of_secs

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.true_as_of_secs = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Pedigree')
        if self.true_as_of_secs is not None:
            oprot.writeFieldBegin('true_as_of_secs', TType.I32, 1)
            oprot.writeI32(self.true_as_of_secs)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.true_as_of_secs is None:
            raise TProtocolException(message='Required field true_as_of_secs is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class DataUnit(object):
    """
    Attributes:
     - pais
     - indicadorRecursos
     - gasta

    """


    def __init__(self, pais=None, indicadorRecursos=None, gasta=None,):
        self.pais = pais
        self.indicadorRecursos = indicadorRecursos
        self.gasta = gasta

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.pais = Pais()
                    self.pais.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.indicadorRecursos = IndicadorRecursos()
                    self.indicadorRecursos.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.gasta = Gasta()
                    self.gasta.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('DataUnit')
        if self.pais is not None:
            oprot.writeFieldBegin('pais', TType.STRUCT, 1)
            self.pais.write(oprot)
            oprot.writeFieldEnd()
        if self.indicadorRecursos is not None:
            oprot.writeFieldBegin('indicadorRecursos', TType.STRUCT, 2)
            self.indicadorRecursos.write(oprot)
            oprot.writeFieldEnd()
        if self.gasta is not None:
            oprot.writeFieldBegin('gasta', TType.STRUCT, 3)
            self.gasta.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Pais(object):
    """
    Attributes:
     - nombrePais

    """


    def __init__(self, nombrePais=None,):
        self.nombrePais = nombrePais

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.nombrePais = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Pais')
        if self.nombrePais is not None:
            oprot.writeFieldBegin('nombrePais', TType.STRING, 1)
            oprot.writeString(self.nombrePais.encode('utf-8') if sys.version_info[0] == 2 else self.nombrePais)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.nombrePais is None:
            raise TProtocolException(message='Required field nombrePais is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class IndicadorRecursos(object):
    """
    Attributes:
     - nombreIndicador
     - valorIndicador

    """


    def __init__(self, nombreIndicador=None, valorIndicador=None,):
        self.nombreIndicador = nombreIndicador
        self.valorIndicador = valorIndicador

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.nombreIndicador = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.valorIndicador = ValorIndicador()
                    self.valorIndicador.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('IndicadorRecursos')
        if self.nombreIndicador is not None:
            oprot.writeFieldBegin('nombreIndicador', TType.I32, 1)
            oprot.writeI32(self.nombreIndicador)
            oprot.writeFieldEnd()
        if self.valorIndicador is not None:
            oprot.writeFieldBegin('valorIndicador', TType.STRUCT, 2)
            self.valorIndicador.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.nombreIndicador is None:
            raise TProtocolException(message='Required field nombreIndicador is unset!')
        if self.valorIndicador is None:
            raise TProtocolException(message='Required field valorIndicador is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ValorIndicador(object):
    """
    Attributes:
     - indicadorInt
     - indicadorDouble

    """


    def __init__(self, indicadorInt=None, indicadorDouble=None,):
        self.indicadorInt = indicadorInt
        self.indicadorDouble = indicadorDouble

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.indicadorInt = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.indicadorDouble = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ValorIndicador')
        if self.indicadorInt is not None:
            oprot.writeFieldBegin('indicadorInt', TType.I32, 1)
            oprot.writeI32(self.indicadorInt)
            oprot.writeFieldEnd()
        if self.indicadorDouble is not None:
            oprot.writeFieldBegin('indicadorDouble', TType.DOUBLE, 2)
            oprot.writeDouble(self.indicadorDouble)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Gasta(object):
    """
    Attributes:
     - nombrePais
     - nombreIndicador
     - nonce

    """


    def __init__(self, nombrePais=None, nombreIndicador=None, nonce=None,):
        self.nombrePais = nombrePais
        self.nombreIndicador = nombreIndicador
        self.nonce = nonce

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.nombrePais = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.nombreIndicador = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.nonce = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Gasta')
        if self.nombrePais is not None:
            oprot.writeFieldBegin('nombrePais', TType.STRING, 1)
            oprot.writeString(self.nombrePais.encode('utf-8') if sys.version_info[0] == 2 else self.nombrePais)
            oprot.writeFieldEnd()
        if self.nombreIndicador is not None:
            oprot.writeFieldBegin('nombreIndicador', TType.STRING, 2)
            oprot.writeString(self.nombreIndicador.encode('utf-8') if sys.version_info[0] == 2 else self.nombreIndicador)
            oprot.writeFieldEnd()
        if self.nonce is not None:
            oprot.writeFieldBegin('nonce', TType.I64, 3)
            oprot.writeI64(self.nonce)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.nombrePais is None:
            raise TProtocolException(message='Required field nombrePais is unset!')
        if self.nombreIndicador is None:
            raise TProtocolException(message='Required field nombreIndicador is unset!')
        if self.nonce is None:
            raise TProtocolException(message='Required field nonce is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Data)
Data.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'pedigree', [Pedigree, None], None, ),  # 1
    (2, TType.STRUCT, 'dataUnit', [DataUnit, None], None, ),  # 2
)
all_structs.append(Pedigree)
Pedigree.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'true_as_of_secs', None, None, ),  # 1
)
all_structs.append(DataUnit)
DataUnit.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'pais', [Pais, None], None, ),  # 1
    (2, TType.STRUCT, 'indicadorRecursos', [IndicadorRecursos, None], None, ),  # 2
    (3, TType.STRUCT, 'gasta', [Gasta, None], None, ),  # 3
)
all_structs.append(Pais)
Pais.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'nombrePais', 'UTF8', None, ),  # 1
)
all_structs.append(IndicadorRecursos)
IndicadorRecursos.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'nombreIndicador', None, None, ),  # 1
    (2, TType.STRUCT, 'valorIndicador', [ValorIndicador, None], None, ),  # 2
)
all_structs.append(ValorIndicador)
ValorIndicador.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'indicadorInt', None, None, ),  # 1
    (2, TType.DOUBLE, 'indicadorDouble', None, None, ),  # 2
)
all_structs.append(Gasta)
Gasta.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'nombrePais', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'nombreIndicador', 'UTF8', None, ),  # 2
    (3, TType.I64, 'nonce', None, None, ),  # 3
)
fix_spec(all_structs)
del all_structs