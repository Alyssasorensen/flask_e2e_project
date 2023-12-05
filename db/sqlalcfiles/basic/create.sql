CREATE TABLE health_statistics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT NOT NULL,
    male FLOAT NOT NULL,
    female FLOAT NOT NULL
);

INSERT INTO health_statistics (year, male, female)
VALUES
    (2019, 14.9, 15.6),
    (2020, 13.2, 14.4),
    (2021, 13.2, 13.9),
    (2022, 13.8, 15.2);

CREATE TABLE additional_health_statistics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT NOT NULL,
    male FLOAT NOT NULL,
    female FLOAT NOT NULL
);

INSERT INTO additional_health_statistics (year, male, female)
VALUES
    (2019, 8.4, 13.7),
    (2020, 8.1, 14.1),
    (2021, 8.4, 14.1),
    (2022, 9.7, 15.5);

CREATE TABLE location_health_statistics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(255) NOT NULL,
    all_women FLOAT NOT NULL,
    non_hispanic_white FLOAT NOT NULL,
    non_hispanic_black FLOAT NOT NULL,
    hispanic FLOAT NOT NULL,
    asian_and_pacific_islander FLOAT NOT NULL,
    american_indian_alaska_native FLOAT NOT NULL,
    other FLOAT NOT NULL
);

INSERT INTO location_health_statistics (location, all_women, non_hispanic_white, non_hispanic_black, hispanic, asian_and_pacific_islander, american_indian_alaska_native, other)
VALUES
    ('United States', 0.71, 0.72, 0.77, 0.67, 0.67, 0.62, 0.61),
    ('Alabama', 0.74, 0.72, 0.82, 0.65, 0.81, 0.64, 0.61),
    ('Alaska',0.62,0.61,0.75,0.53,0.57,0.68,0.62),
	('Arizona',0.67,0.68,0.71,0.68,0.71,0.54,0.69),
	('Arkansas',0.68,0.69,0.76,0.56,NSD,0.6,0.59),
	('California',0.7,0.72,0.78,0.66,0.67,0.69,0.6),
	('Colorado',0.66,0.68,0.71,0.61,0.66,0.53,0.53),
	('Connecticut',0.78,0.79,0.8,0.75,0.56,0.61,0.74),
	('Delaware',0.75,0.74,0.82,0.72,0.59,0.59,0.68),
	('District of Columbia',0.71,0.68,0.74,0.75,0.61,NSD,0.69),
	('Florida',0.72,0.73,0.77,0.68,0.68,0.65,0.5),
	('Georgia',0.73,0.72,0.79,0.67,0.6,0.76,0.65),
	('Hawaii',0.74,0.68,0.54,0.78,0.78,NSD,0.72),
	('Idaho',0.63,0.64,NSD,0.51,0.56,0.63,0.46),
	('Illinois',0.67,0.67,0.73,0.64,0.55,NSD,0.46),
	('Indiana',0.71,0.72,0.74,0.69,0.56,0.48,0.48),
	('Iowa',0.73,0.74,0.83,0.65,0.47,0.64,0.52),
	('Kansas',0.69,0.7,0.79,0.67,0.56,0.66,0.61),
	('Kentucky',0.7,0.7,0.72,0.75,NSD,NSD,NSD),
	('Louisiana',0.77,0.75,0.86,0.74,0.9,0.49,0.57),
	('Maine',0.75,0.75,0.76,0.7,NSD,0.72,0.57),
	('Maryland',0.77,0.75,0.82,0.7,0.81,0.67,0.68),
	('Massachusetts',0.79,0.81,0.71,0.68,0.78,NSD,0.73),
	('Michigan',0.74,0.75,0.73,0.68,0.65,0.67,0.75),
	('Minnesota',0.74,0.75,0.73,0.63,0.63,0.6,0.64),
	('Mississippi',0.72,0.71,0.74,0.67,NSD,0.87,NSD),
	('Missouri',0.71,0.71,0.74,0.74,0.8,0.57,0.61),
	('Montana',0.69,0.7,NSD,0.63,0.83,0.55,0.5),
	('Nebraska',0.67,0.68,0.73,0.55,0.82,0.62,0.69),
	('Nevada',0.64,0.66,0.69,0.62,0.59,0.49,0.58),
	('New Hampshire',0.74,0.74,NSD,0.76,0.84,0.76,0.65),
	('New Jersey',0.71,0.71,0.78,0.69,0.68,0.55,0.72),
	('New Mexico',0.64,0.67,0.86,0.61,0.52,0.64),
	('New York',0.75,0.75,0.77,0.77,0.7,0.48,0.68),
	('North Carolina',0.74,0.73,0.79,0.59,0.71,0.85,0.52),
	('North Dakota',0.73,0.75,NSD,NSD,0.78,0.59,0.72),
	('Ohio',0.71,0.71,0.74,0.71,0.86,0.49,0.55),
	('Oklahoma',0.66,0.66,0.75,0.46,0.68,0.67,0.71),
	('Oregon',0.69,0.71,0.75,0.54,0.75,0.71,0.65),
	('Pennsylvania',0.72,0.72,0.8,0.63,0.63,NSD,0.69),
	('Rhode Island',0.8,0.81,0.8,0.73,0.71,NSD,0.61),
	('South Carolina',0.74,0.73,0.81,0.69,0.47,0.59,0.64),
	('South Dakota',0.73,0.74,0.85,0.82,0.66,0.54,0.72),
	('Tennessee',0.71,0.71,0.77,0.69,NSD,NSD,0.56),
	('Texas',0.68,0.68,0.78,0.67,0.56,0.64,0.57),
	('Utah',0.65,0.66,0.66,0.54,0.65,0.43,0.59),
	('Vermont',0.69,0.7,NSD,0.64,0.47,0.61,0.48),
	('Virginia',0.73,0.73,0.78,0.65,0.69,0.71,0.66),
	('Washington',0.69,0.7,0.67,0.62,0.63,0.63,0.63),
	('West Virginia',0.72,0.73,0.68,NSD,0.65,0.69,0.52),
	('Wisconsin',0.74,0.75,0.79,0.67,0.83,0.53,0.55),
	('Wyoming',0.62,0.62,0.7,0.64,NSD,0.54,0.61),
	('Guam',0.7,0.78,NSD,0.8,0.68,NSD,0.83),
	('Puerto Rico',0.76,NSD,NSD,0.76,NSD,NSD,NSD)