-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 08, 2022 at 09:32 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `resumeshortlisting`
--

-- --------------------------------------------------------

--
-- Table structure for table `jobposting`
--

CREATE TABLE `jobposting` (
  `id` int(10) NOT NULL,
  `company_id` int(10) NOT NULL,
  `skills` varchar(100) NOT NULL,
  `experience` int(10) NOT NULL,
  `education` varchar(50) NOT NULL,
  `city` text NOT NULL,
  `generated_link` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `recruiter`
--

CREATE TABLE `recruiter` (
  `id` int(10) NOT NULL,
  `company_email` varchar(100) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recruiter`
--

INSERT INTO `recruiter` (`id`, `company_email`, `company_name`, `password`) VALUES
(1, 'prteu34@gmail.com', 'xyz', '12345678'),
(2, 'harjanihema52@gmail.com', 'abc', 'qwerty'),
(3, 'preetiharjani1382@gmail.com', 'food', 'food123'),
(4, 'prteu35@gmail.com', 'food@', 'food@123'),
(5, 'harjanihema55@gmail.com', 'wipro', '123preeti');

-- --------------------------------------------------------

--
-- Table structure for table `resume_details`
--

CREATE TABLE `resume_details` (
  `id` int(10) NOT NULL,
  `job_id` int(10) NOT NULL,
  `template_id` int(10) NOT NULL,
  `name` text NOT NULL,
  `dob` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `contact_number` int(12) NOT NULL,
  `address` varchar(100) NOT NULL,
  `title` varchar(50) NOT NULL,
  `skills` varchar(100) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `position` varchar(50) NOT NULL,
  `worked_from` date NOT NULL,
  `worked_to` date NOT NULL,
  `description` varchar(100) NOT NULL,
  `project_title` varchar(50) NOT NULL,
  `project_description` varchar(150) NOT NULL,
  `tech_used` varchar(100) NOT NULL,
  `education` varchar(80) NOT NULL,
  `languages_known` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jobposting`
--
ALTER TABLE `jobposting`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recruiter`
--
ALTER TABLE `recruiter`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `resume_details`
--
ALTER TABLE `resume_details`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jobposting`
--
ALTER TABLE `jobposting`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `recruiter`
--
ALTER TABLE `recruiter`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `resume_details`
--
ALTER TABLE `resume_details`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
