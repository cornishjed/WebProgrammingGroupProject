-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 04, 2019 at 02:16 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

-- Jed Powell (webair, seats)
-- Joseph Ele (pastbookings,fares, times_train)
-- Dariusz Kwiatkowski ( times_taxi)

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webprog`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `find_all` ()  BEGIN
 SELECT id, name 
 FROM animals; 
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `find_by_id` (IN `a_id` INT(11), OUT `a_name` VARCHAR(20))  BEGIN
 	SELECT name INTO a_name FROM animals
 	WHERE id = a_id;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `fName` varchar(30) CHARACTER SET latin1 NOT NULL,
  `lName` varchar(30) CHARACTER SET latin1 NOT NULL,
  `tel` int(15) NOT NULL,
  `email` varchar(30) CHARACTER SET latin1 NOT NULL,
  `fromCity` varchar(30) CHARACTER SET latin1 NOT NULL,
  `toCity` varchar(30) CHARACTER SET latin1 NOT NULL,
  `date` date NOT NULL,
  `fare` int(2) NOT NULL,
  `bookingId` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- --------------------------------------------------------

--
-- Table structure for table `fares`
--

CREATE TABLE `fares` (
  `FromSt` varchar(20) NOT NULL,
  `Destination` varchar(20) NOT NULL,
  `WebAir` int(11) NOT NULL,
  `WebTaxi` int(11) NOT NULL,
  `WebBus` float NOT NULL,
  `WebTrain` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fares`
--

INSERT INTO `fares` (`FromSt`, `Destination`, `WebAir`, `WebTaxi`, `WebBus`, `WebTrain`) VALUES
('Cardiff', 'Edinburgh', 60, 180, 15, 100),
('Aberdeen', 'Portsmouth', 65, 195, 16.5, 130),
('Newcastle', 'Birmingham', 65, 195, 16.5, 130),
('Newcastle', 'Manchester', 65, 195, 16.5, 130),
('Glasgow', 'Newcastle', 65, 195, 16.5, 130),
('London', 'Manchester', 65, 195, 16.5, 130),
('Birmingham', 'Newcastle', 65, 195, 16.5, 130),
('Edinburgh', 'Cardiff', 60, 180, 15, 0),
('Southampton', 'Manchester', 50, 150, 12.5, 100),
('Portsmouth', 'Dundee', 90, 270, 0, 0),
('Dundee', 'Portsmouth', 90, 270, 22.5, 180),
('Bristol', 'Manchester', 50, 150, 12.5, 100),
('Bristol', 'Newcastle', 70, 210, 18, 140),
('Bristol', 'Glasgow', 80, 0, 20, 160),
('Bristol', 'London', 50, 150, 12.5, 100),
('Manchester', 'Southampton', 50, 0, 12.5, 100),
('Manchester', 'Bristol', 50, 150, 12.5, 100),
('Manchester', 'Glasgow', 65, 0, 16.5, 130),
('Newcastle', 'Bristol', 70, 210, 17.5, 140);

-- --------------------------------------------------------

--
-- Table structure for table `pastbookings`
--

CREATE TABLE `pastbookings` (
  `CustomerName` varchar(20) NOT NULL,
  `BookingNr` char(20) NOT NULL,
  `Froms` varchar(20) NOT NULL,
  `Destination` varchar(20) NOT NULL,
  `PassengerNR` int(20) NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pastbookings`
--

INSERT INTO `pastbookings` (`CustomerName`, `BookingNr`, `Froms`, `Destination`, `PassengerNR`, `Date`) VALUES
('jessica', '0', 'Bristol', 'Manchester', 0, '0000-00-00'),
('JessicaAlba', '0', 'Aberdeen', 'Portsmouth', 4, '2019-04-10'),
('JessicaAlba', 'd9h6e5', 'Aberdeen', 'Portsmouth', 4, '2019-04-10'),
('Jessiej', 'd5o4m2', 'Aberdeen', 'Portsmouth', 3, '2019-04-10'),
('Jessiej', 'h1s6P1', 'Aberdeen', 'Portsmouth', 3, '2019-04-10'),
('Jessiej', 'd5d9r6', 'Aberdeen', 'Portsmouth', 3, '2019-04-10'),
('dsada', 'e3i2s1', 'Bristol', 'Newcastle', 2, '2019-04-05'),
('sdasd', 'r3f0i5', 'Cardiff', 'Edinburgh', 2, '2019-04-05'),
('Jed Powell', 'a5r7t5', 'Bristol', 'Manchester', 5, '2019-04-13'),
('Jed Powell', 'o8s3e6', 'Bristol', 'Manchester', 5, '2019-04-13');

-- --------------------------------------------------------

--
-- Table structure for table `seats`
--

CREATE TABLE `seats` (
  `departing_from` varchar(30) CHARACTER SET latin1 NOT NULL,
  `arriving_to` varchar(30) CHARACTER SET latin1 NOT NULL,
  `date` date NOT NULL,
  `seatno` int(11) NOT NULL DEFAULT '60'
) ENGINE=InnoDB DEFAULT CHARSET=ascii COLLATE=ascii_bin;

--
-- Dumping data for table `seats`
--

INSERT INTO `seats` (`departing_from`, `arriving_to`, `date`, `seatno`) VALUES
('Aberdeen', 'Portsmouth', '2019-04-18', 61),
('Bristol', 'Newcastle', '2005-04-19', 1),
('Aberdeen', 'Portsmouth', '2011-04-19', 1),
('Birmingham', 'Newcastle', '2025-04-19', 4),
('Birmingham', 'Newcastle', '2025-04-19', 4),
('Aberdeen', 'Portsmouth', '2019-04-25', 1),
('Aberdeen', 'Portsmouth', '2025-04-19', 1),
('Aberdeen', 'Portsmouth', '2019-04-10', 1),
('Cardiff', 'Edinburgh', '2019-04-12', 1);

-- --------------------------------------------------------

--
-- Table structure for table `times_taxi`
--

CREATE TABLE `times_taxi` (
  `Start` varchar(20) NOT NULL,
  `Departure` time NOT NULL,
  `Dest` varchar(20) NOT NULL,
  `Arrival` time NOT NULL,
  `Price` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `times_taxi`
--

INSERT INTO `times_taxi` (`Start`, `Departure`, `Dest`, `Arrival`, `Price`) VALUES
('Cardiff', '06:00:00', 'Edinburgh', '17:10:00', 180),
('Newcastle', '16:45:00', 'Bristol', '00:50:00', 195),
('Bristol', '08:00:00', 'Newcastle', '16:05:00', 210),
('Bristol', '11:30:00', 'Manchester', '18:30:00', 150),
('Manchester', '12:20:00', 'Bristol', '19:20:00', 150),
('Bristol', '07:40:00', 'London', '14:20:00', 150),
('London', '11:00:00', 'Manchester', '19:40:00', 195),
('Glasgow', '14:30:00', 'Newcastle', '22:35:00', 195),
('Newcastle', '16:15:00', 'Manchester', '20:05:00', 195),
('Manchester', '18:25:00', 'Bristol', '04:00:00', 150),
('Bristol', '06:20:00', 'Manchester', '13:20:00', 150),
('Portsmouth', '12:00:00', 'Dundee', '02:00:00', 195),
('Dundee', '10:00:00', 'Portsmouth', '00:00:00', 195),
('Southampton', '12:00:00', 'Manchester', '21:10:00', 150),
('Birmingham', '16:00:00', 'Newcastle', '01:10:00', 195),
('Newcastle', '06:00:00', 'Birmingham', '15:10:00', 195),
('Aberdeen', '07:00:00', 'Portsmouth', '21:00:00', 195),
('Edinburgh', '18:30:00', 'Cardiff', '03:40:00', 180);

-- --------------------------------------------------------

--
-- Table structure for table `times_train`
--

CREATE TABLE `times_train` (
  `Leaves` varchar(20) NOT NULL,
  `Start` time NOT NULL,
  `Arrives` varchar(20) NOT NULL,
  `End` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `times_train`
--

INSERT INTO `times_train` (`Leaves`, `Start`, `Arrives`, `End`) VALUES
('Cardiff', '06:00:00', 'Edinburgh', '11:20:00'),
('Newcastle', '16:45:00', 'Bristol', '21:45:00'),
('Bristol', '08:00:00', 'Newcastle', '13:00:00'),
('Bristol', '11:30:00', 'Manchester', '15:30:00'),
('Manchester', '12:20:00', 'Bristol', '16:20:00'),
('Bristol', '07:40:00', 'London', '11:40:00'),
('London', '11:00:00', 'Manchester', '16:20:00'),
('Manchester', '12:20:00', 'Glasgow', '17:20:00'),
('Bristol', '07:40:00', 'Glasgow', '12:00:00'),
('Glasgow', '14:30:00', 'Newcastle', '19:30:00'),
('Newcastle', '16:15:00', 'Manchester', '18:15:00'),
('Manchester', '18:25:00', 'Bristol', '23:25:00'),
('Bristol', '06:20:00', 'Manchester', '10:20:00'),
('Dundee', '10:00:00', 'Portsmouth', '18:00:00'),
('Southampton', '12:00:00', 'Manchester', '17:20:00'),
('Manchester', '18:25:00', 'Southampton', '00:20:00'),
('Birmingham', '16:00:00', 'Newcastle', '21:20:00'),
('Newcastle', '06:00:00', 'Birmingham', '11:20:00'),
('Aberdeen', '07:00:00', 'Portsmouth', '15:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `webair`
--

CREATE TABLE `webair` (
  `journeyid` int(3) NOT NULL,
  `departing_from` varchar(20) CHARACTER SET latin1 DEFAULT NULL,
  `departure_time` time DEFAULT NULL,
  `arriving_at` varchar(20) CHARACTER SET latin1 DEFAULT NULL,
  `arrival_time` time DEFAULT NULL,
  `fare` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=ascii COLLATE=ascii_bin;

--
-- Dumping data for table `webair`
--

INSERT INTO `webair` (`journeyid`, `departing_from`, `departure_time`, `arriving_at`, `arrival_time`, `fare`) VALUES
(1, 'Newcastle', '16:45:00', 'Bristol', '18:00:00', 70),
(2, 'Bristol', '08:00:00', 'Newcastle', '09:15:00', 70),
(3, 'Cardiff', '06:00:00', 'Edinburgh', '07:30:00', 60),
(4, 'Bristol', '11:30:00', 'Manchester', '12:30:00', 50),
(5, 'Manchester', '12:20:00', 'Bristol', '13:20:00', 50),
(6, 'Bristol', '07:40:00', 'London', '08:20:00', 50),
(8, 'London', '11:00:00', 'Manchester', '12:20:00', 65),
(9, 'Manchester', '12:20:00', 'Glasgow', '13:30:00', 65),
(10, 'Bristol', '07:40:00', 'Glasgow', '08:45:00', 80),
(11, 'Glasgow', '14:30:00', 'Newcastle', '15:45:00', 65),
(12, 'Newcastle', '16:15:00', 'Manchester', '17:05:00', 65),
(13, 'Manchester', '18:25:00', 'Bristol', '19:30:00', 50),
(14, 'Bristol', '06:20:00', 'Manchester', '07:20:00', 50),
(15, 'Portsmouth', '12:00:00', 'Dundee', '14:00:00', 90),
(16, 'Edinburgh', '18:30:00', 'Cardiff', '20:00:00', 65),
(17, 'Southampton', '12:00:00', 'Manchester', '13:30:00', 65),
(18, 'Birmingham', '16:00:00', 'Newcastle', '17:30:00', 65),
(19, 'Newcastle', '06:00:00', 'Birmingham', '07:30:00', 65),
(20, 'Aberdeen', '07:00:00', 'Portsmouth', '09:00:00', 65);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `webair`
--
ALTER TABLE `webair`
  ADD PRIMARY KEY (`journeyid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
