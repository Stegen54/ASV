from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint, create_engine, Column, String, Integer, Numeric, Text, CHAR, VARCHAR, BigInteger, Index
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
db = SQLAlchemy()


class MRCOLS(db.Model):
    __tablename__ = 'MRCOLS'
    COL = Column(VARCHAR(40),primary_key=True)
    DES = Column(VARCHAR(200))
    REF = Column(VARCHAR(40))
    MIN = Column(INTEGER)
    AV = Column(Numeric(5, 2))
    MAX = Column(INTEGER)
    FIL = Column(VARCHAR(50))
    DTY = Column(VARCHAR(40))


class MRCONSO(db.Model):
    __tablename__ = 'MRCONSO'
    CUI = Column(CHAR(8), primary_key=True)
    LAT = Column(CHAR(3), primary_key=True)
    TS = Column(CHAR(1), primary_key=True)
    LUI = Column(VARCHAR(10), primary_key=True)
    STT = Column(VARCHAR(3), primary_key=True)
    SUI = Column(VARCHAR(10), primary_key=True)
    ISPREF = Column(CHAR(1), primary_key=True)
    AUI = Column(VARCHAR(9), primary_key=True)
    SAUI = Column(VARCHAR(50))
    SCUI = Column(VARCHAR(100))
    SDUI = Column(VARCHAR(100))
    SAB = Column(VARCHAR(40), primary_key=True)
    TTY = Column(VARCHAR(40), primary_key=True)
    CODE = Column(VARCHAR(100), primary_key=True)
    STR = Column(Text, nullable=False)
    SRL = Column(Integer,   nullable=False)
    SUPPRESS = Column(CHAR(1), nullable=False)
    CVF = Column(Integer )

class MRCUI(db.Model):
    __tablename__ = 'MRCUI'
    CUI1 = Column(CHAR(8), primary_key=True)
    VER = Column(VARCHAR(10), primary_key=True)
    REL = Column(VARCHAR(4), primary_key=True)
    RELA = Column(VARCHAR(100))
    MAPREASON = Column(Text)
    CUI2 = Column(CHAR(8))
    MAPIN = Column(CHAR(1))

class MRCXT(db.Model):
    __tablename__ = 'MRCXT'
    CUI = Column(CHAR(8), primary_key=True)
    SUI = Column(VARCHAR(10))
    AUI = Column(VARCHAR(9), primary_key=True)
    SAB = Column(VARCHAR(40), primary_key=True)
    CODE = Column(VARCHAR(100))
    CXN = Column(Integer )
    CXL = Column(VARCHAR(3))
    MRCXTRANK = Column(Integer )
    CXS = Column(Text)
    CUI2 = Column(CHAR(8))
    AUI2 = Column(VARCHAR(9))
    HCD = Column(VARCHAR(100))
    RELA = Column(VARCHAR(100))
    XC = Column(CHAR(1))
    CVF = Column(Integer )

class MRDEF(db.Model):
    __tablename__ = 'MRDEF'
    CUI = Column(CHAR(8), primary_key=True)
    AUI = Column(VARCHAR(9), primary_key=True)
    ATUI = Column(VARCHAR(11), primary_key=True)
    SATUI = Column(VARCHAR(50))
    SAB = Column(VARCHAR(40), primary_key=True)
    DEF = Column(Text, nullable=False)
    SUPPRESS = Column(CHAR(1), nullable=False)
    CVF = Column(Integer )

class MRDOC(db.Model):
    __tablename__ = 'MRDOC'
    DOCKEY = Column(VARCHAR(50), primary_key=True)
    VALUE = Column(VARCHAR(200))
    TYPE = Column(VARCHAR(50), primary_key=True)
    EXPL = Column(Text)

class MRFILES(db.Model):
    __tablename__ = 'MRFILES'
    FIL = Column(VARCHAR(50), primary_key=True)
    DES = Column(VARCHAR(200))
    FMT = Column(Text)
    CLS = Column(Integer )
    RWS = Column(Integer )
    BTS = Column(BigInteger)

class MRHIER(db.Model):
    __tablename__ = 'MRHIER'
    CUI = Column(CHAR(8), primary_key=True)
    AUI = Column(VARCHAR(9), primary_key=True)
    CXN = Column(Integer,   primary_key=True)
    PAUI = Column(VARCHAR(10))
    SAB = Column(VARCHAR(40), primary_key=True)
    RELA = Column(VARCHAR(100))
    PTR = Column(Text)
    HCD = Column(VARCHAR(100))
    CVF = Column(Integer )

class MRHIST(db.Model):
    __tablename__ = 'MRHIST'
    CUI = Column(CHAR(8), primary_key=True)
    SOURCEUI = Column(VARCHAR(100), primary_key=True)
    SAB = Column(VARCHAR(40))
    SVER = Column(VARCHAR(40))
    CHANGETYPE = Column(Text)
    CHANGEKEY = Column(Text)
    CHANGEVAL = Column(Text)
    REASON = Column(Text)
    CVF = Column(Integer )

class MRMAP(db.Model):
    __tablename__ = 'MRMAP'
    MAPSETCUI = Column(CHAR(8), primary_key=True)
    MAPSETSAB = Column(VARCHAR(40), primary_key=True)
    MAPSUBSETID = Column(VARCHAR(10))
    MAPRANK = Column(Integer )
    MAPID = Column(VARCHAR(50), primary_key=True)
    MAPSID = Column(VARCHAR(50))
    FROMID = Column(VARCHAR(50), primary_key=True)
    FROMSID = Column(VARCHAR(50))
    FROMEXPR = Column(Text, nullable=False)
    FROMTYPE = Column(VARCHAR(50), nullable=False)
    FROMRULE = Column(Text)
    FROMRES = Column(Text)
    REL = Column(VARCHAR(4), primary_key=True)
    RELA = Column(VARCHAR(100))
    TOID = Column(VARCHAR(50))
    TOSID = Column(VARCHAR(50))
    TOEXPR = Column(Text)
    TOTYPE = Column(VARCHAR(50))
    TORULE = Column(Text)
    TORES = Column(Text)
    MAPRULE = Column(Text)
    MAPRES = Column(Text)
    MAPTYPE = Column(VARCHAR(50))
    MAPATN = Column(VARCHAR(100))
    MAPATV = Column(Text)
    CVF = Column(Integer )

class MRRANK(db.Model):
    __tablename__ = 'MRRANK'
    MRRANK_RANK = Column(Integer,   primary_key=True)
    SAB = Column(VARCHAR(40), primary_key=True)
    TTY = Column(VARCHAR(40), primary_key=True)
    SUPPRESS = Column(CHAR(1), primary_key=True)

class MRREL(db.Model):
    __tablename__ = 'MRREL'
    CUI1 = Column(CHAR(8), primary_key=True)
    AUI1 = Column(VARCHAR(9))
    STYPE1 = Column(VARCHAR(50), primary_key=True)
    REL = Column(VARCHAR(4), primary_key=True)
    CUI2 = Column(CHAR(8), primary_key=True)
    AUI2 = Column(VARCHAR(9))
    STYPE2 = Column(VARCHAR(50), primary_key=True)
    RELA = Column(VARCHAR(100))
    RUI = Column(VARCHAR(10), primary_key=True)
    SRUI = Column(VARCHAR(50))
    SAB = Column(VARCHAR(40), primary_key=True)
    SL = Column(VARCHAR(40), primary_key=True)
    RG = Column(VARCHAR(10))
    DIR = Column(CHAR(1))
    SUPPRESS = Column(CHAR(1), primary_key=True)
    CVF = Column(Integer )

class MRSAB(db.Model):
    __tablename__ = 'MRSAB'
    VCUI = Column(CHAR(8))
    RCUI = Column(CHAR(8))
    VSAB = Column(VARCHAR(40), primary_key=True)
    RSAB = Column(VARCHAR(40), primary_key=True)
    SON = Column(Text, nullable=False)
    SF = Column(VARCHAR(40), primary_key=True)
    SVER = Column(VARCHAR(40))
    VSTART = Column(CHAR(8))
    VEND = Column(CHAR(8))
    IMETA = Column(VARCHAR(10), nullable=False)
    RMETA = Column(VARCHAR(10))
    SLC = Column(Text)
    SCC = Column(Text)
    SRL = Column(Integer,   nullable=False)
    TFR = Column(Integer )
    CFR = Column(Integer )
    CXTY = Column(VARCHAR(50))
    TTYL = Column(VARCHAR(400))
    ATNL = Column(Text)
    LAT = Column(CHAR(3))
    CENC = Column(VARCHAR(40), nullable=False)
    CURVER = Column(CHAR(1), nullable=False)
    SABIN = Column(CHAR(1), nullable=False)
    SSN = Column(Text, nullable=False)
    SCIT = Column(Text, nullable=False)

class MRSAT(db.Model):
    __tablename__ = 'MRSAT'
    CUI = Column(CHAR(8), primary_key=True)
    LUI = Column(VARCHAR(10))
    SUI = Column(VARCHAR(10))
    METAUI = Column(VARCHAR(100))
    STYPE = Column(VARCHAR(50), primary_key=True)
    CODE = Column(VARCHAR(100))
    ATUI = Column(VARCHAR(11), primary_key=True)
    SATUI = Column(VARCHAR(50))
    ATN = Column(VARCHAR(100), primary_key=True)
    SAB = Column(VARCHAR(40), primary_key=True)
    ATV = Column(Text)
    SUPPRESS = Column(CHAR(1))
    CVF = Column(Integer )

class MRSMAP(db.Model):
    __tablename__ = 'MRSMAP'
    MAPSETCUI = Column(CHAR(8), primary_key=True)
    MAPSETSAB = Column(VARCHAR(40), primary_key=True)
    FROMID = Column(VARCHAR(50), primary_key=True)
    FROMEXPR = Column(Text, nullable=False)
    FROMTYPE = Column(VARCHAR(50), nullable=False)
    FROMRULE = Column(Text)
    REL = Column(VARCHAR(4), primary_key=True)
    RELA = Column(VARCHAR(100))
    TOID = Column(VARCHAR(50), primary_key=True)
    TOEXPR = Column(Text, nullable=False)
    TOTYPE = Column(VARCHAR(50), nullable=False)
    TORULE = Column(Text)
    MAPRULE = Column(Text)
    MAPRES = Column(Text)
    CVF = Column(Integer )

class MRSTY(db.Model):
    __tablename__ = 'MRSTY'
    CUI = Column(CHAR(8), primary_key=True)
    TUI = Column(CHAR(4), primary_key=True)
    STN = Column(VARCHAR(100), nullable=False)
    STY = Column(VARCHAR(50), nullable=False)
    ATUI = Column(VARCHAR(11))
    CVF = Column(Integer )

class MRSO(db.Model):
    __tablename__ = 'MRSO'
    CUI = Column(CHAR(8), primary_key=True)
    AUI = Column(VARCHAR(9), primary_key=True)
    LUI = Column(VARCHAR(10), primary_key=True)
    SUI = Column(VARCHAR(10), primary_key=True)
    SDUI = Column(VARCHAR(100))
    SAB = Column(VARCHAR(40), primary_key=True)
    CODE = Column(VARCHAR(100), primary_key=True)
    STR = Column(Text, nullable=False)
    SRL = Column(Integer,   nullable=False)
    TTY = Column(VARCHAR(40), primary_key=True)
    SUPPRESS = Column(CHAR(1), nullable=False)
    CVF = Column(Integer )

class MRXNW_ENG(db.Model):
    __tablename__ = 'MRXNW_ENG'
    CUI = Column(CHAR(8), primary_key=True)
    LUI = Column(VARCHAR(10), primary_key=True)
    SUI = Column(VARCHAR(10), primary_key=True)
    RXCUI = Column(VARCHAR(8), primary_key=True)
    SAB = Column(VARCHAR(40), primary_key=True)
    TTY = Column(VARCHAR(4), primary_key=True)
    CODE = Column(VARCHAR(100), primary_key=True)
    STR = Column(Text, nullable=False)
    SRL = Column(Integer,   nullable=False)
    SUPPRESS = Column(CHAR(1), nullable=False)
    CVF = Column(Integer )

class MRXW_ENG(db.Model):
    __tablename__ = 'MRXW_ENG'
    CUI = Column(CHAR(8), primary_key=True)
    LUI = Column(VARCHAR(10), primary_key=True)
    SUI = Column(VARCHAR(10), primary_key=True)
    RXCUI = Column(VARCHAR(8), primary_key=True)
    SAB = Column(VARCHAR(40), primary_key=True)
    TTY = Column(VARCHAR(4), primary_key=True)
    CODE = Column(VARCHAR(100), primary_key=True)
    STR = Column(Text, nullable=False)
    SRL = Column(Integer,   nullable=False)
    SUPPRESS = Column(CHAR(1), nullable=False)
    CVF = Column(Integer )

from sqlalchemy import create_engine, MetaData, Table, Column, String, Index

# Assuming engine is already defined, e.g., engine = create_engine('your_connection_string')
metadata = MetaData()

# Define tables
mrconso = Table('MRCONSO', metadata,
                Column('CUI', String),
                Column('AUI', String, primary_key=True),
                Column('SUI', String),
                Column('LUI', String),
                Column('CODE', String),
                Column('SAB', String),
                Column('TTY', String),
                Column('SCUI', String),
                Column('SDUI', String),
                Column('STR', String))

mrcxt = Table('MRCXT', metadata,
              Column('CUI', String),
              Column('AUI', String),
              Column('SAB', String))

mrdef = Table('MRDEF', metadata,
              Column('CUI', String),
              Column('AUI', String),
              Column('ATUI', String, primary_key=True),
              Column('SAB', String))

mrhier = Table('MRHIER', metadata,
               Column('CUI', String),
               Column('AUI', String),
               Column('SAB', String),
               Column('PTR', String),
               Column('PAUI', String))

mrhist = Table('MRHIST', metadata,
               Column('CUI', String),
               Column('SOURCEUI', String),
               Column('SAB', String))

mrrank = Table('MRRANK', metadata,
               Column('SAB', String, primary_key=True),
               Column('TTY', String, primary_key=True))

mrrel = Table('MRREL', metadata,
              Column('CUI1', String),
              Column('AUI1', String),
              Column('CUI2', String),
              Column('AUI2', String),
              Column('RUI', String, primary_key=True),
              Column('SAB', String))

mrsab = Table('MRSAB', metadata,
              Column('VSAB', String, primary_key=True),
              Column('RSAB', String))

mrsat = Table('MRSAT', metadata,
              Column('CUI', String),
              Column('METAUI', String),
              Column('ATUI', String, primary_key=True),
              Column('SAB', String),
              Column('ATN', String))

mrsty = Table('MRSTY', metadata,
              Column('CUI', String),
              Column('ATUI', String, primary_key=True),
              Column('STY', String))

# Define indexes
Index('X_MRCONSO_CUI', mrconso.c.CUI)
Index('X_MRCONSO_SUI', mrconso.c.SUI)
Index('X_MRCONSO_LUI', mrconso.c.LUI)
Index('X_MRCONSO_CODE', mrconso.c.CODE)
Index('X_MRCONSO_SAB_TTY', mrconso.c.SAB, mrconso.c.TTY)
Index('X_MRCONSO_SCUI', mrconso.c.SCUI)
Index('X_MRCONSO_SDUI', mrconso.c.SDUI)
Index('X_MRCONSO_STR', mrconso.c.STR, postgresql_using='btree')
Index('X_MRCXT_CUI', mrcxt.c.CUI)
Index('X_MRCXT_AUI', mrcxt.c.AUI)
Index('X_MRCXT_SAB', mrcxt.c.SAB)
Index('X_MRDEF_CUI', mrdef.c.CUI)
Index('X_MRDEF_AUI', mrdef.c.AUI)
Index('X_MRDEF_SAB', mrdef.c.SAB)
Index('X_MRHIER_CUI', mrhier.c.CUI)
Index('X_MRHIER_AUI', mrhier.c.AUI)
Index('X_MRHIER_SAB', mrhier.c.SAB)
Index('X_MRHIER_PTR', mrhier.c.PTR, postgresql_using='btree')
Index('X_MRHIER_PAUI', mrhier.c.PAUI)
Index('X_MRHIST_CUI', mrhist.c.CUI)
Index('X_MRHIST_SOURCEUI', mrhist.c.SOURCEUI)
Index('X_MRHIST_SAB', mrhist.c.SAB)
Index('X_MRREL_CUI1', mrrel.c.CUI1)
Index('X_MRREL_AUI1', mrrel.c.AUI1)
Index('X_MRREL_CUI2', mrrel.c.CUI2)
Index('X_MRREL_AUI2', mrrel.c.AUI2)
Index('X_MRREL_SAB', mrrel.c.SAB)
Index('X_MRSAB_RSAB', mrsab.c.RSAB)
Index('X_MRSAT_CUI', mrsat.c.CUI)
Index('X_MRSAT_METAUI', mrsat.c.METAUI)
Index('X_MRSAT_SAB', mrsat.c.SAB)
Index('X_MRSAT_ATN', mrsat.c.ATN)
Index('X_MRSTY_CUI', mrsty.c.CUI)
Index('X_MRSTY_STY', mrsty.c.STY)
