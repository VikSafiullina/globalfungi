from django.db import models
import uuid
from django.contrib.gis.db import models
import time


class BiomeEnum(models.TextChoices):
    DESERT = 'desert', 'Desert'
    FOREST = 'forest', 'Forest'
    OCEAN = 'ocean', 'Ocean'
    MOUNTAIN = 'mountain', 'Mountain'
    OTHER = 'other', 'Other'

class PhMethodEnum(models.TextChoices):
    water = 'H2O', 'H20'
    potassium_chloride = 'KCl', 'KCl'


class PhMethodEnum():
    KCL = "KCl"
    H2O = "H2O"
    #TODO: reassure from the dump

class DepthEnum():
    CM = 'cm'

class SampleTypeEnum():
    ROOT = 'root'
    SOIL = 'soil'
    # TODO: init properly based on the unique constraints

class BiomeEnum():
    # TODO: unique constraints from db

class SequencingPlatformEnum():
    #TODO:

class TargetEnum():
    ITS1 = 'its1'
    ITS2 = 'its2'
    ITS1_ITS2 = 'its1,its2'

class ElevationEnum():
    M = 'm'

class MATEnum():
    CELSIUS = 'Celsius'

class MAPEnum():
    MM = 'mm'

class BiomeDetailedEnum():
    # TODO: add entities

class AreaEnum():
    M2 = 'm2'


class Author(models.Model):
    id = models.UUIDField()
    name = models.CharField()
    surname = models.CharField()
    email = models.EmailField(null=True, blank=True)


class Paper(models.Model):
    id = models.UUIDField()
    title = models.TextField()
    authors = models.ManyToManyField(Author, related_name='Paper')
    publication_year = models.DateField()
    journal = models.TextField()
    DOI = models.CharField(max_length=256, ensure_unique=True)
    sampled_area = models.FloatField(null=False,default=-1)
    sampled_area_units = models.CharField(
        choices=AreaEnum.choices,
    )
    #area_gps - to drop? TODO: reassure


class Sample(models.Model):
    id = models.UUIDField()
    created_at = models.DateTimeField(default=time.Now())
    paper_id = models.ForeignKey(Paper)
    species_hypothesis = models.ManyToManyField(TaxonomyData, related_name='SH')

    # samplename interni - as a display name
    sample_type = models.CharField(
        choices=SampleTypeEnum.choices
    )
    biome = models.CharField(
        choices=BiomeEnum.choices,
        default=None
    )
    biome_detailed = models.CharField(
        choices=BiomeDetailedEnum.choices,
    )



class GeographicalData(models.Model):
    id = models.UUIDField()
    sample_id = models.ForeignKey(Sample)
    location = models.PointField()
    elevation = models.IntegerField()
    elevation_units = models.CharField(
        choices=ElevationEnum.choices
    )
    #geocode_location - osmx.geocode("lot,lat") - to be rendered on a FE

class SamplingData(models.Model):
    id = models.UUIDField()
    sample_id = models.ForeignKey(Sample)

    date_of_sampling = models.DateField() #TODO: think of non-existing values
    is_natural_conds = models.BooleanField(default=True) # whether the sample was manipulated
    mean_annual_temp_calculated = models.FloatField
    MAT_units = models.CharField(
        choices=MATEnum.choices
    )
    mean_annual_precipitation_calculated = models.FloatField
    MAP_units = models.CharField(
        choices=MAPEnum.choices
    )
    mean_annual_precipitation_paper = models.FloatField
    mean_annual_temp_paper = models.FloatField
    sample_type_detailed = models.TextField() #ex sample_description 
    min_depth = models.IntegerField(null=True)
    max_depth = models.IntegerField(null=True)
    depth_units = models.CharField(
        choices=DepthEnum.choices,
        null=True
    )
    replicates_count = models.IntegerField(null=True, display_name="Subsamples Count")
    sampling_info = models.TextField() # general additional info about processing of samples


class ChemicalData(models.Model):
    id = models.UUIDField()
    sample_id = models.ForeignKey(Sample)
    ph = models.FloatField(null=True) # NO UNITS
    ph_method = models.CharField(
        choices=PhMethodEnum.choices,
        null=True
    )
    total_carbon_content = models.FloatField(null=True) # TODO: units - percentage from sample mass
    total_nitrogen_content = models.FloatField(null=True) # TODO: units - percentage from sample mass
    total_calcium_content = models.FloatField(null=True) # TODO: units - percent per million (PPM)
    total_potassium_content = models.FloatField(null=True) # TODO: units - percent per million (PPM)
    total_phosphorus_content = models.FloatField(null=True) # TODO: units - percent per million (PPM)

    organic_matter_content = models.FloatField(null=True) # TODO: units - percentage from sample mass


class SequencingData(models.Model):
    id = models.UUIDField()
    sample_id = models.ForeignKey(Sample)

    sequencing_platform = models.CharField(
        choices=SequencingPlatformEnum.choices,
    )

    dna_mass_extracted = models.FloatField() # averaged from origin, in gramms
    dna_size_extracted = models.TextField()
    dna_extraction_method = models.CharField()

    sample_barcode = models.CharField()
    its1_extracted = models.IntegerField(null=False)  # Field name made lowercase.
    its2_extracted = models.IntegerField(null=False)



class TaxonomyData(models.Model):
    sh = models.CharField()
    species = models.CharField()
    genus = models.CharField()
    family = models.CharField()
    order = models.CharField()
    _class = models.CharField()
    phylum = models.CharField()
    kingdom = models.CharField()
    ecology = models.CharField(null=True)


class SampleDescription(models.Model):
    id = models.UUIDField()
    sample_id = models.ForeignKey(Sample)
    external_id = models.CharField(unique=True) # id in external databases, for instance NCBI
    paper_sample_name = models.CharField()
    plants_dominant = models.TextField()
    plants_all  = models.TextField()
    sample_info = models.TextField() # general additional info about samples





class Primer(models.Model):
    id = models.UUIDField()
    name = models.CharField()
    sequence = models.CharField()

class PrimersTuple(models.Model):
    id = models.UUIDField()
    forward_primer = models.ForeignKey(Primer)
    reverse_primer = models.ForeignKey(Primer)

    target_gene = models.CharField(
        choices=TargetEnum.choices)







# TODO  : variant sequence length text or char?
