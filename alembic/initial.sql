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
-- Table structure for table `ChemicalData`
--

DROP TABLE IF EXISTS `ChemicalData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ChemicalData` (
  `id` varchar(36) NOT NULL,
  `total_c_content` float DEFAULT NULL,
  `total_n_content` float DEFAULT NULL,
  `organic_matter_content` float DEFAULT NULL,
  `ph` float DEFAULT NULL,
  `ph_method` varchar(64) DEFAULT NULL,
  `total_ca` float DEFAULT NULL,
  `total_p` float DEFAULT NULL,
  `total_k` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `EnvData`
--

DROP TABLE IF EXISTS `EnvData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EnvData` (
  `id` varchar(36) NOT NULL,
  `biome` varchar(32) DEFAULT NULL,
  `biome_detail` text DEFAULT NULL,
  `plants_dominant` text DEFAULT NULL,
  `plants_all` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Paper`
--

DROP TABLE IF EXISTS `Paper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Paper` (
  `id` varchar(36) NOT NULL,
  `internal_id` text DEFAULT NULL,
  `title` text DEFAULT NULL,
  `authors` text DEFAULT NULL,
  `journal` text DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `doi` text DEFAULT NULL,
  `contact` text DEFAULT NULL,
  `area_gps` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Samples_migrated`
--

DROP TABLE IF EXISTS `Samples_migrated`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Samples_migrated` (
  `id` varchar(36) NOT NULL,
  `original_id` varchar(36) DEFAULT NULL,
  `add_date` date DEFAULT NULL,
  `paper_id` varchar(36) DEFAULT NULL,
  `chemical_data_id` varchar(36) DEFAULT NULL,
  `env_data_id` varchar(36) DEFAULT NULL,
  `sampling_data_id` varchar(36) DEFAULT NULL,
  `sequencing_data_id` varchar(36) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `sample_info` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `paper_id` (`paper_id`),
  KEY `chemical_data_id` (`chemical_data_id`),
  KEY `env_data_id` (`env_data_id`),
  KEY `sampling_data_id` (`sampling_data_id`),
  KEY `sequencing_data_id` (`sequencing_data_id`),
  CONSTRAINT `samples_migrated_ibfk_1` FOREIGN KEY (`paper_id`) REFERENCES `Paper` (`id`) ON DELETE SET NULL,
  CONSTRAINT `samples_migrated_ibfk_2` FOREIGN KEY (`chemical_data_id`) REFERENCES `ChemicalData` (`id`) ON DELETE SET NULL,
  CONSTRAINT `samples_migrated_ibfk_3` FOREIGN KEY (`env_data_id`) REFERENCES `EnvData` (`id`) ON DELETE SET NULL,
  CONSTRAINT `samples_migrated_ibfk_4` FOREIGN KEY (`sampling_data_id`) REFERENCES `SamplingData` (`id`) ON DELETE SET NULL,
  CONSTRAINT `samples_migrated_ibfk_5` FOREIGN KEY (`sequencing_data_id`) REFERENCES `SequencingData` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `SamplingData`
--

DROP TABLE IF EXISTS `SamplingData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SamplingData` (
  `id` varchar(36) NOT NULL,
  `sample_name` text DEFAULT NULL,
  `sample_type` varchar(32) DEFAULT NULL,
  `manipulated` tinyint(1) DEFAULT NULL,
  `sample_type_detailed` text DEFAULT NULL,
  `date_of_sampling` date DEFAULT NULL,
  `area_sampled` float DEFAULT NULL,
  `number_of_subsamples` int(11) DEFAULT NULL,
  `sampling_info` text DEFAULT NULL,
  `sample_depth_from` float DEFAULT NULL,
  `sample_depth_to` float DEFAULT NULL,
  `mat` float DEFAULT NULL,
  `map` float DEFAULT NULL,
  `external_mat` float DEFAULT NULL,
  `external_map` float DEFAULT NULL,
  `sample_seqid` text DEFAULT NULL,
  `sample_barcode` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `SequencingData`
--

DROP TABLE IF EXISTS `SequencingData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SequencingData` (
  `id` varchar(36) NOT NULL,
  `sequencing_platform` varchar(32) DEFAULT NULL,
  `target_gene` varchar(32) DEFAULT NULL,
  `primers` text DEFAULT NULL,
  `primers_sequence` text DEFAULT NULL,
  `extraction_dna_mass` float DEFAULT NULL,
  `extraction_dna_size` text DEFAULT NULL,
  `extraction_dna_method` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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

-- Dump completed on 2023-11-12 17:16:13
