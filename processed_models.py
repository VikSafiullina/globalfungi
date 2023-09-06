from django.db import models
import uuid
from django.contrib.gis.db import models
import time
from enum import Enum


class BiomeEnum(Enum):
    ANTHROPOGENIC = 'anthropogenic'
    AQUATIC = 'aquatic'
    CROPLAND = 'cropland'
    DESERT = 'desert'
    FOREST = 'forest'
    GRASSLAND = 'grassland'
    MANGROVE = 'mangrove'
    SHRUBLAND = 'shrubland'
    TUNDRA = 'tundra'
    WETLAND = 'wetland'
    WOODLAND = 'woodland'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]



class PhMethodEnum(Enum):
    CACL2 = 'CaCl2'
    H2O = 'H2O'
    IN_SITU = 'in situ'
    KCL = 'KCl'
    NA_ = 'NA_'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class DepthEnum():
    CM = 'cm'


class SampleTypeEnum(Enum):
    AIR = 'air'
    CORAL = 'coral'
    DEADWOOD = 'deadwood'
    DUST = 'dust'
    LICHEN = 'lichen'
    LITTER = 'litter'
    RHIZOSPHERE_SOIL = 'rhizosphere soil'
    ROOT = 'root'
    ROOT_RHIZOSPHERE_SOIL = 'root+rhizosphere soil'
    SEDIMENT = 'sediment'
    SHOOT = 'shoot'
    SOIL = 'soil'
    TOPSOIL = 'topsoil'
    WATER = 'water'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class SequencingPlatformEnum(Enum):
    ROCH454 = '454Roche'
    DNBSEQ_G400 = 'DNBSEQ-G400'
    ILLUMINA = 'Illumina'
    IONTORRENT = 'IonTorrent'
    PACBIO = 'PacBio'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]



class TargetEnum(Enum):
    ITS1 = 'ITS1'
    ITS2 = 'ITS2'
    ITSBOTH = 'ITSboth'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class ElevationEnum():
    M = 'm'

class MATEnum():
    CELSIUS = 'Celsius'

class MAPEnum():
    MM = 'mm'


class BiomeDetailedEnum(Enum):
    MARINE_BIOME = 'marine biome'
    AGRICULTURAL_ECOSYSTEM = 'agricultural ecosystem'
    ALPINE_GRASSLAND = 'alpine grassland'
    ALPINE_TUNDRA = 'alpine tundra'
    ALPINE_TUNDRA_BIOME = 'alpine tundra biome'
    ALPINE_TUNDRA_ECOSYSTEM = 'alpine tundra ecosystem'
    ANTHROPOGENIC_TERRESTRIAL_BIOME = 'anthropogenic terrestrial biome'
    AREA_OF_DECIDUOUS_FOREST = 'area of deciduous forest'
    BANANA_PLANTATION = 'banana plantation'
    BROADLEAF_FOREST_BIOME = 'broadleaf forest biome'
    COASTAL_WETLAND_ECOSYSTEM = 'coastal wetland ecosystem'
    COFFEE_PLANTATION = 'coffee plantation'
    CONIFEROUS_FOREST = 'coniferous forest'
    CONIFEROUS_FOREST_BIOME = 'coniferous forest biome'
    CROPLAND = 'cropland'
    CROPLAND_BIOME = 'cropland biome'
    CROPLAND_ECOSYSTEM = 'cropland ecosystem'
    DENSE_SETTLEMENT_BIOME = 'dense settlement biome'
    DESERT = 'desert'
    DESERT_BIOME = 'desert biome'
    DISTURBED_ECOSYSTEM = 'disturbed ecosystem'
    ESTUARINE_BIOME = 'estuarine biome'
    FLOODED_GRASSLAND_BIOME = 'flooded grassland biome'
    FLOODED_SAVANNA_BIOME = 'flooded savanna biome'
    FOREST = 'forest'
    FOREST_BIOME = 'forest biome'
    FOREST_ECOSYSTEM = 'forest ecosystem'
    FRESHWATER_BIOME = 'freshwater biome'
    FRESHWATER_LAKE_BIOME = 'freshwater lake biome'
    FRESHWATER_RIVER_BIOME = 'freshwater river biome'
    FRESHWATER_WETLAND_ECOSYSTEM = 'freshwater wetland ecosystem'
    GRASSLAND = 'grassland'
    GRASSLAND_BIOME = 'grassland biome'
    GRASSLAND_ECOSYSTEM = 'grassland ecosystem'
    INTERTIDAL_ECOSYSTEM = 'intertidal ecosystem'
    LARGE_LAKE_BIOME = 'large lake biome'
    MANGROVE_BIOME = 'mangrove biome'
    MARINE_ABYSSAL_ZONE_BIOME = 'marine abyssal zone biome'
    MARINE_BATHYAL_ZONE_BIOME = 'marine bathyal zone biome'
    MARINE_BENTHIC_BIOME = 'marine benthic biome'
    MARINE_BIOME = 'marine biome'
    MARINE_CORAL_REEF_BIOME = 'marine coral reef biome'
    MARINE_HYDROTHERMAL_VENT_BIOME = 'marine hydrothermal vent biome'
    MARINE_NERITIC_BENTHIC_ZONE_BIOME = 'marine neritic benthic zone biome'
    MARINE_SALT_MARSH_BIOME = 'marine salt marsh biome'
    MEADOW_ECOSYSTEM = 'meadow ecosystem'
    MEDITERANEAN_SHRUBLAND_BIOME = 'mediteranean shrubland biome'
    MEDITERRANEAN_FOREST_BIOME = 'mediterranean forest biome'
    MEDITERRANEAN_SHRUBLAND_BIOME = 'mediterranean shrubland biome'
    MIXED_FOREST = 'mixed forest'
    MIXED_FOREST_BIOME = 'mixed forest biome'
    MONTANE_DESERT_BIOME = 'montane desert biome'
    MONTANE_FOREST = 'montane forest'
    MONTANE_GRASSLAND = 'montane grassland'
    MONTANE_GRASSLAND_BIOME = 'montane grassland biome'
    MONTANE_SHRUBLAND_BIOME = 'montane shrubland biome'
    PASTURE = 'pasture'
    PEAT_SWAMP = 'peat swamp'
    PLANTATION = 'plantation'
    PLANTATIONS = 'plantations'
    PLANTED_FOREST = 'planted forest'
    POLAR_DESERT = 'polar desert'
    POLAR_DESERT_BIOME = 'polar desert biome'
    POLAR_TUNDRA_ECOSYSTEM = 'polar tundra ecosystem'
    PRAIRIE = 'prairie'
    PRIMARY_FOREST = 'primary forest'
    RANGELAND_BIOME = 'rangeland biome'
    RICE_FIELD = 'rice field'
    SALINE_MARSH = 'saline marsh'
    SAVANNA_BIOME = 'savanna biome'
    SHRUBLAND = 'shrubland'
    SHRUBLAND_BIOME = 'shrubland biome'
    SPHAGNUM_BOG = 'sphagnum bog'
    SUBPOLAR_CONIFEROUS_FOREST_BIOME = 'subpolar coniferous forest biome'
    SUBTROPICAL_BROADLEAF_FOREST_BIOME = 'subtropical broadleaf forest biome'
    SUBTROPICAL_CONIFEROUS_FOREST_BIOME = 'subtropical coniferous forest biome'
    SUBTROPICAL_DESERT_BIOME = 'subtropical desert biome'
    SUBTROPICAL_FOREST = 'subtropical forest'
    SUBTROPICAL_MIXED_FOREST = 'subtropical mixed forest'
    SUBTROPICAL_MOIST_BROADLEAF_FOREST_BIOME = 'subtropical moist broadleaf forest biome'
    SUBTROPICAL_SHRUBLAND_BIOME = 'subtropical shrubland biome'
    TEMPERATE_BROADLEAF_EVERGREEN_FOREST = 'temperate broadleaf evergreen forest'
    TEMPERATE_BROADLEAF_FOREST = 'temperate broadleaf forest'
    TEMPERATE_BROADLEAF_FOREST_BIOME = 'temperate broadleaf forest biome'
    TEMPERATE_CONIFEROUS_FOREST_BIOME = 'temperate coniferous forest biome'
    TEMPERATE_DECIDUOUS_BROADLEAF_FOREST = 'temperate deciduous broadleaf forest'
    TEMPERATE_DECIDUOUS_NEEDLELEAF_FOREST = 'temperate deciduous needleleaf forest'
    TEMPERATE_DESERT_BIOME = 'temperate desert biome'
    TEMPERATE_EVERGREEN_NEEDLELEAF_FOREST = 'temperate evergreen needleleaf forest'
    TEMPERATE_FOREST = 'temperate forest'
    TEMPERATE_GRASSLAND = 'temperate grassland'
    TEMPERATE_GRASSLAND_BIOME = 'temperate grassland biome'
    TEMPERATE_MIXED_BROADLEAF_FOREST = 'temperate mixed broadleaf forest'
    TEMPERATE_MIXED_FOREST = 'temperate mixed forest'
    TEMPERATE_MIXED_FOREST_BIOME = 'temperate mixed forest biome'
    TEMPERATE_MIXED_NEEDLELEAF_FOREST = 'temperate mixed needleleaf forest'
    TEMPERATE_SHRUBLAND_BIOME = 'temperate shrubland biome'
    TEMPERATE_WOODLAND_BIOME = 'temperate woodland biome'
    TROPICAL_BROADLEAF_FOREST_BIOME = 'tropical broadleaf forest biome'
    TROPICAL_DECIDUOUS_BROADLEAF_FOREST = 'tropical deciduous broadleaf forest'
    TROPICAL_DRY_BROADLEAF_FOREST_BIOME = 'tropical dry broadleaf forest biome'
    TROPICAL_FOREST = 'tropical forest'
    TROPICAL_GRASSLAND = 'tropical grassland'
    TROPICAL_GRASSLAND_BIOME = 'tropical grassland biome'
    TROPICAL_LOWER_MONTANE_FOREST = 'tropical lower montane forest'
    TROPICAL_LOWLAND_EVERGREEN_BROADLEAF_RAIN_FOREST = 'tropical lowland evergreen broadleaf rain forest'
    TROPICAL_MIXED_FOREST_BIOME = 'tropical mixed forest biome'
    TROPICAL_MOIST_BROADLEAF_FOREST = 'tropical moist broadleaf forest'
    TROPICAL_MOIST_BROADLEAF_FOREST_BIOME = 'tropical moist broadleaf forest biome'
    TROPICAL_SEMI_EVERGREEN_MOIST_BROADLEAF_FOREST = 'tropical semi-evergreen moist broadleaf forest'
    TROPICAL_SHRUBLAND_BIOME = 'tropical shrubland biome'
    TROPICAL_WOODLAND_BIOME = 'tropical woodland biome'
    TUNDRA_BIOME = 'tundra biome'
    TUNDRA_ECOSYSTEM = 'tundra ecosystem'
    URBAN_BIOME = 'urban biome'
    VILLAGE_BIOME = 'village biome'
    VINEYARD = 'vineyard'
    WET_MEADOW_ECOSYSTEM = 'wet meadow ecosystem'
    WETLAND_ECOSYSTEM = 'wetland ecosystem'
    WOODLAND_BIOME = 'woodland biome'
    WOODLAND_ECOSYSTEM = 'woodland ecosystem'
    XERIC_BASIN_BIOME = 'xeric basin biome'
    XERIC_SHRUBLAND_BIOME = 'xeric shrubland biome'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


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
