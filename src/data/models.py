import json
import datetime
from datetime import date
from validate_email import validate_email
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, Boolean, Float, Text, DateTime, func
import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from common import config
import re
from .enums import BiomeEnum, PhMethodEnum, SampleTypeEnum, SequencingPlatformEnum, TargetEnum, BiomeDetailedEnum
logger = logging.getLogger(__name__)

Base = declarative_base()

class Sample(Base):
    __tablename__ = 'Samples_migrated'
    id = Column(UUID(as_uuid=True), primary_key=True)
    original_id = Column(Integer)
    paper_id = Column(UUID(as_uuid=True), ForeignKey('Paper.id'))

    chemical_data_id = Column(UUID(as_uuid=True), ForeignKey('ChemicalData.id'))
    env_data_id = Column(UUID(as_uuid=True), ForeignKey('EnvData.id'))
    sampling_data_id = Column(UUID(as_uuid=True), ForeignKey('SamplingData.id'))
    sequencing_data_id = Column(UUID(as_uuid=True), ForeignKey('SequencingData.id'))
  
    latitude = Column(Float)
    longitude = Column(Float)
    sample_info = Column(Text)
    created_at = Column(DateTime, default=func.current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=func.current_timestamp(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    # One-to-one relationships
    chemical_data = relationship("ChemicalData", back_populates="sample", foreign_keys=[chemical_data_id])
    environmental_data = relationship("EnvData", back_populates="sample", foreign_keys=[env_data_id])
    sampling_data = relationship("SamplingData", back_populates="sample", foreign_keys=[sampling_data_id])
    sequencing_data = relationship("SequencingData", back_populates="sample", foreign_keys=[sequencing_data_id])

    # One-to-many relationships
    
    def __repr__(self):
        return f"<Sample(id='{self.id}', original_id='{self.original_id}', add_date='{self.created_at}', paper_id='{self.paper_id}', chemical_data_id='{self.chemical_data_id}', env_data_id='{self.env_data_id}', sampling_data_id='{self.sampling_data_id}', sequencing_data_id='{self.sequencing_data_id}', latitude={self.latitude}, longitude={self.longitude}, sample_info='{self.sample_info}')>"

    def __str__(self):
        return f"Sample ID: {self.id}, Original ID: {self.original_id}, Added on: {self.created_at}, Paper ID: {self.paper_id}, Chemical Data ID: {self.chemical_data_id}, Environmental Data ID: {self.env_data_id}, Sampling Data ID: {self.sampling_data_id}, Sequencing Data ID: {self.sequencing_data_id}, Latitude: {self.latitude}, Longitude: {self.longitude}, Sample Info: {self.sample_info}"

    def to_dict(self):
        return {
            'id': self.id,
            'original_id': self.original_id,
            'add_date': self.created_at.isoformat() if self.created_at else None,
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

    @staticmethod
    def is_valid_coordinates(latitude, longitude) -> bool:
        """ Validates whether the coordinates are in the correct range. """
        if latitude < -90 or latitude > 90:
            logging.error(f"The latitude '{latitude}' is outside the valid range of -90 to 90.")
            return False
        if longitude < -180 or longitude > 180:
            logging.error(f"The longitude '{longitude}' is outside the valid range of -180 to 180.")
            return False
        return True
    
    @staticmethod
    def is_valid_add_date(add_date) -> bool:
        """ Validates whether the add_date is not in the future. """
        if add_date > date.today():
            logging.error(f"The add_date '{add_date}' is in the future.")
            return False
        return True

    
    

class Paper(Base):
    __tablename__ = 'Paper'
    id = Column(UUID(as_uuid=True), primary_key=True)
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

    @staticmethod
    def is_valid_title(title) -> bool:
        if not title or title.isspace():
            logging.error("The title must not be empty.")
            return False
        return True

    @staticmethod
    def is_valid_authors(authors):
        if not authors or authors.isspace():
            logging.error("The authors field must not be empty.")
            return False
        return True

    @staticmethod
    def is_valid_year(year) -> bool:
        """ Validates whether the year is not in the future. """
        if year > date.today().year:
            logging.error(f"The year '{year}' is in the future.")
            return False
        return True

    @staticmethod
    def is_valid_journal(journal):
        if not journal or journal.isspace():
            logging.error("The journal field must not be empty.")
            return False
        return True

    @staticmethod
    def is_valid_doi(doi) -> bool:
        doi_regex = re.compile(r'^10\.\d+(\.\d+)*\/\w+')
        
        # Check the overall DOI structure.
        if not doi_regex.match(doi):
            logging.error("The DOI '{doi}' is not in the correct format.")
            return False
        # Split the DOI into prefix and suffix
        prefix, suffix = doi.split('/')
        # Validate the prefix further if needed (beyond the regex, for example, checking the number part)
        prefix_number = prefix[3:]  # Remove the '10.' part
        if any(not part.isdigit() or int(part) < 1000 for part in prefix_number.split('.') if part):
            logging.error(f"The DOI prefix '{prefix}' is not valid. Each segment must be a number >= 1000.")
            return False
        
        return True


class ChemicalData(Base):
    __tablename__ = 'ChemicalData'
    id = Column(UUID(as_uuid=True), primary_key=True)
    sample_id = Column(UUID(as_uuid=True), ForeignKey('Samples_migrated.id'))

    # One-to-one relationship with Sample
    sample = relationship("Sample", back_populates="chemical_data")

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
        return f"Chemical Data ID: {self.id}, C Content: {self.total_c_content}, N Content: {self.total_n_content}, Organic Matter: {self.organic_matter_content}, pH: {self.ph}, pH Method: {self.ph_method}, Ca: {self.total_ca}, P: {self.total_p}, K: {self.total_k}"

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


    def validate_chemical_values(self) -> bool:
        """ Validate chemical property values. """
        if self.total_c_content < 0:
            logging.error("Total carbon content cannot be negative.")
            return False
        
        if self.total_n_content < 0:
            logging.error("Total nitrogen content cannot be negative.")
            return False
        if self.organic_matter_content < 0:
            logging.error("Organic matter content cannot be negative.")
            return False
        if not 0 <= self.ph <= 14:
            logging.error("pH value must be between 0 and 14.")
            return False
        return True

    def validate_ph_method(self) -> bool:
        """ Validate the pH method. """
        if not self.ph_method:
            logging.error("pH method cannot be empty.")
            return False
        # Check against PhMethodEnum values
        if self.ph_method.lower() not in [ph_method.value.lower() for ph_method in PhMethodEnum]:
            logging.error(f"The pH method '{self.ph_method}' is not a valid value.")
            return False
        return True

class EnvData(Base):
    __tablename__ = 'EnvData'
    id = Column(UUID(as_uuid=True), primary_key=True)
    sample_id = Column(UUID(as_uuid=True), ForeignKey('Samples_migrated.id'))

    # One-to-one relationship with Sample
    sample = relationship("Sample", back_populates="environmental_data", foreign_keys=[sample_id], single_parent=True)

    biome = Column(String(32))
    biome_detail = Column(Text)
    plants_dominant = Column(Text)
    plants_all = Column(Text)

    def __repr__(self):
        return f"<EnvData(id='{self.id}', biome='{self.biome}')>"

    def __str__(self):
        return f"Env Data ID: {self.id}, Biome: {self.biome}, Biome Detail: {self.biome_detail}, Dominant Plants: {self.plants_dominant}, All Plants: {self.plants_all}"

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

    def validate_biome(self) -> bool:
        """ Validate the biome information. """
        if not self.biome:  # Ensuring the biome is not empty
            logging.error("Biome cannot be empty.")
            return False
        
        # validate against BiomeEnum values
        if self.biome.lower() not in [biome.value.lower() for biome in BiomeEnum]:
            logging.error(f"The biome '{self.biome}' is not a valid value.")
            return False
        return True
    
    def validate_biome_detail(self) -> bool:
        """ Validate the biome detail information. """
        # validate against BiomeDetailedEnum values
        if self.biome_detail.lower() not in [biome_detail.value.lower() for biome_detail in BiomeDetailedEnum]:
            logging.error(f"The biome detail '{self.biome_detail}' is not a valid value.")
            return False
        return True


class SamplingData(Base):
    __tablename__ = 'SamplingData'
    id = Column(UUID(as_uuid=True), primary_key=True)
    sample_id = Column(UUID(as_uuid=True), ForeignKey('Samples_migrated.id'))
    sample_name = Column(String(36))
    sample_type = Column(String(32))
    manipulated = Column(Boolean)
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

    # One-to-one relationship with Sample
    sample = relationship("Sample", back_populates="sampling_data", foreign_keys=[sample_id], single_parent=True)


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
    
    def validate_sample_type(self) -> bool:
        """ Validate the sample type. """
        if not self.sample_type:
            logging.error("Sample type cannot be empty.")
            return False
        # Check against SampleTypeEnum values
        if self.sample_type.lower() not in [sample_type.value.lower() for sample_type in SampleTypeEnum]:
            logging.error(f"The sample type '{self.sample_type}' is not a valid value.")
            return False
        return True


class SequencingData(Base):
    __tablename__ = 'SequencingData'
    id = Column(UUID(as_uuid=True), primary_key=True)
    sample_id = Column(UUID(as_uuid=True), ForeignKey('Samples_migrated.id'))
    sequencing_platform = Column(String(32))
    target_gene = Column(String(32))
    primers = Column(Text)
    primers_sequence = Column(Text)
    extraction_dna_mass = Column(Float)
    extraction_dna_size = Column(Text)
    extraction_dna_method = Column(Text)

    # One-to-one relationship with Sample
    sample = relationship("Sample", back_populates="sequencing_data", foreign_keys=[sample_id], single_parent=True)


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
    
    def validate_sequencing_platform(self) -> bool:
        if not self.sequencing_platform:
            logging.error("Sequencing platform cannot be empty.")
            return False
        # Check against SequencingPlatformEnum values
        if self.sequencing_platform.lower() not in [sequencing_platform.value.lower() for sequencing_platform in SequencingPlatformEnum]:
            logging.error(f"The sequencing platform '{self.sequencing_platform}' is not a valid value.")
            return False
        return True

    def validate_target_gene(self) -> bool:
        if not self.target_gene:
            logging.error("Target gene cannot be empty.")
            return False
        # Check against TargetEnum values
        if self.target_gene.lower() not in [target_gene.value.lower() for target_gene in TargetEnum]:
            logging.error(f"The target gene '{self.target_gene}' is not a valid value.")
            return False
        return True
    

    
class Message(Base):
    __tablename__ = 'messages'
    id = Column(String(255), primary_key=True)
    email = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=True)
    message = Column(Text, nullable=False)  # or Text, depending on the expected length
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
    id = Column(String(255), primary_key=True)
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


class Taxonomy(Base):
    __tablename__ = 'taxonomy_migrated' #TODO: change to table name to "taxonomy" when switching to production
    
    id = Column(UUID(as_uuid=True), primary_key=True)
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


class SH(Base):
    __tablename__ = 'sh_migrated' #TODO: change to table name to "sh" when switching to production
    
    id = Column(UUID(as_uuid=True), primary_key=True)
    sh_name = Column(String(255), nullable=True)
    sample_id = Column(UUID(as_uuid=True), nullable=True)
    abundance = Column(Integer, nullable=True)
    variants = Column(Integer, nullable=True)

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

class Variant(Base):
    __tablename__ = 'variants_migrated' #TODO: change to table name to "variants" when switching to production
    id = Column(UUID(as_uuid=True), primary_key=True)
    sequence = Column(Text, nullable=False)
    abundance = Column(Integer, nullable=False) # most popular = 1, assume NULL on db level
    marker = Column(String(255), nullable=False)
    sh = Column(String(255), nullable=False) 


class Database:
    def __init__(self):
        logger.info("Initializing PostGISDatabase instance.")
        # Construct the database URL for MariaDB
        db_url = f"mysql+pymysql://{config.DBConfig.user}:{config.DBConfig.password}@{config.DBConfig.host}"
        
        # Create the SQLAlchemy engine
        self.engine = create_engine(db_url)
        
        # Create session factory bound to this engine
        self.Session = sessionmaker(bind=self.engine)


    def execute_sql_file(self, filepath):
        logger.info(f"Executing SQL file: {filepath}")
        with open(filepath, 'r') as f:
            sql_content = f.read()

        # Split SQL statements

        sql_statements = [statement.strip() for statement in sql_content.split(';') if statement.strip()]
        
        with self.engine.begin() as connection:  # begin a new transaction
            for statement in sql_statements:
                # Skip empty statements
                if statement.strip():
                    try:
                        connection.execute(text(statement))  # execute the statement
                        logger.info(f"Successfully executed SQL statement: {statement}")
                    except Exception as e:
                        logger.error(f"An error occurred while executing SQL statement: {statement}. Error: {e}")
                        connection.rollback()  # roll back the transaction if error
                    else:
                        connection.commit()  # commit the transaction


    def add_record(self, record):
        logger.info("Adding a new record.")
        session = self.Session()
        try:
            session.add(record)
            session.commit()
            logger.info("Record added successfully.")
        except Exception as e:
            session.rollback()
            logger.error(f"An error occurred: {e}")
        finally:
            session.close()

    def add_records(self, records):
        logger.info("Adding multiple records.")
        session = self.Session()
        try:
            session.add_all(records)
            session.commit()
            logger.info("Records added successfully.")
        except Exception as e:
            session.rollback()
            logger.error(f"An error occurred: {e}")
        finally:
            session.close()
        
    def query_all(self, model):
        logger.info(f"Querying all records from {model.__name__}.")
        session = self.Session()
        try:
            records = session.query(model).all()
            logger.info(f"Successfully queried all records from {model.__name__}.")
            return records
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        finally:
            session.close()

    def query_filter(self, model, filter_expression):
        logger.info(f"Querying records from {model.__name__} with filtering.")
        session = self.Session()
        try:
            records = session.query(model).filter(filter_expression).all()
            logger.info(f"Successfully queried records from {model.__name__} with filtering.")
            return records
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        finally:
            session.close()

    def update_record(self, model, filter_expression, update_values):
        logger.info(f"Updating a record in {model.__name__}.")
        session = self.Session()
        try:
            record = session.query(model).filter(filter_expression).first()
            for key, value in update_values.items():
                setattr(record, key, value)
            session.commit()
            logger.info(f"Successfully updated a record in {model.__name__}.")
        except Exception as e:
            session.rollback()
            logger.error(f"An error occurred: {e}")
        finally:
            session.close()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(255), nullable=False)
    paper_id = Column(UUID(as_uuid=True), ForeignKey('Paper.id', ondelete='IGNORE'))


    def __repr__(self):
        return f"<Author(id='{self.id}', name='{self.name}', paper_id='{self.paper_id}')>"
    
    def to_dict(self):
        return {
            'id': str(self.id),  # Convert UUID to string
            'name': self.name,
            'paper_id': str(self.paper_id)  # Convert UUID to string
        }
    
    def to_json(self):
        return json.dumps(self.to_dict(), default=str)