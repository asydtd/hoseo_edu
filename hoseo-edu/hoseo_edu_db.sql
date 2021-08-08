-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.5.9-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- hoseoedudb 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `hoseoedudb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `hoseoedudb`;

-- 테이블 hoseoedudb.tb_sensor_upload 구조 내보내기
CREATE TABLE IF NOT EXISTS `tb_sensor_upload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_ip` varchar(50) DEFAULT '',
  `company_id` varchar(50) DEFAULT '',
  `sensors_msg` text DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `indexname` (`created_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 hoseoedudb.tb_sensor_upload:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `tb_sensor_upload` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_sensor_upload` ENABLE KEYS */;

-- 테이블 hoseoedudb.tb_sensor_upload_encrypt 구조 내보내기
CREATE TABLE IF NOT EXISTS `tb_sensor_upload_encrypt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_ip` varchar(50) DEFAULT '',
  `company_id` varchar(50) DEFAULT '',
  `sensors_msg` text DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `indexname` (`created_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 hoseoedudb.tb_sensor_upload_encrypt:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `tb_sensor_upload_encrypt` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_sensor_upload_encrypt` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
