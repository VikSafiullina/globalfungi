import json
import datetime
from datetime import date
from validate_email import validate_email
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, Boolean, Float, Text, DateTime, func

Base = declarative_base()
class Sample(Base):
    __tablename__ = 'Samples'
    id = Column(UUID, primary_key=True)
    original_id = Column(Integer)
    add_date = Column(Date)
    paper_id = Column(UUID)
    chemical_data_id = Column(UUID)
    env_data_id = Column(UUID)
    sampling_data_id = Column(UUID)
    sequencing_data_id = Column(UUID)
    latitude = Column(Float)
    longitude = Column(Float)
    sample_info = Column(Text)
    def __repr__(self):
        return f"<Sample(id='{self.id}', original_id='{self.original_id}', add_date='{self.add_date}', " \
               f"paper_id='{self.paper_id}', chemical_data_id='{self.chemical_data_id}', " \
               f"env_data_id='{self.env_data_id}', sampling_data_id='{self.sampling_data_id}', " \
               f"sequencing_data_id='{self.sequencing_data_id}', latitude={self.latitude}, " \
               f"longitude={self.longitude}, sample_info='{self.sample_info}')>"

    def __str__(self):
        return f"Sample ID: {self.id}, Original ID: {self.original_id}, Added on: {self.add_date}, " \
               f"Paper ID: {self.paper_id}, Chemical Data ID: {self.chemical_data_id}, " \
               f"Environmental Data ID: {self.env_data_id}, Sampling Data ID: {self.sampling_data_id}, " \
               f"Sequencing Data ID: {self.sequencing_data_id}, Latitude: {self.latitude}, " \
               f"Longitude: {self.longitude}, Sample Info: {self.sample_info}"
    def to_dict(self):
        return {
            'id': self.id,
            'original_id': self.original_id,
            'add_date': self.add_date.isoformat() if self.add_date else None,
            'paper_id': self.paper_id,
            'chemical_data_id': self.chemical_data_id,
            'env_data_id': self.env_data_id,
            'sampling_data_id': self.sampling_data_id,
            'sequencing_data_id': self.sequencing_data_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'sample_info': self.sample_info
        }

    def to_json(self):
        return json.dumps(self.to_dict())
    

class Paper(Base):
    __tablename__ = 'paper'
    id = Column(UUID, primary_key=True)
    internal_id = Column(String(36))
    title = Column(Text)
    authors = Column(Text)
    journal = Column(Text)
    year = Column(Integer)
    doi = Column(Text)
    contact = Column(Text)
    area_gps = Column(Float)

    def __repr__(self):
        # This method returns an unambiguous string representation of the object, useful for debugging.
        return f"<Paper(id='{self.id}', title='{self.title}')>"

    def __str__(self):
        # This method returns a readable string representation of the object, for display purposes.
        return f"Paper ID: {self.id}, Title: {self.title}, Year: {self.year}"

    def to_dict(self):
        # This method allows a Paper object to be easily converted to a dictionary.
        return {
            'id': self.id,
            'internal_id': self.internal_id,
            'title': self.title,
            'authors': self.authors,
            'journal': self.journal,
            'year': self.year,
            'doi': self.doi,
            'contact': self.contact,
            'area_gps': self.area_gps
        }

    def to_json(self):
        # This method allows a Paper object to be easily serialized to JSON.
        return json.dumps(self.to_dict())

class ChemicalData(Base):
    __tablename__ = 'chemicaldata'
    id = Column(UUID, primary_key=True)
    total_c_content = Column(Float)
    total_n_content = Column(Float)
    organic_matter_content = Column(Float)
    ph = Column(Float)
    ph_method = Column(String(64))
    total_ca = Column(Float)
    total_p = Column(Float)
    total_k = Column(Float)

    def __repr__(self):
        return f"<ChemicalData(id='{self.id}')>"

    def __str__(self):
        return (f"Chemical Data ID: {self.id}, C Content: {self.total_c_content}, "
                f"N Content: {self.total_n_content}, Organic Matter: {self.organic_matter_content}, "
                f"pH: {self.ph}, pH Method: {self.ph_method}, Ca: {self.total_ca}, "
                f"P: {self.total_p}, K: {self.total_k}")

    def to_dict(self):
        return {
            'id': self.id,
            'total_c_content': self.total_c_content,
            'total_n_content': self.total_n_content,
            'organic_matter_content': self.organic_matter_content,
            'ph': self.ph,
            'ph_method': self.ph_method,
            'total_ca': self.total_ca,
            'total_p': self.total_p,
            'total_k': self.total_k
        }

    def to_json(self):
        return json.dumps(self.to_dict(), default=str) # default=str to handle None types


class EnvData(Base):
    __tablename__ = 'envdata'
    id = Column(UUID, primary_key=True)
    biome = Column(String(32))
    biome_detail = Column(Text)
    plants_dominant = Column(Text)
    plants_all = Column(Text)

    def __repr__(self):
        return f"<EnvData(id='{self.id}', biome='{self.biome}')>"

    def __str__(self):
        return (f"Env Data ID: {self.id}, Biome: {self.biome}, "
                f"Biome Detail: {self.biome_detail}, Dominant Plants: {self.plants_dominant}, "
                f"All Plants: {self.plants_all}")

    def to_dict(self):
        return {
            'id': self.id,
            'biome': self.biome,
            'biome_detail': self.biome_detail,
            'plants_dominant': self.plants_dominant,
            'plants_all': self.plants_all
        }

    def to_json(self):
        return json.dumps(self.to_dict(), default=str) # default=str to handle None types


class SamplingData(Base):
    __tablename__ = 'samplingdata'
    id = Column(UUID, primary_key=True)
    sample_name = Column(String(36))
    sample_type = Column(String(32))
    manipulated = Column(Boolean) # tinyint(1) in MariaDB can be represented as a Boolean in Python
    sample_type_detailed = Column(Text)
    date_of_sampling = Column(Date)
    area_sampled = Column(Float)
    number_of_subsamples = Column(Integer)
    sampling_info = Column(Text)
    sample_depth_from = Column(Float)
    sample_depth_to = Column(Float)
    mat = Column(Float)
    map = Column(Float)
    external_mat = Column(Float)
    external_map = Column(Float)
    sample_seqid = Column(String(120))
    sample_barcode = Column(Text)

    def __repr__(self):
        return "<SamplingData(id='{}', sample_name='{}')>".format(self.id, self.sample_name)

    def to_dict(self):
        return {
            'id': self.id,
            'sample_name': self.sample_name,
            'sample_type': self.sample_type,
            'manipulated': self.manipulated,
            'sample_type_detailed': self.sample_type_detailed,
            'date_of_sampling': self.date_of_sampling,
            'area_sampled': self.area_sampled,
            'number_of_subsamples': self.number_of_subsamples,
            'sampling_info': self.sampling_info,
            'sample_depth_from': self.sample_depth_from,
            'sample_depth_to': self.sample_depth_to,
            'mat': self.mat,
            'map': self.map,
            'external_mat': self.external_mat,
            'external_map': self.external_map,
            'sample_seqid': self.sample_seqid,
            'sample_barcode': self.sample_barcode,
        }

    def to_json(self):
        # Convert the object to JSON; using str for date_of_sampling to avoid serialization errors
        return json.dumps({key: (str(value) if isinstance(value, (date, datetime.date)) else value) 
                          for key, value in self.to_dict().items()}, ensure_ascii=False)


class SequencingData(Base):
    __tablename__ = 'SequencingData'
    
    id = Column(UUID, primary_key=True)
    sequencing_platform = Column(String(32))
    target_gene = Column(String(32))
    primers = Column(Text)
    primers_sequence = Column(Text)
    extraction_dna_mass = Column(Float)
    extraction_dna_size = Column(Text)
    extraction_dna_method = Column(Text)

    def __repr__(self):
        return "<SequencingData(id='{0}', sequencing_platform='{1}', target_gene='{2}')>".format(
                self.id, self.sequencing_platform, self.target_gene)
    
    def __str__(self):
        return (f"Sequencing Data ID: {self.id}, Sequencing Platform: {self.sequencing_platform}, "
                f"Target Gene: {self.target_gene}, Primers: {self.primers}, "
                f"Primers Sequence: {self.primers_sequence}, DNA Mass: {self.extraction_dna_mass}, "
                f"DNA Size: {self.extraction_dna_size}, DNA Method: {self.extraction_dna_method}")
    
    def to_dict(self):
        return {
            'id': self.id,
            'sequencing_platform': self.sequencing_platform,
            'target_gene': self.target_gene,
            'primers': self.primers,
            'primers_sequence': self.primers_sequence,
            'extraction_dna_mass': self.extraction_dna_mass,
            'extraction_dna_size': self.extraction_dna_size,
            'extraction_dna_method': self.extraction_dna_method
        }
    
    def to_json(self):
        return json.dumps(self.to_dict(), default=str)
    

    
class Message(Base):
    __tablename__ = 'messages'
    id = Column(UUID, primary_key=True)
    email = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=True)
    message = Column(String, nullable=False)  # or Text, depending on the expected length
    processed = Column(Boolean, default=False, nullable=False)
    date = Column(DateTime, default=func.current_timestamp(), nullable=False)

    @staticmethod
    def is_valid_email(email) -> bool:
        is_valid = validate_email(
            email_address=email,
            check_regex=True,
            check_mx=True,
            use_blacklist=True,
            debug=False
        )
        return is_valid
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
            'processed': self.processed,
            'date': self.date.isoformat()
        }
    
    def save(self, session):
        """ Validates and saves an instance to the database. """
        try:
            if not self.is_valid_email(self.email):
                raise ValueError(f"The email address '{self.email}' is invalid.")
            session.add(self)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e




class MailList(Base):
    __tablename__ = 'maillist'
    id = Column(UUID, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    date = Column(DateTime, default=func.current_timestamp(), nullable=False)

    @staticmethod
    def is_valid_email(email) -> bool:
        is_valid = validate_email(
            email_address=email,
            check_regex=True,
            check_mx=True,
            use_blacklist=True,
            debug=False
        )
        return is_valid
    
    def save(self, session):
        """ Validates and saves an instance to the database. """
        try:
            if not self.is_valid_email(self.email):
                raise ValueError(f"The email address '{self.email}' is invalid.")
            session.add(self)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


class TaxonomyMigrated(Base):
    __tablename__ = 'taxonomy_migrated'
    
    id = Column(String(36), primary_key=True)
    sh = Column(String(32), nullable=False)
    kingdom = Column(String(64), nullable=False)
    phylum = Column(String(64), nullable=False)
    _class = Column('class', String(64), nullable=False)  # 'class' is a reserved keyword in Python, hence the underscore
    order = Column(String(64), nullable=False)
    family = Column(String(64), nullable=False)
    genus = Column(String(64), nullable=False)
    species = Column(String(64), nullable=False)

    def __repr__(self):
        return f"<TaxonomyMigrated(id='{self.id}', kingdom='{self.kingdom}', " \
               f"phylum='{self.phylum}', class='{self._class}', order='{self.order}', " \
               f"family='{self.family}', genus='{self.genus}', species='{self.species}, sh='{self.sh}')>"

    def to_dict(self):
        return {
            'id': self.id,
            'kingdom': self.kingdom,
            'phylum': self.phylum,
            'class': self._class,
            'order': self.order,
            'family': self.family,
            'genus': self.genus,
            'species': self.species,
            'sh': self.sh
        }

    def get_hierarchy(self):
        return {
            'kingdom': self.kingdom,
            'phylum': self.phylum,
            'class': self._class,
            'order': self.order,
            'family': self.family,
            'genus': self.genus,
            'species': self.species
        }

    def validate_hierarchy(self):
        """ Validates whether the taxonomy is provided in correct hierarchical order. """
        hierarchy = ['kingdom', 'phylum', '_class', 'order', 'family', 'genus', 'species']
        known_taxonomy = self.to_dict()  # Assuming to_dict() returns a dictionary of attributes
        
        previous_attribute = None
        for level in hierarchy:
            attribute = level if level != '_class' else 'class'  # Adjust for the 'class' field naming
            # If the current level is unknown, then all subsequent levels must also be unknown.
            if known_taxonomy[attribute] == 'unidentified' or known_taxonomy[attribute] is None:
                if previous_attribute and (known_taxonomy[previous_attribute] == 'unidentified' or known_taxonomy[previous_attribute] is None):
                    # The previous attribute is unidentified, which is valid; continue checking
                    continue
                else:
                    # The previous attribute is identified, but the current is not, which is invalid
                    raise ValueError(f"The taxonomy level '{attribute}' is unidentified, "
                                     f"but the previous level '{previous_attribute}' is identified. "
                                     f"This is an invalid state.")
            previous_attribute = attribute

    def save(self, session):
        """ Validates and saves an instance to the database. """
        try:
            self.validate_hierarchy()  # Validate before saving
            session.add(self)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


class SHMigrated(Base):
    __tablename__ = 'sh_migrated'
    
    id = Column(UUID, primary_key=True)
    sh_name = Column(String(255), nullable=True)
    sample_id = Column(UUID, nullable=True)
    abundance = Column(Integer, nullable=True)
    variants = Column(Integer, nullable=True)

    def __init__(self, id, sh_name, sample_id, abundance, variants):
        self.id = id
        self.sh_name = sh_name
        self.sample_id = sample_id
        self.abundance = abundance
        self.variants = variants

    def __repr__(self):
        return f"<SHMigrated(id='{self.id}', sh_name='{self.sh_name}', sample_id={self.sample_id}, abundance={self.abundance}, variants={self.variants})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'sh_name': self.sh_name,
            'sample_id': self.sample_id,
            'abundance': self.abundance,
            'variants': self.variants
        }
    
    def to_json(self):
        return json.dumps(self.to_dict(), default=str)
    

