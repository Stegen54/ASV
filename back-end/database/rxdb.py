from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RXNATOMARCHIVE(db.Model):
    __tablename__ = 'RXNATOMARCHIVE'
    RXAUI = db.Column(db.String(8), primary_key=True, nullable=False)
    AUI = db.Column(db.String(10))
    STR = db.Column(db.String(4000), nullable=False)
    ARCHIVE_TIMESTAMP = db.Column(db.String(280), nullable=False)
    CREATED_TIMESTAMP = db.Column(db.String(280), nullable=False)
    UPDATED_TIMESTAMP = db.Column(db.String(280), nullable=False)
    CODE = db.Column(db.String(50))
    IS_BRAND = db.Column(db.String(1))
    LAT = db.Column(db.String(3))
    LAST_RELEASED = db.Column(db.String(30))
    SAUI = db.Column(db.String(50))
    VSAB = db.Column(db.String(40))
    RXCUI = db.Column(db.String(8))
    SAB = db.Column(db.String(20))
    TTY = db.Column(db.String(20))
    MERGED_TO_RXCUI = db.Column(db.String(8))
    
    __table_args__ = (
        db.Index('X_RXNATOMARCHIVE_RXAUI', 'RXAUI'),
        db.Index('X_RXNATOMARCHIVE_RXCUI', 'RXCUI'),
        db.Index('X_RXNATOMARCHIVE_MERGED_TO', 'MERGED_TO_RXCUI')
    )

class RXNCONSO(db.Model):
    __tablename__ = 'RXNCONSO'
    RXCUI = db.Column(db.String(8), primary_key=True, nullable=False)
    LAT = db.Column(db.String(3), default='ENG', nullable=False)
    TS = db.Column(db.String(1))
    LUI = db.Column(db.String(8))
    STT = db.Column(db.String(3))
    SUI = db.Column(db.String(8))
    ISPREF = db.Column(db.String(1))
    RXAUI = db.Column(db.String(8), nullable=False)
    SAUI = db.Column(db.String(50))
    SCUI = db.Column(db.String(50))
    SDUI = db.Column(db.String(50))
    SAB = db.Column(db.String(20), nullable=False)
    TTY = db.Column(db.String(20), nullable=False)
    CODE = db.Column(db.String(50), nullable=False)
    STR = db.Column(db.String(3000), nullable=False)
    SRL = db.Column(db.String(10))
    SUPPRESS = db.Column(db.String(1))
    CVF = db.Column(db.String(50))
    
    __table_args__ = (
        db.Index('X_RXNCONSO_STR', 'STR'),
        db.Index('X_RXNCONSO_RXCUI', 'RXCUI'),
        db.Index('X_RXNCONSO_TTY', 'TTY'),
        db.Index('X_RXNCONSO_CODE', 'CODE')
    )

class RXNREL(db.Model):
    __tablename__ = 'RXNREL'
    RXCUI1 = db.Column(db.String(8))
    RXAUI1 = db.Column(db.String(8))
    STYPE1 = db.Column(db.String(50))
    REL = db.Column(db.String(4), primary_key=True, nullable=False)
    RXCUI2 = db.Column(db.String(8))
    RXAUI2 = db.Column(db.String(8))
    STYPE2 = db.Column(db.String(50))
    RELA = db.Column(db.String(100))
    RUI = db.Column(db.String(10))
    SRUI = db.Column(db.String(50))
    SAB = db.Column(db.String(20), nullable=False)
    SL = db.Column(db.String(1000))
    DIR = db.Column(db.String(1))
    RG = db.Column(db.String(10))
    SUPPRESS = db.Column(db.String(1))
    CVF = db.Column(db.String(50))
    
    __table_args__ = (
        db.Index('X_RXNREL_RXCUI1', 'RXCUI1'),
        db.Index('X_RXNREL_RXCUI2', 'RXCUI2'),
        db.Index('X_RXNREL_RELA', 'RELA')
    )

class RXNSAB(db.Model):
    __tablename__ = 'RXNSAB'
    VCUI = db.Column(db.String(8))
    RCUI = db.Column(db.String(8))
    VSAB = db.Column(db.String(40))
    RSAB = db.Column(db.String(20), primary_key=True, nullable=False)
    SON = db.Column(db.String(3000))
    SF = db.Column(db.String(20))
    SVER = db.Column(db.String(20))
    VSTART = db.Column(db.String(10))
    VEND = db.Column(db.String(10))
    IMETA = db.Column(db.String(10))
    RMETA = db.Column(db.String(10))
    SLC = db.Column(db.String(1000))
    SCC = db.Column(db.String(1000))
    SRL = db.Column(db.Integer)
    TFR = db.Column(db.Integer)
    CFR = db.Column(db.Integer)
    CXTY = db.Column(db.String(50))
    TTYL = db.Column(db.String(300))
    ATNL = db.Column(db.String(1000))
    LAT = db.Column(db.String(3))
    CENC = db.Column(db.String(20))
    CURVER = db.Column(db.String(1))
    SABIN = db.Column(db.String(1))
    SSN = db.Column(db.String(3000))
    SCIT = db.Column(db.String(4000))

class RXNSAT(db.Model):
    __tablename__ = 'RXNSAT'
    RXCUI = db.Column(db.String(8))
    LUI = db.Column(db.String(8))
    SUI = db.Column(db.String(8))
    RXAUI = db.Column(db.String(9))
    STYPE = db.Column(db.String(50))
    CODE = db.Column(db.String(50))
    ATUI = db.Column(db.String(11), primary_key=True, nullable=False)
    SATUI = db.Column(db.String(50))
    ATN = db.Column(db.String(1000), nullable=False)
    SAB = db.Column(db.String(20), nullable=False)
    ATV = db.Column(db.String(4000))
    SUPPRESS = db.Column(db.String(1))
    CVF = db.Column(db.String(50))
    
    __table_args__ = (
        db.Index('X_RXNSAT_RXCUI', 'RXCUI'),
        db.Index('X_RXNSAT_ATV', 'ATV'),
        db.Index('X_RXNSAT_ATN', 'ATN')
    )

class RXNSTY(db.Model):
    __tablename__ = 'RXNSTY'
    RXCUI = db.Column(db.String(8), primary_key=True, nullable=False)
    TUI = db.Column(db.String(4))
    STN = db.Column(db.String(100))
    STY = db.Column(db.String(50))
    ATUI = db.Column(db.String(11))
    CVF = db.Column(db.String(50))

class RXNDOC(db.Model):
    __tablename__ = 'RXNDOC'
    DOCKEY = db.Column(db.String(50), primary_key=True, nullable=False)
    VALUE = db.Column(db.String(1000))
    TYPE = db.Column(db.String(50), nullable=False)
    EXPL = db.Column(db.String(1000))

class RXNCUICHANGES(db.Model):
    __tablename__ = 'RXNCUICHANGES'
    RXAUI = db.Column(db.String(8))
    CODE = db.Column(db.String(50))
    SAB = db.Column(db.String(20))
    TTY = db.Column(db.String(20))
    STR = db.Column(db.String(3000))
    OLD_RXCUI = db.Column(db.String(8), primary_key=True, nullable=False)
    NEW_RXCUI = db.Column(db.String(8), primary_key=True, nullable=False)

class RXNCUI(db.Model):
    __tablename__ = 'RXNCUI'
    cui1 = db.Column(db.String(8), primary_key=True, nullable=False)
    ver_start = db.Column(db.String(40))
    ver_end = db.Column(db.String(40))
    cardinality = db.Column(db.String(8))
    cui2 = db.Column(db.String(8), primary_key=True, nullable=False)
