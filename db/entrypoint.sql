-- MariaDB dump 10.19-11.1.2-MariaDB, for osx10.18 (arm64)
--
-- Host: localhost    Database: globalfungitest
-- ------------------------------------------------------
-- Server version	11.1.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `info`
--

DROP TABLE IF EXISTS `info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `info` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `version` text NOT NULL,
  `release` text NOT NULL,
  `unite_version` text NOT NULL,
  `its_variants_count` bigint(20) NOT NULL,
  `its1_raw_count` bigint(20) NOT NULL,
  `its2_raw_count` bigint(20) NOT NULL,
  `info` text NOT NULL,
  `citation` text NOT NULL,
  `date` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `maillist`
--

DROP TABLE IF EXISTS `maillist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maillist` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `email` text NOT NULL,
  `subject` text NOT NULL,
  `message` text NOT NULL,
  `processed` tinyint(1) NOT NULL DEFAULT 0,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `metadata`
--

DROP TABLE IF EXISTS `metadata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `metadata` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `paper_study` varchar(32) NOT NULL,
  `longitude` float NOT NULL,
  `latitude` float NOT NULL,
  `elevation` varchar(32) NOT NULL,
  `continent` varchar(32) NOT NULL,
  `country` text NOT NULL,
  `location` text NOT NULL,
  `sample_type` text NOT NULL,
  `Biome` text NOT NULL,
  `Biome_detail` text NOT NULL,
  `MAT_study` varchar(32) NOT NULL,
  `MAP_study` varchar(32) NOT NULL,
  `sample_name` text NOT NULL,
  `area_sampled` varchar(32) NOT NULL,
  `area_GPS` varchar(32) NOT NULL,
  `number_of_subsamples` varchar(32) NOT NULL,
  `sample_depth` varchar(32) NOT NULL,
  `year_of_sampling` varchar(32) NOT NULL,
  `month_of_sampling` varchar(32) NOT NULL,
  `day_of_sampling` varchar(32) NOT NULL,
  `sampling_info` text NOT NULL,
  `sample_description` text NOT NULL,
  `sequencing_platform` varchar(32) NOT NULL,
  `target_gene` varchar(32) NOT NULL,
  `extraction_DNA_mass` varchar(32) NOT NULL,
  `extraction_DNA_size` text NOT NULL,
  `extraction_DNA_method` text NOT NULL,
  `primers` text NOT NULL,
  `primers_sequence` text NOT NULL,
  `pH` varchar(32) NOT NULL,
  `pH_method` varchar(64) NOT NULL,
  `organic_matter_content` varchar(32) NOT NULL,
  `total_C_content` varchar(32) NOT NULL,
  `total_N_content` varchar(32) NOT NULL,
  `total_P` varchar(32) NOT NULL,
  `total_Ca` varchar(32) NOT NULL,
  `total_K` varchar(32) NOT NULL,
  `plants_dominant` text NOT NULL,
  `plants_all` text NOT NULL,
  `sample_info` text NOT NULL,
  `sample_seqid` text NOT NULL,
  `sample_barcode` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `samples`
--

DROP TABLE IF EXISTS `samples`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `samples` (
  `id` int(11) NOT NULL,
  `add_date` varchar(10) NOT NULL,
  `paper_id` varchar(32) NOT NULL,
  `title` text NOT NULL,
  `year` varchar(4) NOT NULL,
  `authors` text NOT NULL,
  `journal` text NOT NULL,
  `doi` text NOT NULL,
  `contact` text NOT NULL,
  `sample_name` text NOT NULL,
  `sample_type` text NOT NULL,
  `manipulated` varchar(5) NOT NULL,
  `sample_description` text NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `continent` varchar(32) NOT NULL,
  `year_of_sampling` varchar(32) NOT NULL,
  `Biome` text NOT NULL,
  `sequencing_platform` varchar(32) NOT NULL,
  `target_gene` varchar(32) NOT NULL,
  `primers` text NOT NULL,
  `primers_sequence` text NOT NULL,
  `sample_seqid` text NOT NULL,
  `sample_barcode` text NOT NULL,
  `elevation` varchar(32) NOT NULL,
  `MAT` varchar(32) NOT NULL,
  `MAP` varchar(32) NOT NULL,
  `MAT_study` varchar(32) NOT NULL,
  `MAP_study` varchar(32) NOT NULL,
  `Biome_detail` text NOT NULL,
  `country` text NOT NULL,
  `month_of_sampling` varchar(32) NOT NULL,
  `day_of_sampling` varchar(32) NOT NULL,
  `plants_dominant` text NOT NULL,
  `plants_all` text NOT NULL,
  `area_sampled` varchar(32) NOT NULL,
  `number_of_subsamples` varchar(32) NOT NULL,
  `sampling_info` text NOT NULL,
  `sample_depth` varchar(32) NOT NULL,
  `extraction_DNA_mass` varchar(32) NOT NULL,
  `extraction_DNA_size` text NOT NULL,
  `extraction_DNA_method` text NOT NULL,
  `total_C_content` varchar(32) NOT NULL,
  `total_N_content` varchar(32) NOT NULL,
  `organic_matter_content` varchar(32) NOT NULL,
  `pH` varchar(32) NOT NULL,
  `pH_method` varchar(64) NOT NULL,
  `total_Ca` varchar(32) NOT NULL,
  `total_P` varchar(32) NOT NULL,
  `total_K` varchar(32) NOT NULL,
  `sample_info` text NOT NULL,
  `location` text NOT NULL,
  `area_GPS` varchar(32) NOT NULL,
  `ITS1_extracted` int(11) NOT NULL,
  `ITS2_extracted` int(11) NOT NULL,
  `ITS_total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sh_migrated`
--

DROP TABLE IF EXISTS `sh_migrated`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sh_migrated` (
  `id` varchar(36) NOT NULL,
  `sh_name` varchar(255) DEFAULT NULL,
  `sample_id` int(11) DEFAULT NULL,
  `abundance` int(11) DEFAULT NULL,
  `variants` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `study`
--

DROP TABLE IF EXISTS `study`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `study` (
  `hash` varchar(32) NOT NULL,
  `contributor` text NOT NULL,
  `email` text NOT NULL,
  `affiliation_institute` text NOT NULL,
  `affiliation_country` text NOT NULL,
  `ORCID` text NOT NULL,
  `title` text NOT NULL,
  `authors` text NOT NULL,
  `year` text NOT NULL,
  `journal` text NOT NULL,
  `volume` text NOT NULL,
  `pages` text NOT NULL,
  `doi` text NOT NULL,
  `repository` text NOT NULL,
  `include` text NOT NULL,
  `coauthor` text NOT NULL,
  `email_confirmed` int(11) NOT NULL,
  `submission_finished` int(11) NOT NULL,
  `date` varchar(32) NOT NULL,
  PRIMARY KEY (`hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `taxonomy_migrated`
--

DROP TABLE IF EXISTS `taxonomy_migrated`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taxonomy_migrated` (
  `id` varchar(36) NOT NULL,
  `sh` varchar(32) NOT NULL,
  `kingdom` varchar(64) NOT NULL,
  `phylum` varchar(64) NOT NULL,
  `class` varchar(64) NOT NULL,
  `order` varchar(64) NOT NULL,
  `family` varchar(64) NOT NULL,
  `genus` varchar(64) NOT NULL,
  `species` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `traffic`
--

DROP TABLE IF EXISTS `traffic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `traffic` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `session` int(11) NOT NULL,
  `category` varchar(32) DEFAULT NULL,
  `value` varchar(64) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `variants_migrated`
--

DROP TABLE IF EXISTS `variants_migrated`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `variants_migrated` (
  `id` varchar(36) NOT NULL,
  `sequence` varchar(5000) DEFAULT NULL,
  `sample_id` int(11) DEFAULT NULL,
  `abundance` int(11) DEFAULT NULL,
  `marker` varchar(255) DEFAULT NULL,
  `sh` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-23 14:53:41
