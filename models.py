# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class Genus(models.Model):
    genus = models.CharField(max_length=32)
    samples = models.TextField()
    abundances = models.TextField()
    vars = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'genus'


class GlobalfungiAbundance(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'globalfungi_abundance'


class GlobalfungiChemicaldata(models.Model):
    id = models.BigAutoField(primary_key=True)
    total_c_content = models.FloatField()
    total_n_content = models.FloatField()
    organic_matter_content = models.FloatField()
    ph = models.FloatField()
    ph_method = models.CharField(max_length=64)
    total_ca = models.FloatField()
    total_p = models.FloatField()
    total_k = models.FloatField()

    class Meta:
        managed = False
        db_table = 'globalfungi_chemicaldata'


class GlobalfungiContactmessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'globalfungi_contactmessage'


class Info(models.Model):
    name = models.TextField()
    version = models.TextField()
    release = models.TextField()
    unite_version = models.TextField()
    its_variants_count = models.BigIntegerField()
    its1_raw_count = models.BigIntegerField()
    its2_raw_count = models.BigIntegerField()
    info = models.TextField()
    citation = models.TextField()
    date = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'info'


class Maillist(models.Model):
    name = models.TextField()
    email = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maillist'


class Messages(models.Model):
    email = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    processed = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages'


class Metadata(models.Model):
    paper_study = models.CharField(max_length=32)
    longitude = models.FloatField()
    latitude = models.FloatField()
    elevation = models.CharField(max_length=32)
    continent = models.CharField(max_length=32)
    country = models.TextField()
    location = models.TextField()
    sample_type = models.TextField()
    biome = models.TextField(db_column='Biome')  # Field name made lowercase.
    biome_detail = models.TextField(db_column='Biome_detail')  # Field name made lowercase.
    mat_study = models.CharField(db_column='MAT_study', max_length=32)  # Field name made lowercase.
    map_study = models.CharField(db_column='MAP_study', max_length=32)  # Field name made lowercase.
    sample_name = models.TextField()
    area_sampled = models.CharField(max_length=32)
    area_gps = models.CharField(db_column='area_GPS', max_length=32)  # Field name made lowercase.
    number_of_subsamples = models.CharField(max_length=32)
    sample_depth = models.CharField(max_length=32)
    year_of_sampling = models.CharField(max_length=32)
    month_of_sampling = models.CharField(max_length=32)
    day_of_sampling = models.CharField(max_length=32)
    sampling_info = models.TextField()
    sample_description = models.TextField()
    sequencing_platform = models.CharField(max_length=32)
    target_gene = models.CharField(max_length=32)
    extraction_dna_mass = models.CharField(db_column='extraction_DNA_mass', max_length=32)  # Field name made lowercase.
    extraction_dna_size = models.TextField(db_column='extraction_DNA_size')  # Field name made lowercase.
    extraction_dna_method = models.TextField(db_column='extraction_DNA_method')  # Field name made lowercase.
    primers = models.TextField()
    primers_sequence = models.TextField()
    ph = models.CharField(db_column='pH', max_length=32)  # Field name made lowercase.
    ph_method = models.CharField(db_column='pH_method', max_length=64)  # Field name made lowercase.
    organic_matter_content = models.CharField(max_length=32)
    total_c_content = models.CharField(db_column='total_C_content', max_length=32)  # Field name made lowercase.
    total_n_content = models.CharField(db_column='total_N_content', max_length=32)  # Field name made lowercase.
    total_p = models.CharField(db_column='total_P', max_length=32)  # Field name made lowercase.
    total_ca = models.CharField(db_column='total_Ca', max_length=32)  # Field name made lowercase.
    total_k = models.CharField(db_column='total_K', max_length=32)  # Field name made lowercase.
    plants_dominant = models.TextField()
    plants_all = models.TextField()
    sample_info = models.TextField()
    sample_seqid = models.TextField()
    sample_barcode = models.TextField()

    class Meta:
        managed = False
        db_table = 'metadata'


class Samples(models.Model):
    id = models.IntegerField(primary_key=True)
    add_date = models.CharField(max_length=10)
    paper_id = models.CharField(max_length=32)
    title = models.TextField()
    year = models.CharField(max_length=4)
    authors = models.TextField()
    journal = models.TextField()
    doi = models.TextField()
    contact = models.TextField()
    sample_name = models.TextField()
    sample_type = models.TextField()
    manipulated = models.CharField(max_length=5)
    sample_description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    continent = models.CharField(max_length=32)
    year_of_sampling = models.CharField(max_length=32)
    biome = models.TextField(db_column='Biome')  # Field name made lowercase.
    sequencing_platform = models.CharField(max_length=32)
    target_gene = models.CharField(max_length=32)
    primers = models.TextField()
    primers_sequence = models.TextField()
    sample_seqid = models.TextField()
    sample_barcode = models.TextField()
    elevation = models.CharField(max_length=32)
    mat = models.CharField(db_column='MAT', max_length=32)  # Field name made lowercase.
    map = models.CharField(db_column='MAP', max_length=32)  # Field name made lowercase.
    mat_study = models.CharField(db_column='MAT_study', max_length=32)  # Field name made lowercase.
    map_study = models.CharField(db_column='MAP_study', max_length=32)  # Field name made lowercase.
    biome_detail = models.TextField(db_column='Biome_detail')  # Field name made lowercase.
    country = models.TextField()
    month_of_sampling = models.CharField(max_length=32)
    day_of_sampling = models.CharField(max_length=32)
    plants_dominant = models.TextField()
    plants_all = models.TextField()
    area_sampled = models.CharField(max_length=32)
    number_of_subsamples = models.CharField(max_length=32)
    sampling_info = models.TextField()
    sample_depth = models.CharField(max_length=32)
    extraction_dna_mass = models.CharField(db_column='extraction_DNA_mass', max_length=32)  # Field name made lowercase.
    extraction_dna_size = models.TextField(db_column='extraction_DNA_size')  # Field name made lowercase.
    extraction_dna_method = models.TextField(db_column='extraction_DNA_method')  # Field name made lowercase.
    total_c_content = models.CharField(db_column='total_C_content', max_length=32)  # Field name made lowercase.
    total_n_content = models.CharField(db_column='total_N_content', max_length=32)  # Field name made lowercase.
    organic_matter_content = models.CharField(max_length=32)
    ph = models.CharField(db_column='pH', max_length=32)  # Field name made lowercase.
    ph_method = models.CharField(db_column='pH_method', max_length=64)  # Field name made lowercase.
    total_ca = models.CharField(db_column='total_Ca', max_length=32)  # Field name made lowercase.
    total_p = models.CharField(db_column='total_P', max_length=32)  # Field name made lowercase.
    total_k = models.CharField(db_column='total_K', max_length=32)  # Field name made lowercase.
    sample_info = models.TextField()
    location = models.TextField()
    area_gps = models.CharField(db_column='area_GPS', max_length=32)  # Field name made lowercase.
    its1_extracted = models.IntegerField(db_column='ITS1_extracted')  # Field name made lowercase.
    its2_extracted = models.IntegerField(db_column='ITS2_extracted')  # Field name made lowercase.
    its_total = models.IntegerField(db_column='ITS_total')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samples'


class SamplesToSh(models.Model):
    sample = models.IntegerField()
    shs = models.TextField(db_column='SHs')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samples_to_sh'


class Sh(models.Model):
    sh = models.CharField(max_length=32)
    samples = models.TextField()
    abundances = models.TextField()
    vars = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh'


class Species(models.Model):
    species = models.CharField(max_length=64)
    samples = models.TextField()
    abundances = models.TextField()
    vars = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'species'


class Study(models.Model):
    hash = models.CharField(primary_key=True, max_length=32)
    contributor = models.TextField()
    email = models.TextField()
    affiliation_institute = models.TextField()
    affiliation_country = models.TextField()
    orcid = models.TextField(db_column='ORCID')  # Field name made lowercase.
    title = models.TextField()
    authors = models.TextField()
    year = models.TextField()
    journal = models.TextField()
    volume = models.TextField()
    pages = models.TextField()
    doi = models.TextField()
    repository = models.TextField()
    include = models.TextField()
    coauthor = models.TextField()
    email_confirmed = models.IntegerField()
    submission_finished = models.IntegerField()
    date = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'study'


class Taxonomy(models.Model):
    sh = models.CharField(db_column='SH', max_length=32)  # Field name made lowercase.
    ecology = models.CharField(db_column='Ecology', max_length=64)  # Field name made lowercase.
    kingdom = models.CharField(db_column='Kingdom', max_length=64)  # Field name made lowercase.
    phylum = models.CharField(db_column='Phylum', max_length=64)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=64)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    order = models.CharField(db_column='Order', max_length=64)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=64)  # Field name made lowercase.
    genus = models.CharField(db_column='Genus', max_length=64)  # Field name made lowercase.
    species = models.CharField(db_column='Species', max_length=64)  # Field name made lowercase.
    genus_id = models.IntegerField()
    species_id = models.IntegerField()
    sh_id = models.IntegerField(db_column='SH_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxonomy'


class Traffic(models.Model):
    session = models.IntegerField()
    category = models.CharField(max_length=32, blank=True, null=True)
    value = models.CharField(max_length=64, blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'traffic'


class Variants(models.Model):
    hash = models.CharField(max_length=32)
    samples = models.TextField()
    abundances = models.TextField()
    marker = models.CharField(max_length=4)
    sh = models.IntegerField(db_column='SH')  # Field name made lowercase.
    species = models.IntegerField()
    genus = models.IntegerField()
    sequence = models.TextField()

    class Meta:
        managed = False
        db_table = 'variants'
