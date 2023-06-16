from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField
from django.db import models
from enum import Enum
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Biome(Enum):
    AQUATIC = 'aquatic'
    DESERT = 'desert'
    GRASSLAND = 'grassland'
    FOREST = 'forest'
    TUNDRA = 'tundra'
    CROPLAND = 'cropland'
    WETLAND = 'wetland'
    WOODLAND = 'woodland'
    SHRUBLAND = 'shrubland'
    MANGROVE = 'mangrove'
    ANTHROPOGENIC = 'anthropogenic'

class SequencingPlatform(Enum):
    ILLUMINA = 'Illumina'
    ROCH454 = '454Roche'
    PACBIO = 'PacBio'
    IONTORRENT = 'IonTorrent'
    SOLID = 'SOLiD'
    OXFORDNANOPORE = 'Oxford Nanopore'

class TargetGene(Enum):
    ITS1 = 'ITS1'
    ITS2 = 'ITS2'
    ITSBOTH = 'ITSboth'


class Continent(Enum):
    AFRICA = 'Africa'
    ANTARCTICA = 'Antarctica'
    ASIA = 'Asia'
    AUSTRALIA = 'Australia'
    EUROPE = 'Europe'
    NORTH_AMERICA = 'North America'
    SOUTH_AMERICA = 'South America'
    ATLANTIC_OCEAN = 'Atlantic Ocean'
    ARCTIC_OCEAN = 'Arctic Ocean'
    INDIAN_OCEAN = 'Indian Ocean'
    PACIFIC_OCEAN = 'Pacific Ocean'
    SOUTHERN_OCEAN = 'Southern Ocean'

class SampleType(Enum):
    SOIL = 'soil'
    RHIZOSPHERE_SOIL = 'rhizosphere soil'
    LITTER = 'litter'
    TOPSOIL = 'topsoil'
    DEADWOOD = 'deadwood'
    LICHEN = 'lichen'
    SHOOT = 'shoot'
    ROOT = 'root'
    AIR = 'air'
    DUST = 'dust'
    WATER = 'water'
    SEDIMENT = 'sediment'
    FUNGAL_SPOROCARP = 'fungal sporocarp'

class Paper(models.Model):
    paper_id = models.CharField(max_length=32, primary_key=True)
    title = models.TextField()
    year = models.DateField()
    authors = models.TextField()
    journal = models.TextField()
    doi = models.TextField()
    contact = models.EmailField()
    mat_study = models.FloatField()
    map_study = models.FloatField()
    submitted_by_user = models.BooleanField()

class GeoData(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    continent = models.CharField(
        max_length=32,
        choices=[(tag, tag.value) for tag in Continent]
    )
    location = models.TextField()
    area_gps = models.FloatField()
    country = CountryField()

class ChemicalData(models.Model):
    total_c_content = models.FloatField()
    total_n_content = models.FloatField()
    organic_matter_content = models.FloatField()
    ph = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(14)])
    ph_method = models.CharField(max_length=64)
    total_ca = models.FloatField()
    total_p = models.FloatField()
    total_k = models.FloatField()

class TaxonomyData(models.Model): 
    ecology = models.CharField(max_length=64,blank=True, null=True)  
    kingdom = models.CharField(max_length=64,blank=True, null=True)  
    phylum = models.CharField(max_length=64,blank=True, null=True)  
    classis = models.CharField(max_length=64,blank=True, null=True)
    order = models.CharField(max_length=64,blank=True, null=True)  
    family = models.CharField(max_length=64,blank=True, null=True)  
    genus = models.CharField(max_length=64,blank=True, null=True)  
    species = models.CharField(max_length=64,blank=True, null=True)
    species_hypothesis = models.CharField(max_length=32,blank=True, null=True) 
    biome = models.CharField(
        max_length=32,
        choices=[(tag, tag.value) for tag in Biome]
    )
    biome_detail = models.TextField()
    plants_dominant = models.TextField(blank=True, null=True)
    plants_all = models.TextField(blank=True, null=True)

class VariantsData(models.Model):
    its1_extracted = models.IntegerField(blank=True, null=True)
    its2_extracted = models.IntegerField(blank=True, null=True)
    its_total = models.IntegerField()

class SamplingData(models.Model):
    sample_name = models.TextField()
    sample_type = models.CharField(
        max_length=32,
        choices=[(tag, tag.value) for tag in SampleType]
    )
    manipulated = models.BooleanField()
    sample_typed_detailed = models.TextField()
    date_of_sampling = models.DateField()
    area_sampled = models.FloatField()
    number_of_subsamples = models.PositiveIntegerField()
    sampling_info = models.TextField()
    sample_depth = models.FloatField()
    mat = models.FloatField()
    map = models.FloatField()
    sample_seqid = models.TextField()
    sample_barcode = models.TextField()

class SequencingData(models.Model):
    sequencing_platform = models.CharField(
        max_length=32,
        choices=[(tag, tag.value) for tag in SequencingPlatform]
    )
    target_gene = models.CharField(
        max_length=32,
        choices=[(tag, tag.value) for tag in TargetGene]
    )
    primers = models.TextField()
    primers_sequence = models.TextField()
    extraction_dna_mass = models.FloatField()
    extraction_dna_size = models.TextField()
    extraction_dna_method = models.TextField()

class Sample(models.Model):
    id = models.AutoField(primary_key=True)
    add_date = models.DateField()
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='samples')
    geodata = models.ForeignKey(GeoData, on_delete=models.CASCADE, related_name='samples')
    chemical_data = models.ForeignKey(ChemicalData, on_delete=models.CASCADE, related_name='samples')
    taxonomy_data = models.ForeignKey(TaxonomyData, on_delete=models.CASCADE, related_name='samples')
    variants_data = models.ForeignKey(VariantsData, on_delete=models.CASCADE, related_name='samples')
    sampling_data = models.ForeignKey(SamplingData, on_delete=models.CASCADE, related_name='samples')
    sequencing_data = models.ForeignKey(SequencingData, on_delete=models.CASCADE, related_name='samples')
    sample_info = models.TextField()


class DatabaseReleaseInfo(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the GlobalFungi database.")
    version = models.CharField(max_length=20, validators=[RegexValidator(r'^\d+\.\d+\.\d+$')], help_text="Version of the GlobalFungi database following semantic versioning.")
    release = models.CharField(max_length=20, validators=[RegexValidator(r'^\d+\.\d+\.\d+$')], help_text="Release version.")
    unite_version = models.CharField(max_length=20, validators=[RegexValidator(r'^\d+\.\d+\.\d+$')], help_text="UNITE version used in the GlobalFungi database.")
    its_variants_count = models.BigIntegerField(help_text="Count of ITS variants in the GlobalFungi database.")
    its1_raw_count = models.BigIntegerField(help_text="Raw count of ITS1 in the GlobalFungi database.")
    its2_raw_count = models.BigIntegerField(help_text="Raw count of ITS2 in the GlobalFungi database.")
    details = models.TextField(help_text="Detailed information about the GlobalFungi database release.")
    citation = models.TextField(help_text="Citation for the GlobalFungi database.")
    date = models.DateField(help_text="Release date of the GlobalFungi database.")

    class Meta:
        db_table = 'info'


class Maillist(models.Model):
    name = models.TextField()
    email = models.TextField()
    date = models.DateTimeField()

    class Meta:
        db_table = 'maillist'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.subject})"


class GlobalFungiUser(AbstractUser):
    ORCID_REGEX = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    ROLES = [
        ('undergraduate', 'Undergraduate Student'),
        ('master', 'Master Student'),
        ('phd', 'PhD Student'),
        ('researcher', 'Researcher'),
        ('other', 'Other')
    ]

    orcid = models.CharField(
        max_length=19,
        validators=[RegexValidator(
            ORCID_REGEX,
            'Enter a valid ORCID. Format: 0000-0000-0000-0000'
        )],
        unique=True
    )
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=128)
    affiliation_institute = models.CharField(max_length=128)
    is_contributor = models.BooleanField(default=False)
    role = models.CharField(max_length=14, choices=ROLES, null=True, blank=True)
    other_role = models.CharField(max_length=50, blank=True, null=True)
    field_of_study = models.CharField(max_length=100, null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="globalfungi_user_set",
        related_query_name="globalfungi_user",
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="globalfungi_user_set",
        related_query_name="globalfungi_user",
    )


class SubmittedStudy(models.Model):
    contributor = models.ForeignKey(GlobalFungiUser, on_delete=models.CASCADE)
    title = models.TextField()
    authors = models.TextField()
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2099)])
    journal = models.CharField(
        max_length=100,
        validators=[RegexValidator(r'^\w+$', 'Enter a valid journal name. No special characters allowed.')]
    )
    volume = models.CharField(max_length=30)
    pages = models.CharField(
        max_length=100,
    )
    doi = models.TextField()
    repository = models.TextField()
    allowed_to_show = models.BooleanField(default=False)
    mat_study = models.FloatField()
    map_study = models.FloatField()
    submitted_by_user = models.BooleanField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'study'
