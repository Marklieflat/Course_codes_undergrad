-- -----------------------------------------------------
-- ---------------- Solution for Q1 --------------------
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Meta Data Settings: Leave These Unchanged
-- -----------------------------------------------------
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Drop Schema `as2`: Leave It Unchanged
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `as2`;

-- -----------------------------------------------------
-- Create Schema `as2`: Leave It Unchanged
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `as2` DEFAULT CHARACTER SET utf8;
USE `as2`;

-- -----------------------------------------------------
-- Create Table `regions` here
-- -----------------------------------------------------
create table regions(
    REGION_ID int(5) not null,
    REGION_NAME varchar(25) not null
);


-- -----------------------------------------------------
-- Create Table `countries` here
-- -----------------------------------------------------
create table countries(
    COUNTRY_ID char(2) not null,
    COUNTRY_NAME varchar(45) not null,
    REGION_ID int(5) not null
);


-- -----------------------------------------------------
-- Create Table `locations` here
-- -----------------------------------------------------
create table locations(
    LOCATION_ID int(4),
    STREET_ADDRESS varchar(40),
    POSTAL_CODE varchar(12),
    CITY varchar(30) not null,
    STATE_PROVINCE varchar(25),
    COUNTRY_ID char(2) not null
);


-- -----------------------------------------------------
-- Create Table `jobs` here
-- -----------------------------------------------------
create table jobs(
    JOB_ID varchar(10),
    JOB_TITLE varchar(35) not null,
    MIN_SALARY int(6),
    MAX_SALARY int(6)
);


-- -----------------------------------------------------
-- Create Table `employees` here
-- -----------------------------------------------------
create table employees(
    EMPLOYEE_ID int(6),
    FIRST_NAME varchar(20),
    LAST_NAME varchar(25) not null,
    EMAIL varchar(25) not null,
    PHONE_NUMBER varchar(20),
    HIRE_DATE varchar(10),
    JOB_ID char(10),
    SALARY numeric(10,2),
    COMMISSION_PCT numeric(5,2),
    MANAGER_ID int(6),
    DEPARTMENT_ID int(10)
);


-- -----------------------------------------------------
-- Create Table `departments` here
-- -----------------------------------------------------
create table departments(
    DEPARTMENT_ID int(10),
    DEPARTMENT_NAME varchar(45) not null,
    MANAGER_ID int(6),
    LOCATION_ID int(4)
);


-- -----------------------------------------------------
-- Create Table `job_history` here
-- -----------------------------------------------------
create table job_history(
    EMPLOYEE_ID int(6),
    START_DATE varchar(45) not null,
    END_DATE varchar(45) not null,
    JOB_ID char(10),
    DEPARTMENT_ID int(10)
);

-- -----------------------------------------------------
-- Recover Meta Data: Leave These Unchanged
-- -----------------------------------------------------
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
