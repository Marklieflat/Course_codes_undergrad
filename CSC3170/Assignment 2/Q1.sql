SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

DROP SCHEMA IF EXISTS `as3` ;
CREATE SCHEMA IF NOT EXISTS `as3` DEFAULT CHARACTER SET utf8 ;
USE `as3` ;

-- -----------------------------------------------------
-- Create below: Table `as3`.`regions`
-- -----------------------------------------------------
create table if not exists `as3`.`regions`(
	`REGION_ID` decimal(5,0) not null,
    `REGION_NAME` varchar(25) not null,
	primary key (`REGION_ID`)
);

-- -----------------------------------------------------
-- Create below: Table `as3`.`countries`
-- -----------------------------------------------------
create table if not exists `as3`.`countries`(
	`COUNTRY_ID` char(2) not null,
    `COUNTRY_NAME` varchar(40) not null,
    `REGION_ID` decimal(5,0) not null,
    primary key (`COUNTRY_ID`),
    foreign key (`REGION_ID`) references `as3`.`regions`(`REGION_ID`)
);

-- -----------------------------------------------------
-- Create below: Table `as3`.`locations`
-- -----------------------------------------------------
create table if not exists `as3`.`locations`(
	`LOCATION_ID` decimal(4,0) not null,
    `STREET_ADDRESS` varchar(40),
    `POSTAL_CODE` varchar(12),
    `CITY` varchar(30) not null,
    `STATE_PROVINCE` varchar(25),
    `COUNTRY_ID` char(2) not null,
    primary key (`LOCATION_ID`),
    foreign key (`COUNTRY_ID`) references `as3`.`countries`(`COUNTRY_ID`)
);

-- -----------------------------------------------------
-- Create below: Table `as3`.`jobs`
-- -----------------------------------------------------
create table if not exists `as3`.`jobs`(
	`JOB_ID` varchar(10) not null,
    `JOB_TITLE` varchar(35) not null,
    `MIN_SALARY` decimal(6,0),
    `MAX_SALARY` decimal(6,0),
    primary key (`JOB_ID`)
);

-- -----------------------------------------------------
-- Create below: Table `as3`.`employees`
-- -----------------------------------------------------
create table if not exists `as3`.`employees`(
	`EMPLOYEE_ID` decimal(6,0) not null,
    `FIRST_NAME` varchar(20),
    `LAST_NAME` varchar(25) not null,
    `EMAIL` varchar(25) not null,
    `PHONE_NUMBER` varchar(20),
    `HIRE_DATE` date not null,
    `JOB_ID` varchar(10) not null,
    `SALARY` decimal(8,2) not null,
    `COMMISSION_PCT` decimal(2,2) null default null,
    `MANAGER_ID` decimal(6,0) not null,
    `DEPARTMENT_ID` decimal(4,0) not null,
    primary key (`EMPLOYEE_ID`),
    foreign key (`JOB_ID`) references `as3`.`jobs`(`JOB_ID`),
    foreign key (`DEPARTMENT_ID`) references `as3`.`departments`(`DEPARTMENT_ID`),
    foreign key (`MANAGER_ID`) references `as3`.`employees` (`EMPLOYEE_ID`)
);

-- -----------------------------------------------------
-- Create below: Table `as3`.`departments`
-- -----------------------------------------------------
create table if not exists `as3`.`departments`(
	`DEPARTMENT_ID` decimal(4,0) not null,
    `DEPARTMENT_NAME` varchar(30) not null,
    `MANAGER_ID` decimal(6,0),
    `LOCATION_ID` decimal(4,0) not null,
    primary key (`DEPARTMENT_ID`),
    foreign key (`LOCATION_ID`) references `as3`.`locations`(`LOCATION_ID`),
    foreign key (`MANAGER_ID`) references `as3`.`employees` (`EMPLOYEE_ID`)
);

-- -----------------------------------------------------
-- Create below: Table `as3`.`job_history`
-- -----------------------------------------------------
create table if not exists `as3`.`job_history`(
	`EMPLOYEE_ID` decimal(6,0) not null,
    `START_DATE` date not null,
    `END_DATE` date not null,
    `JOB_ID` varchar(10) not null,
    `DEPARTMENT_ID` decimal(4,0) not null,
    primary key (`EMPLOYEE_ID`, `START_DATE`),
    foreign key (`EMPLOYEE_ID`) references `as3`.`employees`(`EMPLOYEE_ID`),
    foreign key (`JOB_ID`) references `as3`.`jobs`(`JOB_ID`),
    foreign key (`DEPARTMENT_ID`) references `as3`.`departments`(`DEPARTMENT_ID`)
);

-- -----------------------------------------------------
-- End of coding
-- -----------------------------------------------------

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
