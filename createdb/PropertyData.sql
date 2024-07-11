-- Create the database
CREATE DATABASE PropertyData;

-- Use the created database
USE PropertyData;

-- Create the Place table
CREATE TABLE Place (
    PlaceID INT PRIMARY KEY,
    PlaceName VARCHAR(255)
);

-- Create the PropertyType table
CREATE TABLE PropertyType (
    PropertyTypeID INT PRIMARY KEY,
    TypeName VARCHAR(255)
);

-- Create the Property table
CREATE TABLE Property (
    PropertyID INT PRIMARY KEY AUTO_INCREMENT,
    Address VARCHAR(255),
    PlaceID INT,
    ListYear INT,
    AssessedValue DECIMAL(10, 2),
    SaleAmount DECIMAL(10, 2),
    SalesRatio FLOAT,
    PropertyTypeID INT,
    ResidentialType VARCHAR(255),
    FOREIGN KEY (PlaceID) REFERENCES Place(PlaceID),
    FOREIGN KEY (PropertyTypeID) REFERENCES PropertyType(PropertyTypeID)
);

-- Create the RetailStore table
CREATE TABLE RetailStore (
    RetailStoreID INT PRIMARY KEY AUTO_INCREMENT,
    LicenseNumber VARCHAR(50),
    StoreName VARCHAR(255),
    PlaceID INT,
    OperationType VARCHAR(255),
    EntityName VARCHAR(255),
    DBAName VARCHAR(255),
    FOREIGN KEY (PlaceID) REFERENCES Place(PlaceID)
);

-- Create the CrimeData table
CREATE TABLE CrimeData (
    CrimeID INT PRIMARY KEY AUTO_INCREMENT,
    CaseNumber VARCHAR(50),
    PlaceID INT,
    OtherCrimeDetails VARCHAR(255),  -- Placeholder for other crime-specific columns
    FOREIGN KEY (PlaceID) REFERENCES Place(PlaceID)
);
